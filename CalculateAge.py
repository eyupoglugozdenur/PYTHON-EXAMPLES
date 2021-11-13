#Age Calculator 

print("Please Enter The Birth Date!")

day=int(input("Day: "))#Birth Day
while 1:
    if day <=0:
        print("Invalid Value!")
        day=int(input("Please Enter The Birth Day Again!"))
    elif day >31:
        print("Invalid Value!")
        day=int(input("Please Enter The Birth Day Again!"))
    else:
        break
        
month=int(input("Month: ")) #Birth Month
while 1:
    if month <=0:
        print("Invalid Value!")
        month=int(input("Please Enter The Birth Month Again!"))
    elif month >31:
        print("Invalid Value!")
        month=int(input("Please Enter The Birth Month Again!"))
    else:
        break
        
year=int(input("Year: ")) #Birth Year
while 1:
    if year <=0:
        print("Invalid Value!")
        year=int(input("Please Enter The Birth Year Again!"))
    elif year>2021:
        print("Year can be Maximum 2021!")
        year=int(input("Please Enter The Birth Year Again!"))
    else:
        break

print("Please Enter the Today's Date!")

tDay=int(input("Day: ")) #Today's Day
while 1:
    if tDay <=0:
        print("Invalid Value!")
        tDay=int(input("Please Enter The Day Again!"))
    elif tDay >31:
        print("Invalid Value!")
        tDay=int(input("Please Enter The Day Again!"))
    else:
        break

tMonth=int(input("Month: ")) #Months
while 1:
    if tMonth <=0:
        print("Invalid Value!")
        tMonth=int(input("Please Enter The Today's Month Again!"))
    elif tMonth >31:
        print("Invalid Value!")
        tMonth=int(input("Please Enter The Today's Month Again!"))
    else:
        break

tYear=int(input("Year: ")) #Year
while 1:
    if tYear <=0:
        print("Invalid Value!")
        tYear=int(input("Please Enter The Birth Year Again!"))
    elif tYear>2021:
        print("Year can be Maximum 2021!")
        tYear=int(input("Please Enter The Birth Year Again!"))   
    else:
        break
        
ageD= tDay-day
if ageD<0:
    ageD=-ageD # or abs(ageD)
ageM= tMonth-month
if ageM<0:
    ageM=-ageM # or abs(ageM)
ageY=tYear-year

print("You\'re {} Years {} Months and {} Days Old".format(ageY,ageM,ageD))