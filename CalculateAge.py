#Age Calculator 

print("Please Enter The Birth Date!")
day=int(input("Day: "))#Birth Day
month=int(input("Month: ")) #Birth Month
year=int(input("Year: ")) #Birth Year

print("Please Enter the Today's Date!")
tDay=int(input("Day: ")) #Today's Day
tMonth=int(input("Month: ")) #Months
tYear=int(input("Year: ")) #Year

ageD= tDay-day
if ageD<0:
    ageD=-ageD # or abs(ageD)
ageM= tMonth-month
if ageM<0:
    ageM=-ageM # or abs(ageM)
ageY=tYear-year

print("You\'re {} Years {} Months and {} Days Old".format(ageY,ageM,ageD))