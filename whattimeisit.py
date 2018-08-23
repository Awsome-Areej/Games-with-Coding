import datetime
def whattimeisit():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    if hour >= 12 :
        print ("Good evening it is "  +  str(hour-12) + ":"  +  str(minute) + " Pm")
    else :
        print ("Good Morning it is "  +  str(hour)  +  ":"   +  str(minute) + " Am")
