# Logs Analysis Project _first project

## DESCRIPTION
in this project, will be create a database that prints out reports,based on the data in the given database. This database is used a Python program using the `psycopg2` module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

### RUNNING THE PROGRAM
- To get started, I recommend the user use a virtual machine to ensure they are using the same environment that this project was developed on, running on your computer. You can download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage your virtual machine.
Use `vagrant up` to bring the virtual machine online and `vagrant ssh` to login.

- Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder. 

- Load the database using `psql -d news -f newsdata.sql`. 

- Connect to the database using `psql -d news`.

-  Create the Views given below. Then exit `psql`.

-  Now execute the Python file - `python logs_analysis.py`.


##### Views for Question 2
```sql
CREATE VIEW article_authors AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;
```










