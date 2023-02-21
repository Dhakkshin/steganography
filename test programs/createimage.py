from PIL import Image
im=Image.frombytes(mode='RGBA', size=(w,h), data=)
im.show()































cntrl=0
#lislen=len(updatedpics)
for i in range(w):
    for j in range(h):
        r=updatedpics[0][0]
        g=updatedpics[0][1]
        b=updatedpics[0][2]
        a=updatedpics[0][3]
        #print(r,g,b,a)
        pixel_map[i, j] =(int(r,2), int(g,2), int(b,2), int(a,2))
        updatedpics.pop(0)
        cntrl+=1
        #print(cntrl)
        if cntrl==lislen:
            #print('qwerty')
            break
    if cntrl==lislen:
        break
img.save("steg_img", format="png")
img.show()
img.close()
print('done4')
