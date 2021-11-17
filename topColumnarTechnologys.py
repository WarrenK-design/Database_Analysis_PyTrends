from dbAnalysis import dbAnalysis

if __name__ == '__main__':
    # Get your search list
    topDBSearchList = ["HBase", "Cassandra", "Azure Table Storage",
                       "Google Bigtable"]
    
    #topDBSearchList = ["columnar database"]
    outputDir = "./figuers/topColumnarTechnologys/"

    # Initiliase the analysis object
    db = dbAnalysis(topDBSearchList)
    # Build the payload - cat 343 = Enterprise Technology -> Data Management 343
    db.build_payload(cat=343)

    # Get the interest over time of the top database
    db.getInterestOverTime()
    interestOverTimeFile = outputDir + "InterestOverTime.png"
    db.plotLine(db.interest_over_time,interestOverTimeFile,target_value="HBase",xoffSet=-1500,yoffset=40,title="HBase Interest over time compared to other Columnar Databases")

    # Get the interest by hour 
    #db.getHourlyInterest()
    #interestByHourFile = outputDir + "InterestByHour.png"
    #db.plotLine(db.hourly_Interest,interestByHourFile,target_value="columnar database",xoffSet=1,yoffset=10,title="Top Databases and HBase hourly interest")
    #
    ## Get the interest by region 
    db.getInterestByRegion("COUNTRY",sortValues=topDBSearchList)
    interestByRegionFile = outputDir + "InterestByRegion.png"
    db.plotStackedBar(db.interestByRegion,interestByRegionFile,title="Interest by region sorted by HBase")

    ## Plot the Related Queries 
    db.getRelatedQueries()
    relatedQueriesFile = outputDir + "ReleatedQueries.png"
    #db.plotStackedBar(db.relatedQueries["HBase"]["top"],relatedQueriesFile,title="Queries Related to HBase")
    db.plotRelatedQueries("HBase",relatedQueriesFile,ylabel="Search Term",xlabel="Score",title="Top Queries Related to HBase")
