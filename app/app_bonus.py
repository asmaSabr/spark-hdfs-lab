from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, lower, col

spark = SparkSession.builder \
    .appName("WordCount_Bonus") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.read.text("hdfs://namenode:9000/data/words*.txt")

result = df.select(
        explode(
            split(lower(col("value")), " ")
        ).alias("word")
    ) \
    .groupBy("word") \
    .count() \
    .orderBy("count", ascending=False)

print("\n========== RÉSULTATS TOUS FICHIERS ==========")
result.show()
print("==============================================\n")

result.write.mode("overwrite").csv("hdfs://namenode:9000/data/output")

print("Resultats sauvegardes dans /data/output !")

spark.stop()
