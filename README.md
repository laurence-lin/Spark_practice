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
