# coding:utf-8
# opencv_03图像运算(二)
# author：Qinyuan

from cv2 import cv2
import numpy as np

##########
### 例1 ##
#参数为0，灰度图像
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\baby_200.jpg",0)
cv2.imshow("img",img)
#获得img图像的像素
r,c=img.shape
#构造提取矩阵
x = np.zeros((r,c,8),dtype=np.uint8)
#将提取矩阵每层像素值赋值
for i in range(8):
    x[:,:,i]=2**i
#构造为平面存储矩阵
y = np.zeros((r,c,8),dtype=np.uint8)
#按位与提取位平面
for i in range(8):
    y[:,:,i]=cv2.bitwise_and(img,x[:,:,i])
    #阈值处理
    mask = y[:,:,i]
    y[mask]=255
    cv2.imshow(str(i),y[:,:,i])
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例2 ##
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\baby_200.jpg",0)
cv2.imshow("a",img)
#获得img图像的像素
r,c=img.shape
#用np.random.randint()构造随机密钥
key = np.random.randint(0,256,size=(r,c),dtype=np.uint8)
cv2.imshow("b", key)
#按位异或进行图像加密
encryption=cv2.bitwise_xor(img,key)
decryption=cv2.bitwise_xor(encryption,key)
cv2.imshow("c", encryption)
cv2.imshow("a1", decryption)
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例3 ##
读取原始载体图像
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\baby_200.jpg",0)
r,c=img.shape
#显示原图像
cv2.imshow("img",img)
#构建随机水印图像
watermark = np.random.randint(0,256,size=(r,c),dtype=np.uint8)
#化为255
w = watermark[:,:]>0
watermark[w]=255
cv2.imshow("1",watermark)
#阈值处理，将其处理为二值图像
w = watermark[:,:]>0
watermark[w]=1
#显示水印图像
cv2.imshow("watermark",watermark)

############# 水印嵌入 #############
#生成元素值都是254的数组
t254=np.ones((r,c),dtype=np.uint8)*254
#保留原始载体图像的高七位
imgH7=cv2.bitwise_and(img,t254)
cv2.imshow("H7",imgH7)
#将watermark嵌入嵌入imgH7内
result = cv2.bitwise_or(imgH7,watermark)
#显示水印嵌入结果
cv2.imshow("r1",result)

############# 提取过程 #############
#生成元素值为1的数组
t1 = np.ones((r,c),dtype=np.uint8)
#从水印图像中提取出水印图像
result2 = cv2.bitwise_and(result,t1)
#将水印图像值1处理为255，以方便显示
w = result2[:,:]>0
result2[w]=255
#显示提取出的水印
cv2.imshow("r2",result2)
cv2.waitKey()
cv2.destroyAllWindows()

##########
### 例4 ##
img = cv2.imread(r"F:\USER\Desktop\Benny\benny\opencv\picture\baby_200.jpg",0)
r,c=img.shape
cv2.imshow("img",img)
#生成掩膜图
mask = np.zeros((r,c),dtype=np.uint8)
mask[70:120,70:120]=1
face = cv2.bitwise_and(img,mask*255)
cv2.imshow("1",face)

#随机生成一个用于打码和解码的密钥
key=np.random.randint(0,256,size=[r,c],dtype=np.uint8)
########### 对面部进行打码 ##########
#使用密钥key对img进行加密
img_key = cv2.bitwise_xor(img,key)
#获取加密图像的脸部信息
face_key = cv2.bitwise_and(img_key,mask*255)
cv2.imshow("2",face_key)
#除去img中的脸部信息
img_no_face = cv2.bitwise_and(img,(1-mask)*255)
cv2.imshow("3",img_no_face)
#对img图像脸部进行打码
img_face_key = img_no_face + face_key
cv2.imshow("4",img_face_key)

########### 对脸部进行解码 ############
#将打码的img_face_key与key进行异或获取脸部信息
img_face = cv2.bitwise_xor(img_face_key,key)
cv2.imshow("5",img_face)
#将解码脸部信息提取出来
face1 = cv2.bitwise_and(img_face,mask*255)
cv2.imshow("6",face1)
#从脸部打码的img_face_key提取出没有脸部信息的图像
img_no_face1 = cv2.bitwise_and(img_face_key,(1-mask)*255)
cv2.imshow("7",img_no_face1)
#得到解码的img图像
img1 = img_no_face1 + face1 
cv2.imshow("8",img1)
cv2.waitKey()
cv2.destroyAllWindows()
