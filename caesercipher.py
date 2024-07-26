user=input("write your message")
ls=list(user)
print(ls)
po=input("add secret code")
pos=int(po)
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(ls)):
    if ls[i].isalpha():
        index=alphabets.index(ls[i])
        ls[i]=alphabets[(index+pos)%26]
str=""
lis=str.join(ls)
print(lis)

post=input("enter secret code")
io=int(post)
mess=input("enter secret message")
messt=list(mess)
print(messt)
for i in range(len(messt)):
    if messt[i].isalpha():
        indext=alphabets.index(messt[i])
        messt[i]=alphabets[(indext-io)%26]
        
str1=""
decode=str.join(messt)
print(decode)


        
        
