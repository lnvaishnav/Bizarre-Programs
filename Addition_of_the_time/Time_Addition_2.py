import math
totalNo = int(input("How many total sequences? "))
input("NOTE: Please enter the time in the defined format only. \nFORMAT:- HHMMSS (If 2 hr 5 minutes 9 secs then it should be like 020509 \
    \nIf you'll enter like 52311 then 52 will be count as hr, 31 be minute and 1 will be second, be carefull! \nPress ENTER to continue...")

time = []
hour = []
minute = []
second = []
left = totalNo
for i in range(totalNo):
    left -= 1
    x = input("Enter the time: ")
    time.append(x)
    if left !=0:
        print(f"\t\tLeft number: {left}")

print("Full dictionary of the time: ", end="")
print({i: time[i] for i in range(0, len(time))})

for i in time:
    x = [int(i[j:j+2]) for j in range(0, len(i),2)]
    hour.append(x[0])
    minute.append(x[1])
    second.append(x[2])

hourX = minuteX = secondX = 0
for i in hour:
    hourX += i

for i in minute:
    minuteX += i

for i in second:
    secondX += i

print(f"Total..\nHours: {hourX}, Minutes: {minuteX}, Seconds: {secondX}")

if secondX >= 60: 
    minuteX_E = math.floor(secondX/60)
    secondX_E = secondX%60
else:
    minuteX_E = 0
    secondX_E = secondX

if minuteX >= 60:
    hourX_E = math.floor(minuteX/60)
    minuteX_F = minuteX%60
else:
    hourX_E = 0
    minuteX_F = minuteX

minute_T = minuteX_E + minuteX_F
hour_T = hourX + hourX_E

print(f"Total time: {hour_T}:{minute_T}:{secondX_E}")