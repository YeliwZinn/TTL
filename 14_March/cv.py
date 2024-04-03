import cv2

face_cascade = cv2.CascadeClassifier('14_March/haarcascade_frontalface_default.xml')

img = cv2.imread('14_March\WhatsApp Image 2024-03-14 at 09.41.19_67ca0a5a.jpeg')

resz = cv2.resize(img, (900, 500))

cv2.imshow("Anime Picture", resz)
cv2.waitKey(0)
cv2.destroyAllWindows()

grayimg = cv2.cvtColor(resz, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grayimg, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(resz, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow("Detected", resz)
cv2.waitKey(0)
cv2.destroyAllWindows()
