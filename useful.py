import datetime
import pytz

def datetimeFromUnix(unix_timestamp):
    my_time = datetime.datetime.fromtimestamp(unix_timestamp/1000)

    eastern_tz = pytz.timezone('US/Eastern')
    local_time = datetime.datetime.fromtimestamp(unix_timestamp/1000, eastern_tz)
    return(my_time, local_time)

def dayOfWeekFromUnix(unix_timestamp):
    day_of_week = datetime.strftime(datetime.fromtimestamp(unix_timestamp/1000), '%A')
    return day_of_week
