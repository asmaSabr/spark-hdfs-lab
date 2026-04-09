
# Lab 1 — Spark + HDFS Cluster with PySpark

## Description
This lab sets up a distributed Big Data environment using Docker Compose,
combining HDFS for distributed storage and Apache Spark for data processing.
A PySpark word count application is implemented and executed on the cluster.
## Architecture
![architecture](https://github.com/user-attachments/assets/460a2cfc-bcea-45d5-bccb-ec0192145677)

## Project Structure
```
spark-hdfs-lab/
├── docker-compose.yml        # Cluster definition (6 services)
├── .gitignore
└── app/
    ├── app.py                # Word count — RDD API
    ├── app_dataframe.py      # Word count — DataFrame API
    └── app_bonus.py          # Multi-file word count + save to HDFS
```
## How to Run

### Prerequisites
- Docker Desktop installed and running
- Git
- Minimum 4 GB RAM available

### 1. Clone the repository
```bash
git clone https://github.com/asmaSabr/spark-hdfs-lab.git
cd spark-hdfs-lab
```

### 2. Start the cluster
```bash
docker compose up -d
```
### 3. Verify all containers are running
```bash
docker ps
```
Expected output: 6 containers with status `Up`
- namenode
- datanode1
- datanode2
- spark-master
- spark-worker1
- spark-client
### 4. Check Web UIs
| Interface | URL |
|-----------|-----|
| HDFS NameNode | http://localhost:9870 |
| Spark Master  | http://localhost:8080 |
| Spark Worker  | http://localhost:8081 |

### 5. Upload data to HDFS
```bash
docker exec -it namenode bash

hdfs dfs -mkdir -p /data
echo "Hello Hadoop
Learning Spark
Learning Big Data" > /tmp/words.txt

hdfs dfs -put /tmp/words.txt /data/words.txt
hdfs dfs -ls /data
```
### 6. Submit the PySpark job
```bash
docker exec -it spark-client bash

/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --deploy-mode client \
  /opt/spark/app/app.py
```

### 7. Stop the cluster
```bash
# Stop containers (data is preserved)
docker compose down

# Stop and delete all data
docker compose down -v
```
