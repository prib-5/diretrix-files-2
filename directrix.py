def camer();
input cv2
face@cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while True;
_, img=cap.read()
gray=cv2.cvtColor(img,cv2.COLOR_DGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,5,meanSize=(30,30),flags=cv2.cascade_scale_image)
for(x,y,w,h)infaces;
cv2.rectangle(img,(x,y),(x+w,y+h),(10,159,255),2)
cv2.imshow('web can check',img)
if cv2.waitKey(1) and 