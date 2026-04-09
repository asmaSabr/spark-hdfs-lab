from pyspark import SparkContext

# Créer le contexte Spark
sc = SparkContext("spark://spark-master:7077", "WordCount")
sc.setLogLevel("ERROR")
# Lire le fichier depuis HDFS
text = sc.textFile("hdfs://namenode:9000/data/words.txt")

# Compter les mots
counts = text.flatMap(lambda line: line.lower().split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b) \
             .sortBy(lambda x: x[1], ascending=False)

# Afficher les résultats
print("\n========== RÉSULTATS ==========")
for word, count in counts.collect():
    print(f"  {word} : {count}")
print("================================\n")

sc.stop()
