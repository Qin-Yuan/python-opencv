# coding:utf-8
# opencv_03图像运算(一)
# author：Qinyuan

from cv2 import cv2
import numpy as np

###########
### 例1 ###
img1 = np.random.randint(0,256,size=[3,3],dtype=np.uint8)
img2 = np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print("img1=\n",img1)
print("img2=\n",img2)
print("img1+img2=\n",img1+img2)
print("cv2.add(img1,img2)=\n",cv2.add(img1,img2))

############
### 例2 ###
a = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\hai_640x450.png")
b = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\opencv_640x450.png")
result = cv2.addWeighted(a,0.6,b,0.4,0)
cv2.imshow("result",result)
cv2.imwrite(r"F:\USER\Desktop\Benny\benny\opencv\picture\result_640x450.png",result)
cv2.waitKey()
cv2.destroyAllWindows()

############
### 例3 ###
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\opencv_logo.png")
mask = np.zeros(img.shape,dtype=np.uint8)
mask[250:340,30:340,:]=255
result = cv2.bitwise_and(img,mask)
cv2.imshow("result",result)
cv2.waitKey()
cv2.destroyAllWindows()

############
### 例4 ###
img = np.ones([3,3],dtype=np.uint8)*4
result = cv2.add(img,3)
print("img=\n",img)
print("result=\n",result)
