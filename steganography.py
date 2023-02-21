#steganography

from PIL import Image
import csv

#file=open('pics_els.csv','w',newline='')
#w_object=csv.writer(file)
imgfilename='image.png'#str(input('Enter the file path of the image with extension:'))
txtfilename='content.txt'#str(input('Enter the file path of the text file with extension:'))

orig_img=Image.open(imgfilename)
orig_pixel_map=orig_img.load()

w,h=orig_img.size
#print(w,h)
orig_pixels=[]
for i in range(w):
    for j in range(h):
        r,g,b,a=orig_img.getpixel((i,j))
        r,g,b,a=bin(r),bin(g),bin(b),bin(a)
        r,g,b,a=r.removeprefix('0b'),g.removeprefix('0b'),b.removeprefix('0b'),a.removeprefix('0b')
        #print(r,g,b,a)
        if len(r)<8:
            r='0'*(8-len(r)) + r
        if len(g)<8:
            g='0'*(8-len(g)) + g
        if len(b)<8:
            b='0'*(8-len(b)) + b
        if len(a)<8:
            a='0'*(8-len(a)) + a
        #print(r,g,b,a)
        #w_object.writerow([r,g,b,a])
        orig_pixels.append([r,g,b,a])

#file.close
print('done')
################################

file=open(txtfilename,'r',encoding="utf8")
text=file.read()
text= text + '\n\n\n\nTHIS IS THE END OF HIDDEN MESSAGE. PRESS <CTRL+C> NOW\n\n\n\n'
lis=[]
for i in text:
    a=ord(i)
    b=bin(a)
    b=b.removeprefix('0b')
    if len(b)<8:
        b='0'*(8-len(b)) + b
    lis.append(b)
file.close()

#print('lis',len(lis))
file=open('bincontent.csv','w',newline='')
w_object=csv.writer(file)
for i in lis:
    w_object.writerow(i)
file.close()
print('done2')

######################################

#file=open('pics_els.csv','r+',newline='')
#freader=csv.reader(file)
updatedpics=[]
cntrl=0
lislen=len(lis)
for i in orig_pixels:
    r=i[0][:-2]+lis[0][0:2]
    g=i[1][:-2]+lis[0][2:4]
    b=i[2][:-2]+lis[0][4:6]
    a=i[3][:-2]+lis[0][6:]
    lis.pop(0) 
    updatedpics.append([r,g,b,a])
    cntrl+=1
    if cntrl==lislen:
        break

#print(lis)
#print(updatedpics,len(updatedpics))
file.close()
print('done3')

###########################
new_image = Image.new(mode='RGBA', size=(w,h))
new_pixel_map = new_image.load()
for x in range(w):
    for y in range(h):
        new_pixel_map[x, y] = orig_pixel_map[x, y]

cntrl=0
lislen=len(updatedpics)
for i in range(w):
    for j in range(h):
        r=updatedpics[0][0]
        g=updatedpics[0][1]
        b=updatedpics[0][2]
        a=updatedpics[0][3]
        #print(r,g,b,a)
        new_pixel_map[i, j] =(int(r,2), int(g,2), int(b,2), int(a,2))
        updatedpics.pop(0)
        cntrl+=1
        #print(cntrl)
        if cntrl==lislen:
            #print('qwerty')
            break
    if cntrl==lislen:
        break
    
new_image.save('final image.png')
print('done4')
