#girilen sayının rakamlarının çarpımını bulma

number=int(input("Please Enter A Number: "))
product=1 #çarpımdaki etkisiz eleman

for numeral in str(number):
    product*=int(numeral)
print(product)