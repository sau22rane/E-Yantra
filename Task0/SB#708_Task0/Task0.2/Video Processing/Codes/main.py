import cv2
import numpy as np
import os

dirc = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def partA():
    vdo=cv2.VideoCapture(dirc+"\\Videos\\RoseBloom.mp4")
    fps = vdo.get(cv2.CAP_PROP_FPS)
    count=0
    while(True):
        ret, frame = vdo.read()
        if(count==int(fps)*6):
            cv2.imwrite(dirc+"\\Generated\\frame_as_6.jpg",frame)
            break
        count+=1
    pass

def partB():
    img=cv2.imread(dirc+"\\Generated\\frame_as_6.jpg",1)
    cv2.imwrite(dirc+"\\Generated\\frame_as_6_red.jpg",img[:,:,2])
    pass

partA()
partB()
