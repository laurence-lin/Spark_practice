import socket
import sys
import requests
import requests_oauthlib
import json, os, yaml


WORK_DIR = "/Users/linyanliang/experiment/data_streaming/first_twitter"

with open(os.path.join(WORK_DIR, "secret.yml"), "r") as f:
    try:
        result = yaml.safe_load(f)

        CONSUMER_KEY = result["consumer_key"]
        CONSUMER_KEY_SECRET = result["consumer_key_secret"]
        ACCESS_TOKEN = result["access_token"]
        ACCESS_TOKEN_SECRET = result["access_token_secret"]
        BEARER_TOKEN = result["bearer_token"]

    except Exception as e:
        print("Error: ", e)

# Enter keyword and get tweets
my_auth = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def get_tweets(keyword: str):
    # Requests twitter posts with keyword filtered
    url = 'https://stream.twitter.com/1.1/statuses/filter.json'
    query_data = [('language', 'en'), ('track', keyword)]
    query_url = url + '?' + '&'.join([str(t[0]) + '=' + str(t[1]) for t in query_data])
    response = requests.get(query_url, auth=my_auth, stream=True)
    print(query_url, response)
    return response


def send_tweets_to_spark(http_resp, tcp_connection):
    # Given the twitter API response, extract text and send to Spark streaming
    for line in http_resp.iter_lines():
        try:
            full_tweet = json.loads(line)
            tweet_text = full_tweet['text']
            print("Tweet Text: " + tweet_text)
            print("------------------------------------------")
            tcp_connection.send((tweet_text + '\n').encode())  # send data in Bytes
        except Exception as E:
            print("Error occurs: ", E)
            e = sys.exc_info()[0]
            print("System Error: %s" % e)


# Get tweets with keyword, and send to Spark stream
KEY_WORDS = "ukraine"
TCP_IP = "localhost"
TCP_PORT = 9009
conn = None
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))  # socket bind to: localhost:9009
s.listen(1)  # socket start listening
print("Waiting for TCP connection...")
conn, addr = s.accept()  # socket accept connections: the one connected is Spark client
print("Connected... Starting getting tweets.")
resp = get_tweets(KEY_WORDS)
send_tweets_to_spark(resp, conn)

