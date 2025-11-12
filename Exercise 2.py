import time
print("Indian Standard Time")
timesnow = time.strftime('%I:%M:%S%p') 
print(timesnow)

# hour,minute,second = int(input("enter hour")),int(input("enter minute")),int(input("enter second"))
# print(hour,":",minute,":",second)
hour = int(time.strftime('%H'))
print(hour)
minute = time.strftime('%M')
print(minute)
second = time.strftime('%S')
print(second)
ampm = time.strftime('%p')
print(ampm)


# if timesnow >= "12:00:00AM" and timesnow <= "11:59:59AM":
#     print("Good Morning, Sir")
# if timesnow >= "12:00:00PM" and timesnow <= "03:59:59PM":
#     print("Good Afternoon, Sir")
# if timesnow >= "04:00:00PM" and timesnow <= "07:59:59PM":
#     print("Good Evening, Sir")
# if timesnow >= "08:00:00PM" and timesnow <= "11:59:59PM":
#     print("Good Night, Sir")

if(hour >= 0 and hour < 12 and ampm == "AM"):
    print("Good Morning, Boss")
elif(hour >= 12 and hour < 17 and ampm == "PM"):
    print("Good Afternoon, Boss")
elif(hour >= 17 and hour < 21 and ampm == "PM"):
    print("Good Evening, Boss")
elif(hour >= 21 and hour <24 and ampm == "PM"):
    print("Good Night, Boss")