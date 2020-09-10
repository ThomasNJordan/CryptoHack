from pwn import *
import cv2
import numpy as np 

img1 = cv2.imread('flag.png')  
img2 = cv2.imread('lemur.png') 
  
# cv2.bitwise_and is applied over the 
# image inputs with applied parameters  
dest_and = cv2.bitwise_and(img2, img1, mask = None) 
  
# the window showing output image 
# with the Bitwise AND operation 
# on the input images 
cv2.imshow('Bitwise And', dest_and) 
   
# De-allocate any associated memory usage   
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  

    #Outputs: crypto{X0Rly_n0t!}