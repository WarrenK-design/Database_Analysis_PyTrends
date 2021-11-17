# Database_Analysis_PyTrends
This repo holds the code to generate graphs using the PyTrends and the data from Google Trends API. 
The graphs generated have a particular focus on Columnar databases and HBase. 


Three example scripts are created already in this directory which generate graphs to the ```figuers``` directory. 

```
topColumnarTechnologys.py - Compares the top columnar technologys ("HBase", "Cassandra", "Azure Table Storage","Google Bigtable")
topDBTechnologyTypes.py - Compares the top database technolgys ("columnar database", "document database", "relational database","key value database")
topDatabases.py - Compares the top databases ("HBase", "Oracle", "MySQL","Microsoft SQL Server", "PostgresSQL")
```

The files can be copied and the basic templates reused changing values at the top of the scripts for the variables listed below. All the template scripts used the same functions defined in the ```dbAnalysis``` class.
```
topDBSearchList - This is a list of keywords to compare in the Google trends API 
outputDir - A directory to saved the generated figuers
```

***NOTE*** When comparing values you may also need to change the category in which they are compared using a [category number](https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories).
For example ```Cassandra``` is a database but most Google searches are related to names of people or there is also a Greek god named Cassandra.
In relations to databases it is better to compare this under category number ```343``` which relates to Enterprise Technology and in particular Data Management.
