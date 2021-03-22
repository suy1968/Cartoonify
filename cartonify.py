import cv2
import matplotlib.pyplot as plt

num_down = 2
num_bilateral = 7
img = cv2.imread(r"C:\Users\Admin\Downloads\test.jpg")
print(img.shape)

# resizing image
img = cv2.resize(img,(800,800))

# downsample image using Gaussian Pyramid
img_color = img
for _ in range(num_down):
    img_color = cv2.pyrDown(img_color)
    
    
# repeatedly apply small bilateral filter instead of applying one large filter
for _ in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color,d=9,sigmaColor=9,sigmaSpace=7)
    
# Upsampling image to original size

for _ in range(num_down):
    img_color = cv2.pyrUp(img_color)
    
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(img_gray,7)
img_edge = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=9,C=2)

img_edge = cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB)
img_cartoon = cv2.bitwise_and(img_color,img_edge)

# display

plt.imshow(img_cartoon)
plt.show()
