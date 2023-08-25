import polars as pl
import pickle

def doubleListTest(paramsList):

    parameters=["200 sma", "100 sma", "50 sma", "20 sma", "10 sma", "current price", "price 1 days after", "price 2 days after", "price 3 days after", "price 4 days after", "price 5 days after", "price 6 days after", "price 7 days after", "price 8 days after", "price 9 days after", "price 10 days after"]

    openAverages=[]
    closeAverages=[]

    for k in range(10,1205,5):
        openAverages.append(pl.read_csv("../Data/sp500/sma/2017/Open/SimpleMovingAverages"+str(k)+".csv", infer_schema_length=None))
    for k in range(10,1205,5):
        closeAverages.append(pl.read_csv("../Data/sp500/sma/2017/Close/SimpleMovingAverages"+str(k)+".csv", infer_schema_length=None))
    stocks=list(openAverages[0].columns)

    start=0
    end=239

    total=0
    momentumWorks1=0
    momentumWorks2=0
    averagePercent=0

    for k in range(start, end):
        for j in range(len(stocks)):
            if openAverages[k][paramsList[0],stocks[j]] > openAverages[k][paramsList[1],stocks[j]]:
                total+=1
                if openAverages[k][paramsList[2],stocks[j]] > openAverages[k][paramsList[3],stocks[j]]:
                    momentumWorks1+=1
                    averagePercent+=((closeAverages[k][paramsList[4],stocks[j]])/(openAverages[k][paramsList[5],stocks[j]]))
                    if closeAverages[k][paramsList[4],stocks[j]] > openAverages[k][paramsList[5],stocks[j]]:
                        momentumWorks2+=1

    try:
        averagePercent=averagePercent/momentumWorks1
    except:
        averagePercent=1

    days = abs(paramsList[5] - paramsList[4])+1
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
        with open('../Data/sp500/bestStrategies/Double/'+tempParams+'.txt','w') as file:
            for k in range(len(tempRead)):
                file.write(tempRead[k]+'\n')
    return(total, momentumWorks1, momentumWorks2, averagePercent, perDay)




def doublePickleTest(paramsList):

    parameters=["200 sma", "100 sma", "50 sma", "20 sma", "10 sma", "current price", "price 1 days after", "price 2 days after", "price 3 days after", "price 4 days after", "price 5 days after", "price 6 days after", "price 7 days after", "price 8 days after", "price 9 days after", "price 10 days after"]

    with open('../Data/sp500/pandasOpenAverages.pkl', 'rb') as file:
        openAverages = pickle.load(file)
    with open('../Data/sp500/pandasCloseAverages.pkl', 'rb') as file:
        closeAverages = pickle.load(file)

    start=0
    end=239

    total=0
    momentumWorks1=0
    momentumWorks2=0
    averagePercent=0

    for k in range(start, end):
        openCurrent=openAverages[k]
        closeCurrent=closeAverages[k]
        total += sum((openCurrent.iloc[paramsList[0]] > openCurrent.iloc[paramsList[1]]).astype(int))
        momentumWorks1 += sum(((openCurrent.iloc[paramsList[2]] > openCurrent.iloc[paramsList[3]]) & (openCurrent.iloc[paramsList[0]] > openCurrent.iloc[paramsList[1]])).astype(int))
        momentumWorks2 += sum(((closeCurrent.iloc[paramsList[4]] > openCurrent.iloc[paramsList[5]]) & (openCurrent.iloc[paramsList[2]] > openCurrent.iloc[paramsList[3]]) & (openCurrent.iloc[paramsList[0]] > openCurrent.iloc[paramsList[1]])).astype(int))
        averagePercent += sum((closeCurrent.iloc[paramsList[4]])/(openCurrent.iloc[paramsList[5]])*((openCurrent.iloc[paramsList[0]] > openCurrent.iloc[paramsList[1]]).astype(int))*((openCurrent.iloc[paramsList[2]] > openCurrent.iloc[paramsList[3]]).astype(int)))

    try:
        averagePercent=averagePercent/momentumWorks1
    except:
        averagePercent=1
    
    days = abs(paramsList[5] - paramsList[4])+1
    perDay = averagePercent ** (1/days)

    if perDay>1.0035:

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
        with open('../Data/sp500/bestStrategies/Double/'+tempParams+'.txt','w') as file:
            for k in range(len(tempRead)):
                file.write(tempRead[k]+'\n')
    return(total, momentumWorks1, momentumWorks2, averagePercent, perDay)
