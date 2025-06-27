import time
from time import strftime
timestamp = strftime("%Y-%m-%d %H:%M:%S")
print("Current timestamp:", timestamp)
timestamp1 = time.strftime("%H")
print("Current Hour:", timestamp1)
timestamp2 = time.strftime("%M")
print("Current Minute:", timestamp2)
timestamp3 = time.strftime("%S")
print("Current Second:", timestamp3)

def wishme(timestamp1):
    if int(timestamp1) < 12:
        print("Good Morning Sir!!")


    elif int(timestamp1) == 12:
        print("Good Afternoon Sir!!")


    elif int(timestamp1) > 12:
        print("Good Afternoon Sir!!")


    elif int(timestamp1) >= 16:
        print("Good Evening Sir!!")

    elif int(timestamp1) >= 20:
        print("Good Night Sir!!")


    else:
        print("Give Valid Input Sir!!") 

wishme(timestamp1)