from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, lower, col

# Créer la session Spark
spark = SparkSession.builder \
    .appName("WordCount_DataFrame") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Lire le fichier depuis HDFS
df = spark.read.text("hdfs://namenode:9000/data/words.txt")

# Compter les mots
result = df.select(
        explode(
            split(lower(col("value")), " ")
        ).alias("word")
    ) \
    .groupBy("word") \
    .count() \
    .orderBy("count", ascending=False)

# Afficher les résultats
print("\n========== RÉSULTATS DATAFRAME ==========")
result.show()
print("==========================================\n")

spark.stop()
