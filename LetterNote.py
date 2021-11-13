#This program is printing the user's letter note that entered via keyboard

note=int(input("Please Enter Your Note: "))
if note>=88:
    print("Your letter Note Is: AA")
elif note>=81:
    print("Your Letter Note Is: BA")
elif note>=74:
    print("Your Letter Note Is: BB")
elif note>=67:
    print("Your Letter Note Is: CB")
elif note>=60:
    print("Your Letter Note Is: CC")
elif note>=53:
    print("Your Letter Note Is: DC")
elif note>=45:
    print("Your Letter Note Is: DD")
else:
    print("Your Letter Note Is: FF")
    
if note>=45:
    print("Congratulations! You've passed the exam!")
else:
    print("You've not passed the exam!")