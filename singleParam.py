import pickle

def test(paramsList):
    with open('averages.pkl', 'rb') as file:
        averages = pickle.load(file)
    start=0
    end=239
    total=0
    momentumWorks=0
    averagePercent=0
    for k in range(start, end):
        for j in range(len(stocks)):
            if averages[k][paramsList[0],stocks[j]] > averages[k][paramsList[1],stocks[j]]:
                total+=1
                averagePercent+=((averages[k][paramsList[2],stocks[j]])/(averages[k][paramsList[3],stocks[j]]))
                if averages[k][paramsList[2],stocks[j]] > averages[k][paramsList[3],stocks[j]]:
                    momentumWorks+=1
    try:
        averagePercent=averagePercent/total
    except:
        averagePercent=0
    return(total, momentumWorks, averagePercent)
