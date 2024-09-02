Kafka ETL Pipeline
Overview
This project implements a real-time ETL (Extract, Transform, Load) pipeline using Apache Kafka and Python. The ETL pipeline ingests data from multiple sources through Kafka, performs data cleaning and validation to ensure data quality, and then loads the transformed data into a PostgreSQL data warehouse.

Features
- Real-time data ingestion using Apache Kafka.
- Data transformation with Pandas for cleaning, validation, and processing.
- Data loading into a PostgreSQL data warehouse using SQLAlchemy.
- Logging to track ETL operations.
- Modular design to support easy maintenance and scaling.

Getting Started
Prerequisites
Ensure you have the following software installed:

Python 3.8+
Apache Kafka
PostgreSQL

To work with it! :)
1. Clone the repository
    git clone https://github.com/JaniSisinni/kafka-etl-pipeline.git
    cd kafka-etl-pipeline

2. Set Up a Python Virtual Environment
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the Required Python Packages
    pip install -r requirements.txt

4. Set Up Apache Kafka --> Download and extract Kafka, Start Zookeeper and Kafka server
    bin/zookeeper-server-start.sh config/zookeeper.properties
    bin/kafka-server-start.sh config/server.properties

5. Create Kafka Topic --> Topic name: etl-topic
    bin/kafka-topics.sh --create --topic etl-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

6. Set Up PostgreSQL
    CREATE DATABASE etl_db;
    CREATE USER etl_user WITH ENCRYPTED PASSWORD 'your_password';
    GRANT ALL PRIVILEGES ON DATABASE etl_db TO etl_user;

7. Update the config/config.yaml file with your PostgreSQL credentials.

8. Configure the Kafka and PostgreSQL settings in config/config.yaml

9. Running the ETL Pipeline
    python src/main.py

10. Unit testing, run
    pytest tests/

Logging
Logs are stored in the logs/etl_pipeline.log file to track ETL operations and errors.

Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

Contact
For any questions or issues, please contact alejandra.sisinni@gmail.com


