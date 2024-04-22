# GreenDB

Towards Energy Efficient Databases

# Description

GreenDB makes use of the tool, DBJoules, a tool designed to measure the energy consumption of database queries across four databases, i.e., MySQL, PostgreSQL, MongoDB, and Couchbase. This tool measures the energy consumption of queries by gathering the information about CPU and RAM usage, by utilizing psutil package.

# System Requirements

1. Windows Operating System</li>
2. Have <a href="https://www.python.org/downloads/">Python</a>, <a href="https://dev.mysql.com/downloads/installer/">MySQL</a>, <a href="https://www.postgresql.org/download/">PostgreSQL</a>, <a href="https://www.mongodb.com/try/download/community">MongoDB</a>, <a href="https://www.couchbase.com/downloads/?family=couchbase-server">Couchbase</a> installed in your system.</li>


# Steps to run

1. Clone the repository
2. Navigate to the folder DBJoules ```cd DBJoules```
3. Run "setup.py" file to install necessary dependencies: ```python setup.py```
4. Run "stop_background_processes.py" file to stop all the currently running background processes ```python stop_background_processes.py```
5. Command to start the tool ```python main_app.py```

# Usage

1. Measuring energy consumption due to query execution in four databases: MySQL, PostgreSQL, MongoDB, Couchbase.
2. Comparing energy consumption among these databases.

# Architecture

DBJoules uses psutil package to measure energy consumption. The tool is developed to compare energy consumed by CPU and RAM for query execuation. The internal workflow is described in the below figure.

![DBJoules_Workflow](https://github.com/LellaHemasriSai/GreenDB/assets/91315524/f829386a-619f-4745-b69c-9340498ab7d1)

# Packages Used


1. **mysql-connector-python**: This module facilitates Python programs in accessing and manipulating MySQL databases through API calls.
2. **psycopg2**: Psycopg is the most popular PostgreSQL database adapter for the Python. It offers complete implementation of the Python DB API 2.0 specification10 and ensures thread safety.
3. **pymongo**: This package serves as a native Python driver for MongoDB, providing tools for seamless interaction with MongoDB databases from Python.
4. **couchbase**: This module allows Python applications to access a Couchbase cluster efficiently.
5. **psutil.cpu_percent()**: This function gathers CPU utilization percentage for calculating energy consumed by CPU.
6. **psutil.virtual_memory()**: This function provides the allocated memory for calculating energy consumed by RAM.

# Versions of Database systems and Connection packages

| Database System  | Version | Database Connection Package  | Version|
| ------------- | ------------- | ------------- | ------------- |
|  MySQL | 8.0.34  | mysql-connector-python | 8.0.32  |
| PostgreSQL  | 15.3  | psycopg2  | 2.9.6  |
| MongoDB  | 5.0.12  | pymongo  | 4.3.3  |
| Couchbase  | 7.2.5325  | couchbase  | 4.1.7  |

# Datasets

Following are the datasets used for the experiments (can be found in the Experiments/Datasets folder):
| Dataset  | Number of Data Points | Number of Attributes  | File Size (Bytes) |
| ------------- | ------------- | ------------- | ------------- |
|  <a href="https://www.kaggle.com/datasets/arnavsmayan/netflix-userbase-dataset">Netflix Userbase Dataset</a> | 2500  | 10  | 181211  |
| <a href="https://archive.ics.uci.edu/dataset/352/online+retail">Online Retail</a>  | 541909  | 8  | 46133248  |
| <a href="https://www.kaggle.com/datasets/unitednations/international-energy-statistics">International Energy Statistics</a>  | 1189482  | 7  | 130003960  |

# Small Description of each Database System
1. MySQL, established in 1995 by David Axmark, is the most widely used open-source client-server relational database management system. It originated from TcX, a Swedish company's pursuit of an SQL interface for web application development. MySQL adopts a table-based approach and provides a range of replication and clustering options to facilitate vertical or horizontal scaling as data and user base expand.
2. PostgreSQL, an open-source object-relational database management system, was developed by the University of California, Berkeley Computer Science Department. The project's goal was to create a database system with minimal features to support various data types. PostgreSQL allows the writing of stored procedures and functions in multiple programming languages.
3. MongoDB was established by Dwight Merriman, Eliot Horowitz and Kevin Ryan in 2007. MongoDB is an open-source, cross-platform, document-oriented non-relational database management system that employs JSON-like documents with flexible schemas, unlike traditional SQL database systems that organize data in tables.
4. Couchbase is an open-source distributed document database with a powerful search engine and built-in operational and analytical capabilities. It was initially released in 2010 and is designed to address the modern needs of application developers by providing the strengths of SQL, NoSQL, and NewSQL in a single database system.

# Note

1. The document in MongoDB query should be in JSON format
2. Internet should be connected while running the tool
3. OS version of systems used for experiments- Windows 11 23H2
4. Dbjoules saves the resultant values with up to two decimal places in a CSV file.


