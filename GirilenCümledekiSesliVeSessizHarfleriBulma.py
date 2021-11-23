#Kullanıcı tarafından girilen cümledeki sesli ve sessiz harfleri bulan ve bunları yazdıran program

string=input("Lütfen İstediğiniz Bir Cümleyi Yazınız: ") #Kullanıcıdan cümle istenir

liste1=[]
liste2=[]
liste3='aeıioöuü' #Türkçedeki sesli harfler

sesliHarf=0 #Başlangıçtaki sesli harf sayısı sıfır
sessizHarf=0 #Başlangıçtaki sessiz harf sayısı sıfır

for letter in string:
    if letter in liste3:
      if letter not in liste1: #Eğer sesli harf liste1'e daha önce eklenmediyse ekle! 
        liste1.append(letter)
      sesliHarf+=1 #Sesli harf sayısını 1 arttır
      
        
    else:
      if letter not in liste2:#Eğer sessiz harf liste2'ye daha önce eklenmediyse ekle!
        liste2.append(letter)
      sessizHarf+=1 #Sessiz harf sayısını 1 arttır
        
print("Sesli Harf Sayısı: {} \nSessiz Harf Sayısı: {}".format(sesliHarf,sessizHarf)) #Cümledeki sesli ve sessiz harf sayısı ekrana yazdırılır
print("Sesli Harfler: {} \nSessiz Harfler: {}".format(liste1,liste2)) #Cümledeki sesli ve sessiz harfler ekrana yazdırılır