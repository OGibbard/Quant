import pickle

def test(paramsList):
    with open('../Data/sp500/averages.pkl', 'rb') as file:
        averages = pickle.load(file)
    with open('../Data/sp500/stockList.pkl', 'rb') as file:
        stocks = pickle.load(file)

    start=0
    end=239
    total=0
    momentumWorks=0
    averagePercent=0
    for k in range(start, end):
        for j in range(len(stocks)):
            if averages[k].loc(0)[paramsList[0]][j] > averages[k].loc(0)[paramsList[1]][j]:
                total+=1
                averagePercent+=((averages[k].loc(0)[paramsList[2]][j])/(averages[k].loc(0)[paramsList[3]][j]))
                if averages[k].loc(0)[paramsList[2]][j] > averages[k].loc(0)[paramsList[3]][j]:
                    momentumWorks+=1
    try:
        averagePercent=averagePercent/total
    except:
        averagePercent=1
    return(total, momentumWorks, averagePercent)
