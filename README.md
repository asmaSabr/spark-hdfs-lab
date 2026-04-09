
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
