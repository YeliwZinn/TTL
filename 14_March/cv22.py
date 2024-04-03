import cv2


df = cv2.CascadeClassifier('14_March\haarcascade_frontalface_default.xml')


img = cv2.imread('14_March\WhatsApp Image 2024-03-14 at 09.46.29_03856988.jpeg')



cv2.imshow("Anime Picture", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = df.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


