# Spark_practice
Experiment to apply spark for parallel computing



Deploy spark computing:

Spark work with RDD data architecture system and hadoop data storage. 

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
