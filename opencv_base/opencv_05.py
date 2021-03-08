# coding:utf-8
# opencv_04色彩空间
# author：Qinyuan

from cv2 import cv2
import numpy as np

##########
### 例1 ##
BGR = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\baby_200.jpg")
cv2.imshow("BGR",BGR)
#转化为RGB
RGB = cv2.cvtColor(BGR,cv2.COLOR_BGR2RGB)
cv2.imshow("RGB",RGB)
#转化为HSV
HSV = cv2.cvtColor(BGR,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",HSV)
#转化为GRAY
GRAY = cv2.cvtColor(BGR,cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY",GRAY)
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例2 ##
创建三通道的图像像素值
Green_BGR = np.zeros([1,1,3],dtype=np.uint8)
#将G（绿色）通道显示纯绿色，设置为255
Green_BGR[0,0,1]=255
#转为HSV色彩空间 
Green_HSV = cv2.cvtColor(Green_BGR,cv2.COLOR_BGR2HSV)
#输出对应的值
print("BGR=",Green_BGR)
print("HSV",Green_HSV)

##########
### 例3 ##
img = np.random.randint(0,256,size=[3,3],dtype=np.uint8)
min = 100
max = 200
dst = cv2.inRange(img,min,max)
print("img=\n",img)
print("dst=\n",dst)

##########
### 例4 ##
img = np.random.randint(0,256,size=[5,5],dtype=np.uint8)
#设置像素下限
min = 100
#设置像素上限
max = 200
#范围单元处理
mask = cv2.inRange(img,min,max)
#按位与操作得到处于该范围内的像素值
ROI = cv2.bitwise_and(img,img,mask=mask)
print("img=\n",img)
print("mask=\n",mask)
print("ROI=\n",ROI)

##########
### 例5 ##
BGR = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\baby_200.jpg")
cv2.imshow("BGR",BGR)
#转化为HSV
HSV = cv2.cvtColor(BGR,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",HSV)
############ 指定蓝色值的范围 ##############
min_blue = np.array([0,50,50])
max_blue = np.array([10,255,255])
# 确定蓝色区域
mask = cv2.inRange(HSV,min_blue,max_blue)
cv2.imshow("mask",mask)
# 通过按或与操作提取红色区域
result = cv2.bitwise_and(BGR,BGR,mask=mask)
cv2.imshow("result",result)
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例6 ##
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\face.jpg")
cv2.imshow("img",img)
HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#将HSV色彩空间通道拆分
h,s,v = cv2.split(HSV)
#设置色调上、下限
min_H = 5
max_H = 170
#处理色调范围
mask_h = cv2.inRange(h,min_H,max_H)
#设置饱和度上、下限
min_s = 25
max_s = 166
#处理饱和度范围
mask_s = cv2.inRange(s,min_s,max_s)
#得到脸部肤色的mask
mask = mask_h & mask_s
#获得最后结果图 ROI
ROI = cv2.bitwise_and(img,img,mask = mask)
cv2.imshow("ROI",ROI)
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例7 ##
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\face.jpg")
cv2.imshow("img",img)
HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#将HSV色彩空间通道拆分
h,s,v = cv2.split(HSV)
#将亮度V全赋值为255
v[:,:]=255
#通道合成
hsv = cv2.merge([h,s,v])
art = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow("art",art)
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例8 ##
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\baby_200.jpg")
cv2.imshow("BGR",img)
#转为BGRA四通道
alpha = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
#对图像进行通道拆分
b,g,r,a = cv2.split(alpha)
#赋值a为255,与原图一致
a[:,:]=255
#通道合成
alp_255 = cv2.merge([b,g,r,a])
cv2.imshow("255",alp_255)
#赋值a为125
a[:,:] = 125
alp_125 = cv2.merge([b,g,r,a])
cv2.imshow("125",alp_125)
#赋值a为0
a[:,:] = 0
alp_0 = cv2.merge([b,g,r,a])
cv2.imshow("0",alp_0)
#保存图像至本地
cv2.imwrite(r"F:\USER\Desktop\Benny\benny\opencv\picture\alpha\alp_255.png",alp_255)
cv2.imwrite(r"F:\USER\Desktop\Benny\benny\opencv\picture\alpha\alp_0.png",alp_0)
cv2.imwrite(r"F:\USER\Desktop\Benny\benny\opencv\picture\alpha\alp_125.png",alp_125)
cv2.waitKey()
cv2.destroyAllWindows()
