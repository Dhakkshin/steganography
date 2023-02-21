from PIL import Image
#right click on the desired image and select 'copy as path' and give it as the input
image_path=input('Enter the full file path for the image:').strip('"')
orig_img=Image.open(image_path)
w,h=orig_img.size
for i in range(w):
    for j in range(h):
        r,g,b,a=orig_img.getpixel((i,j))
        r,g,b,a=bin(r).removeprefix('0b'),bin(g).removeprefix('0b'),bin(b).removeprefix('0b'),bin(a).removeprefix('0b')
        if len(r)<8:
            r='0'*(8-len(r)) + r
        if len(g)<8:
            g='0'*(8-len(g)) + g
        if len(b)<8:
            b='0'*(8-len(b)) + b
        if len(a)<8:
            a='0'*(8-len(a)) + a
        print(chr(int(r[-2:] + g[-2:] + b[-2:] + a[-2:] , 2)),end='')
        
