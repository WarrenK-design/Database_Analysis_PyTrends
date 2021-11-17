## Imports ##
# pandas     - Dataframe library
# pytrends   - API for google trends
# matplotlib - Plotting library for python
import pandas as pd
from pytrends.request import TrendReq
import matplotlib
from matplotlib import pyplot as plt


class dbAnalysis:
    def __init__(self, searchList):
        self.pytrends = TrendReq()
        self.searchList = searchList
        #self.interest_over_time_df = null
        #self.interest_by_region_df = null
        # self.related_queries_dict
        # self.trending_searches_df
        # self.today_searches_df
        # self.top_charts_df

    def build_payload(self,geo=None,cat=None):
        self.pytrends.build_payload(kw_list=self.searchList,geo=geo,cat=cat,timeframe='2011-11-09 2021-11-09')

    # Calculate interest over time
    def getInterestOverTime(self):
        self.interest_over_time = pd.DataFrame(self.pytrends.interest_over_time()).drop(columns='isPartial')

    # Calculate the historical hourly interest 
    def getHourlyInterest(self,year_start=2021, month_start=10, day_start=7, hour_start=0, year_end=2021, month_end=11, day_end=1, hour_end=0):
        self.hourly_Interest = pd.DataFrame(self.pytrends.get_historical_interest(self.searchList, year_start=year_start, month_start=month_start, day_start=day_start, hour_start=hour_start, year_end=year_end, month_end=month_end, day_end=day_end, hour_end=hour_end, cat=0, geo='', gprop='', sleep=0))

    # Get the interest by region, sortValues is a list 
    def getInterestByRegion(self,resolution="COUNTRY",number=20,sortValues=None):
        self.interestByRegion = pd.DataFrame(self.pytrends.interest_by_region(resolution=resolution, inc_low_vol=True, inc_geo_code=False))
        if sortValues:
            self.interestByRegion = self.interestByRegion.sort_values(sortValues, ascending=False).head(20)
    
    # Get the mean of every column in a dataframe 
    def getMeandf(self,data):
        result = {}
        for column in data:
            result[column] = data[column].mean()
        return result

    # Get the related queries 
    def getRelatedQueries(self):
        self.relatedQueries = self.pytrends.related_queries()

    # Get the related topics 
    def getRelatedTopics(self):
        self.relatedTopics = self.pytrends.related_topics()
        print(self.relatedTopics)

    # Plots line graph -> Mainly used for interest over time
    def plotLine(self,data,outputFile,target_value=None,xoffSet=0,yoffset=0,title="Interest over time",ylabel="Interest",xlabel="Time"):
        ax = plt.gca()
        data.plot(kind='line',title=title,ax=ax)
#        print(data["columnar database"].mean())
        averages = self.getMeandf(data)
        if target_value:
            xmax = (data[target_value].idxmax())
            ymax = data[target_value].max()
            time = xmax.round(freq='D')
            ax.annotate(f'{target_value} max value of\n {ymax} on {time.day}-{time.month}-{time.year}', xy=(xmax, ymax), xytext=(xmax+pd.Timedelta(xoffSet,unit='D'), ymax+yoffset),
            arrowprops=dict(facecolor='black'))
        #first_legend = plt.legend(handles=[data],loc='lower right')
        #ax.legend(["1","2","3"])
        legendText = []
        for key, value in averages.items():
            text = f'{key}, AVG={round(value,2)}'
            legendText.append(text)
        ax.legend(legendText)
        #plt.gca().add_artist(first_legend)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(outputFile)
        plt.close()

    # Plot the barchart -> Used for interest by country  
    def plotStackedBar(self,data,outputFile,title="XXXXXXX",ylabel="Interest",xlabel="Time"):
        ax = plt.gca()
        data.plot(kind ='bar', stacked=True, title=title,ax=ax)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.gcf().subplots_adjust(bottom=0.3)
        ax.tick_params(axis='x', which='major', labelsize=7)
        ax.tick_params(axis='x', which='minor', labelsize=1)
        plt.savefig(outputFile)
        plt.close()

    # Plots the related queries in a bar chart 
    def plotRelatedQueries(self,targetValue,outputFile,title="XXXXXXX",xlabel="Querys",ylabel="Change me"):
        ax = plt.gca()
        data = self.relatedQueries[targetValue]["top"]
        data.plot(kind='barh',title=title,xlabel=xlabel,x="query",y="value",ylabel=ylabel,ax=ax)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend_ = None
        plt.tight_layout()
        plt.savefig(outputFile)


    

    # Plot bar chart of data 
    #def plotBarChart(self,data,xlabel,ylabel):





