def test(paramsList, averages, stocks):

    parameters=["200 sma", "100 sma", "50 sma", "20 sma", "10 sma", "current price", "price 1 days after", "price 2 days after", "price 3 days after", "price 4 days after", "price 5 days after", "price 6 days after", "price 7 days after", "price 8 days after", "price 9 days after", "price 10 days after"]

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
        averagePercent=1

    if averagePercent>1.01:
        print(parameters[paramsList[0]] + " is higher than " + parameters[paramsList[1]] + " " + str(total) + " times.")
        print("Of these times, the " + parameters[paramsList[2]] + " is higher than the " + parameters[paramsList[3]] + " " + str(momentumWorks) + " times.")
        print("Overall this is " + str(momentumWorks/total) + " of the time.")
        print('The average increase is '+(str(averagePercent))+".")
    return(total, momentumWorks, averagePercent)