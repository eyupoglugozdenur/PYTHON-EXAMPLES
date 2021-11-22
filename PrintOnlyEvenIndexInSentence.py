st = 'Print every word in this sentence that has an even number of letters'

list=[]
counter=0

for letter in st:
    counter+=1
    index=counter-1
    
    if index%2==0:
        list.append(letter)
    
print(list)