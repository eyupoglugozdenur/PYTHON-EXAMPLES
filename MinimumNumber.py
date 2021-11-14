num1=int(input("Please Ente Number 1: "))
num2=int(input("Please Ente Number 2: "))
num3=int(input("Please Ente Number 3: "))

min=num1

if num2<min:
    min=num2
    
if num3<min:
    min=num3
    
print("Minimum Number Is:", min)