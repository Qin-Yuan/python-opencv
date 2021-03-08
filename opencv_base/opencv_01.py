# coding:utf-8
# opencv_01入门opencv
# author：Qinyuan

# 导入库
#import cv2 
from cv2 import cv2  

# cv2.imread()函数读取图片
a = cv2.imread("f:/USER/Desktop/Benny/benny/opencv/picture/opencv_logo.png")
b = cv2.imread("f:/USER/Desktop/Benny/benny/opencv/picture/opencv_logo.png", 0 )
c = cv2.imread("f:/USER/Desktop/Benny/benny/opencv/picture/opencv_logo.png", 1 )
# imshow()显示图片
cv2.imshow("a",a)
cv2.imshow("b",b)
cv2.imshow("c",c)
cv2.waitKey()
cv2.destroyAllWindows()
