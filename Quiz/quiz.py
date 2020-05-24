print(" ********** **      ** ********         *******    **     ** ** ********")
print("/////**/// /**     /**/**/////         **/////**  /**    /**/**//////** ")
print("    /**    /**     /**/**             **     //** /**    /**/**     **  ")
print("    /**    /**********/*******       /**      /** /**    /**/**    **   ")
print("    /**    /**//////**/**////        /**    **/** /**    /**/**   **    ")
print("    /**    /**     /**/**            //**  // **  /**    /**/**  **     ")
print("    /**    /**     /**/********       //******* **//******* /** ********")
print("    //     //      // ////////         /////// //  ///////  // //////// ")

print("\n\n****This is the quiz section****")
print("RULES:-\t1.There are 3 rounds of this quiz. \n\t2.If you succeed 1st round than you'll be able to get access for second round. \n\t3.You must secure 60% score in the each quiz. \n\t4.You can play the next round if you failed in previous but without a score!\n\tLet's dig in")
player_name = input("Enter Your Name: ")
print("\n\n")

print("$$$$$$$\                                      $$\             $$\   ")
print("$$  __$$\                                     $$ |          $$$$ |  ")
print("$$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$$ |$$\       \_$$ |  ")
print("$$$$$$$  |$$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$ |\__|        $$ |  ")
print("$$  __$$< $$ /  $$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |            $$ |  ")
print("$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\         $$ |  ")
print("$$ |  $$ |\$$$$$$  |\$$$$$$  |$$ |  $$ |\$$$$$$$ |\__|      $$$$$$\ ")
print("\__|  \__| \______/  \______/ \__|  \__| \_______|          \______|")

print("\n\n")
input("Press Enter to continue...")

print("\nQ1. What is the full form of MAC Address?")
print("\t1.Media Access Control \t\t2.Mobile Activity Control \n\t3.Media Access Configurations \t4.Media Access Center")
a1 = int(input("Enter your answer: "))  # Answer=1
print("Q2. In Windows 10, black screen error also called as?")
print("\t1.Dark Error \t2.Dark Entity \n\t3.Death Screen \t4.Death Error")
a2 = int(input("Enter your answer: "))  # Answer=3
print("Q3. MacOS is build by which company?")
print("\t1.Microsoft \t2.Google \n\t3.Amazon \t4.Apple")
a3 = int(input("Enter your answer: "))  # Answer=4
print("Q.4 Which 'Multiple Access' technique mostly uses in telecom?")
print("\t1.CDMA \t2.FDMA \n\t3.TDMA \t4.SDMA")
a4 = int(input("Enter your answer: "))  # Answer=1
print("Q.5 Which year, Android started?")
print("\t1.2009 \t2.2010 \n\t3.2008 \t4.2011")
a5 = int(input("Enter your answer: "))  # Answer=3
print("Q.6 What means of AAPT in Android?")
print("\t1.Android Asset Packaging Tool \t2.Android Asset Packaging Test \n\t3.Android Asset Packages Tool \t4.Android Asset Packages Test")
a6 = int(input("Enter your answer: "))  # Answer=1
print("Q.7 Which question is mostly asked on Google?")
print("\t1.Why is the sky blue \t\t2.Why should we hire you \n\t3.Why is education important \t4.Why is my poop green")
a7 = int(input("Enter your answer: "))  # Answer=1
print("Q.8 What is APM?")
print("\t1.Advanced Power Managing \t2.Advanced Power Management \n\t3.Advanced Power Manager \t4.Advanced Power Manages")
a8 = int(input("Enter your answer: "))  # Answer=2
print("Q.9 What is DLL stands for?")
print("\t1.Dynamic Local Library \t2.Dynamic List Library \n\t3.Dynamic Live Library \t\t4.Dynamic Link Library")
a9 = int(input("Enter your answer: "))  # Answer=4
print("Q.10 MacOS is based on?")
print("\t1.Linux \t2.XNU Kernal \n\t3.Windows \t4.Dos")
a10 = int(input("Enter your answer: "))  # Answer=2

result1 = 0
if(a1 == 1):
    result1 += 1
if(a2 == 3):
    result1 += 1
if(a3 == 4):
    result1 += 1
if(a4 == 1):
    result1 += 1
if(a5 == 3):
    result1 += 1
if(a6 == 1):
    result1 += 1
if(a7 == 1):
    result1 += 1
if(a8 == 2):
    result1 += 1
if(a9 == 4):
    result1 += 1
if(a10 == 2):
    result1 += 1

input("Press Enter to continue...")
print(f"{player_name} scored in round 1: {result1}")
round_1_ans = "Answers: Q1=1, Q2=3, Q3=4, Q4=1, Q5=3\n\t Q6=1, Q7=1, Q8=2, Q9=4, Q10=2"
if(result1 >= 6):
    print("Awesome, You're eligible for next round_2 :)")
    print(round_1_ans)

elif(result1 < 6):
    print("Damn!! \nYou're not allowed for next round :( Good Luck :)")
    print("Press '1' if you want to be continue without a score!\nPress '0' if you wanna quit!")
    print(round_1_ans)
    entry_1 = int(input("Enter your wish:- "))
    if(entry_1 == 0):
        exit(0)
    elif(entry_1 == 1):
        print("Great! You're in")
input("Press Enter to continue...")
print("\n\n")

print("$$$$$$$\                                      $$\            $$$$$$\  ")
print("$$  __$$\                                     $$ |          $$  __$$\ ")
print("$$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$$ |$$\       \__/  $$ |")
print("$$$$$$$  |$$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$ |\__|       $$$$$$  |")
print("$$  __$$< $$ /  $$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |          $$  ____/ ")
print("$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\       $$ |      ")
print("$$ |  $$ |\$$$$$$  |\$$$$$$  |$$ |  $$ |\$$$$$$$ |\__|      $$$$$$$$\ ")
print("\__|  \__| \______/  \______/ \__|  \__| \_______|          \________|")

print("\n\n")

print("Q.1 Who is called as father of Python programming?")
print("\t1.Yukihiro Matsumoto \t2.Guido van Rossum \n\t3.Larry Wall \t\t4.Noam Chomsky")
b1 = int(input("Enter your answer: "))  # Answer=2
print("Q.2 Who is called as father of Bitcoin?")
print("\t1.Schwartz \t\t2.Vitalik Buterin \n\t3.Alex Tapscott \t4.Satoshi Nakamoto")
b2 = int(input("Enter your answer: "))  # Answer=4
print("Q.3 Which award as honor YouTube give to a user after 100 Million subscribers?")
print("\t1.Red Diamond Award \t2.Ruby Diamond Award \n\t3.White Diamond Award \t4.Blue Diamond Award")
b3 = int(input("Enter your answer: "))  # Answer=1
print("Q4. Which shortcut key can directly opens Settings in Windows 10?")
print("\t1.Win+O \t2.Win+S \n\t3.Win+I \t4.Win+J")
b4 = int(input("Enter your answer: "))  # Answer=3
print("Q.5 What is XSS?")
print("\t1.Cross Site Scripting \t\t2.Cross Site Security \n\t3.Cross Security Script \t4.Cross Security Site")
b5 = int(input("Enter your answer: "))  # Answer=1

result2 = 0
if(b1 == 2):
    result2 += 1
if(b2 == 4):
    result2 += 1
if(b3 == 1):
    result2 += 1
if(b4 == 3):
    result2 += 1
if(b5 == 1):
    result2 += 1

input("\nPress Enter to continue...")

if(result1 >= 6 and result2 >= 3):
    print(f"{player_name} scored in round 2: {result2}")
    print(f"Your total score till now: {result1+result2}")
    print("Awesome, You're eligible for next round_3 :)")

print("Answers: Q1=2, Q2=4, Q3=1, Q4=3, Q5=1")

if(result1 < 6 or result2 < 3):
    print("Damn!! \nYou're not allowed for next round :( Good Luck :)\nBut still you can enjoy the next round!")
    print("Press '1' if you want to be continue without a score!\nPress '0' if you wanna quit!")
    entry_1 = int(input("Enter your wish:- "))
    if(entry_1 == 0):
        exit(0)
    elif(entry_1 == 1):
        print("Great! You're in again")
        
input("\nPress Enter to continue...")

print("\n\n")
print("$$$$$$$\                                      $$\            $$$$$$\  ")
print("$$  __$$\                                     $$ |          $$ ___$$\ ")
print("$$ |  $$ | $$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$$ |$$\       \_/   $$ |")
print("$$$$$$$  |$$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$ |\__|        $$$$$ / ")
print("$$  __$$< $$ /  $$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |            \___$$\ ")
print("$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\       $$\   $$ |")
print("$$ |  $$ |\$$$$$$  |\$$$$$$  |$$ |  $$ |\$$$$$$$ |\__|      \$$$$$$  |")
print("\__|  \__| \______/  \______/ \__|  \__| \_______|           \______/ ")

print("\n\n")

print("Q1. What is CIA in Information Security?")
print("\t1.Confidentiality, Integrity, Availability \t2.Confidentiality, Integrity, Advancement \n\t3.Confidentiality, Integrity, Affirmative \t4.Confidentiality, Integrity, Action")
c1=int(input("Enter your answer: "))  # Answer=1
print("Q2. Which is the most notorious cyberattack?")
print("\t1.Stuxnet: A smoking cybergun \t\t\t\t2.DarkHotel: Spies in suite rooms \n\t3.NotPetya/ExPetr: The costliest cyberattack to date \t4.WannaCry: A real epidemic")
c2=int(input("Enter your answer: "))  # Answer=4
print("Q.3 What is the most searched for thing on Google?")
print("\t1.YouTube \t2.Facebook \n\t3.Gmail \t4.Amazon")
c3=int(input("Enter your answer: "))  # Answer=2

result3 = 0
if(c1 == 1):
    result3 += 1
if(c3 == 4):
    result3 += 1
if(c3 == 2):
    result3 += 1

input("Press Enter to continue...")
if(result1>=6 and result2>=3 and result3>=2):
    print("{player_name} scored in round 3: {result3}")
    print(f"Your total score till now: {result1+result2+result3}")
    print("Awesome, You're the WINNER of the QUIZ :)")

elif(result1 < 6 or result2 < 3 or result3 < 2):    
    print("Damn!! \nYou missed the gossips! :( Good Luck :)")
    print("Thanks for giving your time! :)")

print("Answers: Q1=1, Q2=4, Q3=2")
exit(0)