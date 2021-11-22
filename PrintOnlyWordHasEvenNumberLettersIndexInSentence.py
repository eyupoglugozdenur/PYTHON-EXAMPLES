st = 'Print every word in his sentence that has an even number of letters'

list=[]
counter=0

for word in st.split():
    
    lenght=len(word)
    
    if lenght%2==0:
        list.append(word)
    
print(list)