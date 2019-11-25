## Logs Analysis
For this project, I had to create a reporting tool for a fictional news website. This tool is written in Python and uses the psycopg2 module to connect to the mock 'news' database created in PostgreSQL and provided by Udacity.  So based on the database tables, I had to answer the following questions:

 1. What are the most popular three articles of all time?
 2. Who are the most popular article authors of all time?
 3. On which days did more than 1% of requests lead to errors?

## How do I run this?
1. I used the VM to make sure that the environment I was building the project was similar to the one instructors had used. It is recommended to use 'vagrant' to have the Linux Development environment and you can download [vagrant](https://www.vagrantup.com/) and [Virtual Machine](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) in those links.

2. Download the VM configuration from the [downloads folder](https://github.com/metalwihen/udacity-full-stack-nanodegree-projects/blob/master/Project3/downloads) or clone from this [github repo.](https://github.com/udacity/fullstack-nanodegree-vm) Note the path where you downloaded it as it will be used in other steps.

The configuration file specifies the arrangement of resources (processors, memory, disks, network adapters, etc) assigned to a virtual machine.

After downloading those files, install the Virtual Box first. Then go the directory 'vagrant' was downloaded and run:
`vagrant up`
to install the environment. Note that it will take a quuite amount of time and you have to run this command everytime you reboot your system.

Then run:
`vagrant ssh`
from the same directory to log in to the Virtual Environment.

3. Download the mock database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and unzip it to the directory inside Virtual Machine, folder name is 'vagrant'. 

4. Load the database using `psql -d news -f newsdate.sql`

5. Connect to the database using  `psql -d news`

6. Create the views I have provided below. Then exit the database with `ctrl+d` or `psql`

7. Now execute the python file `logdb.py`


## Views for the Questions

# Question 2 
``` sql
CREATE VIEW article_authors AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;

CREATE VIEW article.views AS 
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/',article.slug)
GROUP BY article.title
ORDER BY views desc;
```

# Question 3
```sql
CREATE VIEW requests AS
SELECT to_char(time,'DD-MON-YYYY') as date, COUNT(status) as requestCount
FROM log
GROUP by date;

CREATE VIEW ErrorResponse AS 
SELECT to_char(time,'DD-MON-YYYY') as date, COUNT(status) as ErrorResponseCount
FROM log
where status = '404 NOT FOUND'
GROUP BY date;
```

## References

- [Creating time string from time stamp](http://www.postgresqltutorial.com/postgresql-to_char/)
- [Functions PostgreSQL](https://www.postgresql.org/docs/12/functions.html)
- [Aggregate Functions](https://www.postgresql.org/docs/9.5/static/functions-aggregate.html)
- [Subqueries](https://www.postgresql.org/docs/9.4/static/functions-subquery.html)
- [PSQL CLI Commands](https://www.postgresql.org/docs/9.2/static/app-psql.html)
