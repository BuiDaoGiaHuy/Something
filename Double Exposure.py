import cv2
import numpy as np

def blend(img1, alpha, img2, beta, gamma):
  #dst=alpha*img1 + beta*img2 + gamma
  dst=float(alpha)*img1 + float(beta)*img2+gamma
  dst=np.where(dst>255,255,dst)
  return dst.astype(np.uint8)

girl=cv2.imread(r'D:\Dowload\girl.jpg')
mask=cv2.imread(r'D:\Dowload\mask.png')
fire=cv2.imread(r'D:\Dowload\fire.jpg')
#cv2.imshow('girl',girl)
#cv2.imshow('mask',mask)
#cv2.imshow('fire',fire)
non_black_pixels=(mask!=0).all(axis=2)
temp=girl.copy()
temp[non_black_pixels]=fire[non_black_pixels]

h,w,d=girl.shape
cap=cv2.VideoCapture(r'C:\Users\HELLO\Desktop\Animated_fire_by_nevit.gif')
i=1
while 1:
    ret, frame = cap.read()
    if not ret: break
    frame=cv2.resize(frame,(w,h))
    temp=girl.copy()
    temp[non_black_pixels]=frame[non_black_pixels]
    blended=blend(girl,0.5,temp,0.5,0)
    h_,w_=int(h*i),int(w*i)
    blended=cv2.resize(blended,(w_,h_))
    off_h,off_w=(h_-h)//2,(w_-w)//2
    cv2.imshow('blended',blended[off_h:off_h+h,off_w:off_w+w])
    i+=0.008
    cv2.waitKey(50)

