from datetime import datetime
#for finding the current time(0-23)
hour = datetime.now().hour
if hour < 12:
    print("Good Morning...")
elif 12 <= hour < 17:
    print("Good AfterNoon..")
elif 17 <= hour < 21 :
    print("Good Evening..")
else :
    print("Good Night...")
