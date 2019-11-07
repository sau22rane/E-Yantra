import cv2
import numpy as np
import os

dirc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def partA():
    items = os.listdir(dirc+"\\Images")
    fp=open(dirc+"\\Generated\\stats.csv",'+w')
    for item in items:
        img=cv2.imread(dirc+"\\Images\\"+item,1)
        h,w,n=img.shape
        B,G,R = img[int(h/2),int(w/2),0],img[int(h/2),int(w/2),1],img[int(h/2),int(w/2),2]
        content=item+','+str(h)+','+str(w)+','+str(n)+','+str(B)+','+str(G)+','+str(R)+'\n'
        fp.write(content)
    pass

def partB():
    img=cv2.imread(dirc+"\\Images\\cat.jpg",1)
    cat_red = img[:,:,2]
    cv2.imwrite(dirc+"\\Generated\\cat_red.jpg",cat_red)
    pass

def partC():
    img=cv2.imread(dirc+"\\Images\\flowers.jpg",1)
    rgba=cv2.cvtColor(img,cv2.COLOR_RGB2RGBA)
    rgba[:, :, 3]=rgba[:, :, 3]*0.5
    cv2.imwrite(dirc+"\\Generated\\flowers_alpha.png",rgba)
    pass

def partD():
    img=cv2.imread(dirc+"\\Images\\horse.jpg",1)
    I=0.3*img[:,:,2]+0.59*img[:,:,1]+0.11*img[:,:,0]
    cv2.imwrite(dirc+"\\Generated\\horse_gray.jpg",I)
    pass

partA()
partB()
partC()
partD()
