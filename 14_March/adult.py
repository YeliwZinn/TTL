import cv2
dataset=cv2.CascadeClassifier('14_March\haarcascade_frontalface_default.xml')
img=cv2.imread('14_March\WhatsApp Image 2024-03-14 at 10.16.12_d23a47bc.jpeg')
cv2.imshow('family picture is here',img)
cv2.waitKey(1000)
gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
fc=dataset.detectMultiScale(gimg)

for i in range (0,len(fc)):
    x,y,w,h=fc[i]
    if (w>=27):
        cv2.rectangle(img,(x,y),(x+w,y+h),(i*5,255-i,i*10),2)
        cv2.imshow('Adults are',img)
        cv2.waitKey()
    else:
        cv2.rectangle(img,(x,y),(x+w,y+h),(i*5,255-i,i*10),2)
        cv2.imshow('Childs are',img)
        cv2.waitKey()