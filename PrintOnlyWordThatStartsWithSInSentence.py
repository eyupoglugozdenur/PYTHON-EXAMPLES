st = 'Print only the words that start with s in this sentence'
list=[]
for word in st.split():
    if word[0]=='s':
        list.append(word)
        
        
print(list)