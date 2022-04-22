# Spark_practice
Experiment to apply spark for parallel computing

Basic service of Spark tools: provide API to perform massive distributed processing over resilient sets of data. 
For example:
Spark SQL: work with structured data
MLlib: scalable machine learning library




Deploy spark computing:

Spark work with RDD data architecture system and hadoop data storage. Resilient Distributed Dataset(RDD)'s advantage: 
1. Distributed storage, which is safe for data when one of the machine is crashed
2. Faster manipulation of data, support parallel computing over distributed engine that is helpful during big data applications.

Spark is written in Scala, run on Java environment, but support mulitple language API such as python. Pyspark is an efficient tool to deploy spark with python.

To start working on PySpark, we need to:

1. Install Spark package on your computer

2. Install Pyspark package with python pip


Pass the data to parallel collections: make data distributed in separate space, and could operate in parallel. 

distribute_data = sc.parallel(data)

The distribute_data is stored in RDD format.

To operate with RDD format data, there are two types of Ops in Spark: Transformation and Action

Transformation: create a new RDD after operation. EX: Map, filter, filtermap

Action: computation for the origin RDD. EX: collect, take, first, count.
Collect: fetch all RDD elements to the single driver machine. 

Spark working session and context:

In Spark shell, a SparkContext is auto-created for you to run. SparkContext stands for "sc" variable, that being an entry point to connect to Spark cluster.
Ex. sc.parallel(data)

Spark session: comparing to SparkContext for creating RDDs, Spark Session is an entry point to interact with Spark Dataframes. 
With datafrmae operations we could create, manipulate, execute SQL queries. 
variable of session: 'spark'








