import datetime
import pytz
import numpy as np

def datetimeFromUnix(unix_timestamp):
    my_time = datetime.datetime.fromtimestamp(unix_timestamp/1000)

    eastern_tz = pytz.timezone('US/Eastern')
    local_time = datetime.datetime.fromtimestamp(unix_timestamp/1000, eastern_tz)
    return(my_time, local_time)

def dayOfWeekFromUnix(unix_timestamp):
    day_of_week = datetime.strftime(datetime.fromtimestamp(unix_timestamp/1000), '%A')
    return day_of_week

def printWhenExecuting(fn):
    def fn2(self):
        print("   doing", fn.__name__)
        fn(self)
        print("   done w/", fn.__name__)

    return fn2

def sqrt(x):
    return x**0.5

def sharpe_ratio_annual(returns, risk_free_rate=0.02):
    return np.mean(returns - risk_free_rate) / np.std(returns)

def sharpe_ratio_daily(returns, risk_free_rate=1.02**(1/252)-1):
    return np.mean(returns - risk_free_rate) / np.std(returns)