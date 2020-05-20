empLi1 = []
empLi2 = []
def excNum():
    input_n = "Enter the length for the numbers. Ex. 2 or 4: "
    empLi1.append(input_n)
    n = int(input(input_n))
    empLi2.append(n)
    if n%2==0:
        li = []
        left = n
        for i in range(n):    
            left -= 1
            input_x = "Enter element: "
            empLi1.append(input_x)
            x = int(input(input_x))
            empLi2.append(x)
            if left !=0:
                print(f"\t\tLeft number: {left}")
            li.append(x)

        print(f"Total elements: {li}")
        half_1 = li[:len(li)//2]
        half_2 = li[len(li)//2:]
        print(f"First half: {half_1} & Second half: {half_2}")
        full = int("".join(map(str,li)))
        half_1X = int("".join(map(str,half_1)))
        half_2X = int("".join(map(str,half_2)))
        print(f"\nAfter, Full length: {full} First half: {half_1X} & Second half: {half_2X}")
        a = half_1X**2
        print(f"Square of {half_1X} : {a}")
        b = half_2X**2
        print(f"Square of {half_2X} : {b}")
        c = b - a
        print(f"The subtraction of {b} - {a} : {c}")
        if c == full:
            print(f"The given items fullfill the requirement. \n{full} = {c}")
        else:
            print(f"Given items doesn't fullfill the requirements!!! \n{full} != {c}")

    else:
        print("Your length must be \"EVEN\"")
        input_x = "Enter 1 for retry, else press anything to exit!!! "
        empLi1.append(input_x)
        x = int(input(input_x))
        empLi2.append(x)
        if x != 1:
            print(f"User's query: {dict(zip(empLi1, empLi2))}")
            exit(0)
        else:
            return excNum()
excNum()
print(empLi1)
print(empLi2)
print(f"User's query: {dict(zip(empLi1, empLi2))}")
