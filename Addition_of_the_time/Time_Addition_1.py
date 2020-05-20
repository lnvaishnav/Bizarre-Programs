import math

totalNo = int(input("How many total sequence? "))

hrs = []
mins = []
secs = []
left = totalNo

for i in range(totalNo):    
    left -= 1
    x = int(input("Enter total hours: "))
    hrs.append(x)
    y = int(input("Enter total minutes: "))
    mins.append(y)
    z = int(input("Enter total seconds: "))
    secs.append(z)

    if left !=0:
        print(f"\t\tLeft number: {left}")

print(f"Hours: {hrs} \nMinutes: {mins} \nSeconds: {secs}")

a = b = c = 0
for i in hrs:
    a += i

for i in mins:
    b += i

for i in secs:
    c += i

print(f"Totalling....\nHours: {a}, Minutes: {b}, Seconds: {c}")

if c >= 60:
    c_mins = math.floor(c/60)
    c_secs = c%60
else:
    c_mins = 0
    c_secs = c

if b >= 60:
    b_hrs = math.floor(b/60)
    b_mins = b%60
else:
    b_hrs = 0
    b_mins = b

c_mins = c_mins + b_mins
c_hrs = a + b_hrs
print(f"\nTotal timing: {c_hrs}:{c_mins}:{c_secs}")


    