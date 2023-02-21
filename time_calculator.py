def add_time(start, duration, option = ""):
    baseMinutes = getMinutesWithListOptPeriod(split_timePeriod(start)[0], period_toMinute(split_timePeriod(start)[1]))
    toAddMinutes = getMinutesWithListOptPeriod(duration)
    totalMinutes = baseMinutes + toAddMinutes
    toAddDays = getDaysFromMinutes(totalMinutes)
    flavorText = daysMessage(toAddDays)
    flavoredText =""
    if flavorText:
        flavoredText = (" (" + flavorText + ")")

    mainTime = str(getHoursPeriod(totalMinutes/60)[1])  + ":" + formatMinutesToString(int(totalMinutes%60)) +" " + str(getHoursPeriod(totalMinutes/60)[0])
    if option:
        optional = ", " + getUpdatedDay(option, toAddDays)
        return mainTime + optional + flavoredText
    return  mainTime + flavoredText

def getUpdatedDay(dayOption, daysPassed):
    weekDaysList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    indexLocation = weekDaysList.index(dayOption.capitalize())
    daysCount = daysPassed
    while daysCount > 0:
        daysCount -= 1
        indexLocation += 1
        if(indexLocation >6):
            indexLocation = 0
    return weekDaysList[indexLocation]

def formatMinutesToString(minute):
    if minute<10:
        return "0" + str(minute)
    return str(minute)

def daysMessage(days):
    if days == 1:
        return "next day"
    if days > 1:
        return (str(days) + " days later")
    return ""

def getHoursPeriod(hours):
    hour = int(hours)
    if hour%24> 11:
        period = "PM"
    else:
        period = "AM"
    while hour>12:
        hour-=12
    return period, hour

def getHoursAndMinutes(minutes):
    return int(minutes/60), minutes%60

def getDaysFromMinutes(minutes):
    return int(minutes/1440)

def getMinutesWithListOptPeriod(minuteList, optional = 0):
    return transform_hourToMinute(strList_toInt(minuteList), optional)

def transform_hourToMinute(baseTime, period = 0):
    return (baseTime[0] + period)* 60 + baseTime[1]

def strList_toInt(string):
    return [int(x) for x in split_hourMinute(string)]

def period_toMinute(period):
    if period == "AM":
        return 0
    return 12

def split_hourMinute(time):
    return time.split(":")

def split_timePeriod(timeString):
    return timeString.split(" ")

print(add_time("8:16 PM", "466:02", "tuesday"))