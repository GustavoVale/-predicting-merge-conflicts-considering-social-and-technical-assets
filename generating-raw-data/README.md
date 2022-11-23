
# Generating Raw Data for Developer Role Analysis

This folder has all necessary scripts to collect data from the database and store them in CSV files. In the file *4CsNet-DB.pdf* you see an overview of the tables in the used database.

*1-retrieving-data-from-database.R* has the steps to retrieve and store data using some dao files as source.
	*1-1-database-connection.R* has functions to open and close database connections.
	
Note that it requires a cnf.file with database credentials, such as

```[serverDB]
unix.socket=/var/run/mysqld/mysqld.sock
user=<user>
password=<password>
dbname=<database name>
host=<>host
port=3306

[client]
ssl-cipher=<ss-cipher>
ssl-ca=<path to the ca certificate>
```
*1-2-dao-devs.R* functions related to developers table
*1-3-dao-merge-scenario.R* functions related to merge scenarios table
*1-4-dao-project-metrics* functions related to projects table

In the CSVs sub-folder are CSV files generated and used in our analyses.
