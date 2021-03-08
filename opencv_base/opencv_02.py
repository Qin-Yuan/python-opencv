# coding:utf-8
# opencv_02图像处理基础
# author：Qinyuan

from cv2 import cv2  
import numpy as np


#二值图像
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\code\o.png",cv2.IMREAD_REDUCED_GRAYSCALE_8)
print(img)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows() 

##########
### 例1 ##
img = np.zeros((8,8),dtype=np.uint8)
print("img=\n",img)
cv2.imshow('before',img)
print('读取像素点img[3,3]=',img[3,3])
img[3,3]=255
print("修改后的img=\n",img)
print('读取修改后的像素点img[3,3]=', img[3,3])
cv2.imshow('after',img)
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例2 ##
#--------蓝色通道值----------
blue=np.zeros((300,300,3),dtype=np.uint8)
blue[:,:,0]=255
print('blue=\n',blue)
cv2.imshow("blue",blue)
#--------绿色通道值----------
green=np.zeros((300,300,3),dtype=np.uint8)
green[:,:,1]=255
print('green=\n',green)
cv2.imshow("green",green)
#--------红色通道值----------
red=np.zeros((300,300,3),dtype=np.uint8)
red[:,:,2]=255
print('red=\n',red)
cv2.imshow("red",red)
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例3 ##
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\code\opencv_logo.png",0)
#测试读取、修改翻个像素值
print("读取像素点img.item(3,2)=",img.item(3,2))
img.itemset((3,2),255)
print("修改后像素点img.item(3,2)=",img.item(3,2))
#测试修改一个区域的像素值
cv2.imshow("img",img)
for i in range(10,50):
    for j in range(30,60):
        img.itemset((i,j),0)
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例4 ##
img = np.random.randint(0,256,size=[256,256,3],dtype=np.uint8)
cv2.imshow("one",img)
print("读取BGR像素点img.item(100,100,1)=",img.item(100,100,1))
img.itemset((100,100,1),255)
print("修改后BGR像素点img.item(100,100,1)=",img.item(100,100,1))
#修改一片区域
for i in range(50,100):
    for j in range(50,100):
        for n in range(0,1):
            img.itemset((i,j,n),255)
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例5 ##
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\baby.jpg",cv2.IMREAD_REDUCED_COLOR_2)
img1 = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\baby.jpg",cv2.IMREAD_REDUCED_COLOR_2)
#创建脸部信息存储矩阵
mask1=np.ones((100,100,3),dtype=np.uint8)
mask2=np.ones((100,100,3),dtype=np.uint8)
#海绵宝宝的脸部信息
mask1=img1[200:300,200:300,:]
#派大星的脸部信息
mask2=img1[100:200,350:450,:]
#显示原图
cv2.imshow("img",img)
#显示海绵宝宝的脸
cv2.imshow("face1",mask1)
#显示派大星的脸
cv2.imshow("face2",mask2)
#换脸
img[200:300,200:300,:]=mask2
img[100:200,350:450,:]=mask1
#显示换脸后的图像
cv2.imshow("after",img)
cv2.waitKey()
cv2.destroyAllWindows()
