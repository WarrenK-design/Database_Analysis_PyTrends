from dbAnalysis import dbAnalysis

if __name__ == '__main__':
    # Get your search list
    topDBSearchList = ["columnar database", "document database", "relational database",
                       "key value database"]
    #topDBSearchList = ["columnar database"]
    outputDir = "./figuers/topDBTechnologyTypes/"

    # Initiliase the analysis object
    db = dbAnalysis(topDBSearchList)
    # Build the payload 
    db.build_payload(cat=343)

    # Get the interest over time of the top database
    db.getInterestOverTime()
    interestOverTimeFile = outputDir + "InterestOverTime.png"
    db.plotLine(db.interest_over_time,interestOverTimeFile,target_value="columnar database",xoffSet=-300,yoffset=15,title="Columnar Database Interest over time compared to other Database types")

    # Get the interest by hour 
    #db.getHourlyInterest()
    #interestByHourFile = outputDir + "InterestByHour.png"
    #db.plotLine(db.hourly_Interest,interestByHourFile,target_value="columnar database",xoffSet=1,yoffset=10,title="Top Databases and HBase hourly interest")
    #
    ## Get the interest by region 
    db.getInterestByRegion("COUNTRY",sortValues=["columnar database","key value database","document database","relational database"])
    interestByRegionFile = outputDir + "InterestByRegion.png"
    db.plotStackedBar(db.interestByRegion,interestByRegionFile,title="Interest by region sorted by Columnar Database")