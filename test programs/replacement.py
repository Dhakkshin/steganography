import csv
#file1=open('bincontent.csv','r+',newline='')
#freader1=csv.reader(file1)
file=open('pics_els.csv','r+',newline='')
freader=csv.reader(file)

for i in freader2:
    r=i[0].replace(i[0][-2:],lis[0][0:2])
    g=i[1].replace(i[1][-2:],lis[0][2:4])
    b=i[2].replace(i[2][-2:],lis[0][4:6])
    a=i[3].replace(i[3][-2:],lis[0][6:])
    lis.pop(0)
