file=open('content.txt','r',encoding="utf8")
text=file.read()
lis=[]
for i in text:
    a=ord(i)
    b=bin(a)
    b=b.removeprefix('0b')
    if len(b)<8:
        b='0'*(8-len(b)) + b
    lis.append(b)

print(lis)

for i in lis:
    a=int(i,2)
    b=chr(a)
    print(b,end='')
