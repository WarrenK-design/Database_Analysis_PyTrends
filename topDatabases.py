from dbAnalysis import dbAnalysis

if __name__ == '__main__':
    # Get your search list
    topDBSearchList = ["HBase", "Oracle", "MySQL",
                       "Microsoft SQL Server", "PostgresSQL"]
    outputDir = "./figuers/topDBComparisonWithHBase/"

    # Initiliase the analysis object
    db = dbAnalysis(topDBSearchList)
    # Build the payload 
    db.build_payload()

    # Get the interest over time of the top database
    db.getInterestOverTime()
    interestOverTimeFile = outputDir + "InterestOverTime.png"
    db.plotLine(db.interest_over_time,interestOverTimeFile,target_value="HBase",xoffSet=365,yoffset=15,title="Top Databases and HBase interest over time")

    # Get the interest by hour 
    db.getHourlyInterest()
    interestByHourFile = outputDir + "InterestByHour.png"
    db.plotLine(db.hourly_Interest,interestByHourFile,target_value="HBase",xoffSet=1,yoffset=10,title="Top Databases and HBase hourly interest")
    
    # Get the interest by region 
    db.getInterestByRegion("COUNTRY",sortValues=topDBSearchList)
    interestByRegionFile = outputDir + "InterestByRegion.png"
    db.plotStackedBar(db.interestByRegion,interestByRegionFile)
    
    ## Get the related queries 
    db.getRelatedQueries()
    relatedQueriesFile = outputDir + "RelatedQueries.png"
    print(db.relatedQueries)
    db.plotRelatedQueries(db.relatedQueries,"HBase",relatedQueriesFile,ylabel="Interest",title="Querys related to HBase")