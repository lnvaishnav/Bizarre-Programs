def bmi_Calculator():
    name = input("Enter your name: ")
    a = eval(input("Enter your age: "))
    if a >= 18 and a <= 65:
        print("Your age is perfect for BMI")
        w = eval(input("Enter your weight: "))
        h = float(input("Enter your height: "))
        x = h/100
        bmi = (w / (x*x))
        print(f"Your BMI according to Data is: {bmi:.02f}")
        if bmi > 25:
            print(f"{name} is over weighted!")
        elif bmi >= 18 and bmi <= 24.9:
            print(f"{name} is  healthy")
        elif bmi <18:
            print(f"{name} is  under weight")
    else:
        print("Sorry!!, Please enter correct age.")

bmi_Calculator()
while True:
    test = int(input("If you wanna continue, enter 1, else anything: "))
    if test == 1:
        bmi_Calculator()
    else:
        break
