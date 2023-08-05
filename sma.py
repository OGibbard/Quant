import polars as pl

#Function for sma
def sma(length, date, stock, dataframe):
    start=0-(length+date)-1
    end=0-date-1

    total = 0
    for k in range(start,end):
        total+=int(dataframe[k,stock])
    average = total/length

    return (average)

def downloadSma(backDate):
    df = pl.read_csv("../Data/sp500/dailyOpenHist2017.csv", infer_schema_length=None)
    stockComponents=df.columns
    allsma={}
    for k in range(len(stockComponents)):
        tempStock=stockComponents[k]
        #Add sma for different lengths of time
        stockSMA=[]
        stockSMA.append(sma(200, backDate, stockComponents[k], df))
        stockSMA.append(sma(100, backDate, stockComponents[k], df))
        stockSMA.append(sma(50, backDate, stockComponents[k], df))
        stockSMA.append(sma(20, backDate, stockComponents[k], df))
        stockSMA.append(sma(10, backDate, stockComponents[k], df))

        #Add current price
        stockSMA.append(df[(0-backDate-1),stockComponents[k]])
        #Add prices 1-10 days after current date
        if backDate>=5:
            stockSMA.append(df[(0-backDate),stockComponents[k]])
            stockSMA.append(df[(1-backDate),stockComponents[k]])
            stockSMA.append(df[(2-backDate),stockComponents[k]])
            stockSMA.append(df[(3-backDate),stockComponents[k]])
            stockSMA.append(df[(4-backDate),stockComponents[k]])
        if backDate>=10:
            stockSMA.append(df[(5-backDate),stockComponents[k]])
            stockSMA.append(df[(6-backDate),stockComponents[k]])
            stockSMA.append(df[(7-backDate),stockComponents[k]])
            stockSMA.append(df[(8-backDate),stockComponents[k]])
            stockSMA.append(df[(9-backDate),stockComponents[k]])
            
        allsma[tempStock] = stockSMA

    allsmaDF = pl.DataFrame(allsma)
    #Write dataframe to csv
    allsmaDF.write_csv(("../Data/sp500/sma/2017/Open/SimpleMovingAverages"+str(backDate)+".csv"), separator=",")