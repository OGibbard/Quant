import polars as pl
import pickle

def doubleTest(paramsList, averages, stocks):

    parameters=["200 sma", "100 sma", "50 sma", "20 sma", "10 sma", "current price", "price 1 days after", "price 2 days after", "price 3 days after", "price 4 days after", "price 5 days after", "price 6 days after", "price 7 days after", "price 8 days after", "price 9 days after", "price 10 days after"]

    averages=[]
    for k in range(10,1205,5):
        averages.append(pl.read_csv("../Data/sp500/sma/Open/SimpleMovingAverages"+str(k)+".csv", infer_schema_length=None))
    stocks=list(averages[0].columns)

    start=0
    end=239

    total=0
    momentumWorks1=0
    momentumWorks2=0
    averagePercent=0

    for k in range(start, end):
        for j in range(len(stocks)):
            if averages[k][paramsList[0],stocks[j]] > averages[k][paramsList[1],stocks[j]]:
                total+=1
                if averages[k][paramsList[2],stocks[j]] > averages[k][paramsList[3],stocks[j]]:
                    momentumWorks1+=1
                    averagePercent+=((averages[k][paramsList[4],stocks[j]])/(averages[k][paramsList[5],stocks[j]]))
                    if averages[k][paramsList[4],stocks[j]] > averages[k][paramsList[5],stocks[j]]:
                        momentumWorks2+=1

    try:
        averagePercent=averagePercent/momentumWorks1
    except:
        averagePercent=1

    days = abs(paramsList[5] - paramsList[4])
    perDay = averagePercent ** (1/days)

    if perDay>1.005:

        tempParams=''
        for i in paramsList:
            tempParams+=str(i)

        tempRead=[]
        tempRead.append(parameters[paramsList[0]] + " is higher than " + parameters[paramsList[1]] + " " + str(total) + " times.")
        tempRead.append("Of these times, the " + parameters[paramsList[2]] + " is higher than the " + parameters[paramsList[3]] + " " + str(momentumWorks1) + " times.")
        tempRead.append("Of these times, the " + parameters[paramsList[4]] + " is higher than the " + parameters[paramsList[5]] + " " + str(momentumWorks2) + " times.")
        tempRead.append("Overall this is " + str(momentumWorks2/momentumWorks1) + " of the time.")
        tempRead.append('The average increase is '+(str(averagePercent))+".")
        tempRead.append('This is '+str(perDay)+'  increase per day.')
        with open('../Data/sp500/bestStrategies/Double/Open/'+tempParams+'.txt','w') as file:
            for k in range(len(tempRead)):
                file.write(tempRead[k]+'\n')
    return(total, momentumWorks1, momentumWorks2, averagePercent)


def doubleListTest(paramsList):

    parameters=["200 sma", "100 sma", "50 sma", "20 sma", "10 sma", "current price", "price 1 days after", "price 2 days after", "price 3 days after", "price 4 days after", "price 5 days after", "price 6 days after", "price 7 days after", "price 8 days after", "price 9 days after", "price 10 days after"]

    averages=[]
    for k in range(10,1205,5):
        averages.append(pl.read_csv("../Data/sp500/sma/Open/SimpleMovingAverages"+str(k)+".csv", infer_schema_length=None))
    stocks=list(averages[0].columns)

    start=0
    end=239

    total=0
    momentumWorks1=0
    momentumWorks2=0
    averagePercent=0

    for k in range(start, end):
        for j in range(len(stocks)):
            if averages[k][paramsList[0],stocks[j]] > averages[k][paramsList[1],stocks[j]]:
                total+=1
                if averages[k][paramsList[2],stocks[j]] > averages[k][paramsList[3],stocks[j]]:
                    momentumWorks1+=1
                    averagePercent+=((averages[k][paramsList[4],stocks[j]])/(averages[k][paramsList[5],stocks[j]]))
                    if averages[k][paramsList[4],stocks[j]] > averages[k][paramsList[5],stocks[j]]:
                        momentumWorks2+=1

    try:
        averagePercent=averagePercent/momentumWorks1
    except:
        averagePercent=1

    days = abs(paramsList[5] - paramsList[4])
    perDay = averagePercent ** (1/days)

    if perDay>1.005:

        tempParams=''
        for i in paramsList:
            tempParams+=str(i)

        tempRead=[]
        tempRead.append(parameters[paramsList[0]] + " is higher than " + parameters[paramsList[1]] + " " + str(total) + " times.")
        tempRead.append("Of these times, the " + parameters[paramsList[2]] + " is higher than the " + parameters[paramsList[3]] + " " + str(momentumWorks1) + " times.")
        tempRead.append("Of these times, the " + parameters[paramsList[4]] + " is higher than the " + parameters[paramsList[5]] + " " + str(momentumWorks2) + " times.")
        tempRead.append("Overall this is " + str(momentumWorks2/momentumWorks1) + " of the time.")
        tempRead.append('The average increase is '+(str(averagePercent))+".")
        tempRead.append('This is '+str(perDay)+'  increase per day.')
        with open('../Data/sp500/bestStrategies/Double/Open/'+tempParams+'.txt','w') as file:
            for k in range(len(tempRead)):
                file.write(tempRead[k]+'\n')
    return(total, momentumWorks1, momentumWorks2, averagePercent)

def doublePickleTest(paramsList):

    parameters=["200 sma", "100 sma", "50 sma", "20 sma", "10 sma", "current price", "price 1 days after", "price 2 days after", "price 3 days after", "price 4 days after", "price 5 days after", "price 6 days after", "price 7 days after", "price 8 days after", "price 9 days after", "price 10 days after"]

    with open('../Data/sp500/polarsOpenAverages.pkl', 'rb') as file:
        averages = pickle.load(file)
    with open('../Data/sp500/stockList.pkl', 'rb') as file:
        stocks = pickle.load(file)

    start=0
    end=239

    total=0
    momentumWorks1=0
    momentumWorks2=0
    averagePercent=0

    for k in range(start, end):
        for j in range(len(stocks)):
            if averages[k][paramsList[0],stocks[j]] > averages[k][paramsList[1],stocks[j]]:
                total+=1
                if averages[k][paramsList[2],stocks[j]] > averages[k][paramsList[3],stocks[j]]:
                    momentumWorks1+=1
                    averagePercent+=((averages[k][paramsList[4],stocks[j]])/(averages[k][paramsList[5],stocks[j]]))
                    if averages[k][paramsList[4],stocks[j]] > averages[k][paramsList[5],stocks[j]]:
                        momentumWorks2+=1

    try:
        averagePercent=averagePercent/momentumWorks1
    except:
        averagePercent=1
    
    days = abs(paramsList[5] - paramsList[4])
    perDay = averagePercent ** (1/days)

    if perDay>1.005:

        tempParams=''
        for i in paramsList:
            tempParams+=str(i)

        tempRead=[]
        tempRead.append(parameters[paramsList[0]] + " is higher than " + parameters[paramsList[1]] + " " + str(total) + " times.")
        tempRead.append("Of these times, the " + parameters[paramsList[2]] + " is higher than the " + parameters[paramsList[3]] + " " + str(momentumWorks1) + " times.")
        tempRead.append("Of these times, the " + parameters[paramsList[4]] + " is higher than the " + parameters[paramsList[5]] + " " + str(momentumWorks2) + " times.")
        tempRead.append("Overall this is " + str(momentumWorks2/momentumWorks1) + " of the time.")
        tempRead.append('The average increase is '+(str(averagePercent))+".")
        tempRead.append('This is '+str(perDay)+'  increase per day.')
        with open('../Data/sp500/bestStrategies/Double/Open/'+tempParams+'.txt','w') as file:
            for k in range(len(tempRead)):
                file.write(tempRead[k]+'\n')
    return(total, momentumWorks1, momentumWorks2, averagePercent)