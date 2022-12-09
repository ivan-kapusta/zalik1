f=open("text.txt","r")

#aaa=input("введіть якесь число у форматі 'AAA': ")
aaa="123"

if len(aaa)!=3:
    print("введіть 3 цифрове число!")
    quit()

try: aaa=int(aaa)
except ValueError:
    print("використайте число")
    quit()

arr=[]
for i in f:
    arr.append(i)

g=0
hh=[]
tempmm=[]
xxx=[]
for i in arr:
    hh.append(arr[g][:2])
    tempmm.append(arr[g][:5])
    xxx.append(arr[g][6:])
    g+=1

g=0
mm=[]
for i in tempmm:
    mm.append(tempmm[g][3:])
    g+=1

try:
    g=0
    for i in arr:     
        hh[g]=int(hh[g])
        mm[g]=int(mm[g])
        xxx[g]=int(xxx[g])
        g+=1
except ValueError:
    print("некоректний ввід данних(має бути час у форматі HH:MM та 3 цифрове число")

g=0
for i in arr:
    if hh[g]>=24 or hh[g]<0:
        print(f"введено некоректний час у {g+1} строчці текстового файлу")
        quit()
    if mm[g]>=60 or mm[g]<0:
        print(f"введено некоректний час у {g+1} строчці текстового файлу")
        quit()
    else:
        g+=1


g=0
for i in xxx:
    if i>aaa:
        print(f"введене значення ААА менше за значення при цьому часі - {hh[g]}:{mm[g]}")
        g+=1
    else:g+=1