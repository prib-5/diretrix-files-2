import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime

video_capture=cv2.VideoCapture(0)

sagnik_image=face_recognition.load_image_file("photos/sagnik.jpeg")
sagnik_encoding=face_recognition.face_encodings(sagnik.image)[0]
 
arna_image=face_recognition.load_image_file("photos/arna.jpeg")
arna_encoding=face_recognition.face_encodings(arna.image)[0]

saptarshi_image=face_recognition.load_image_file("photos/saptarshi.jpeg")
saptarshi_encoding=face_recognition.face_encodings(saptarshi.image)[0]

riddhi_image=face_recognition.load_image_file("photos/riddhi.jpeg")
riddhi_encoding=face_recognition.face_encodings(riddhi.image)[0]

rohan_image=face_recognition.load_image_file("photos/rohan.jpeg")
rohan_encoding=face_recognition.face_encodings(rohan.image)[0]

debajyoti_image=face_recognition.load_image_file("photos/debajyoti.jpeg")
debajyoti_encoding=face_recognition.face_encodings(debajyoti.image)[0]

known_face_encoding=[
sagnik_encoding,
arna_encoding,
saptarshi_encoding,
riddhi_encoding,
rohan_encoding,
debajyoti_encoding
]

known_faces_names=[
"sagnik",
"arna",
"saptarshi",
"riddhi",
"rohan",
"debajyoti"
]

students=known_faces_names.copy()

face_locations=[]
face_encodings=[]
face_names=[]
s=True


now=datetime.now()
current_date=now.sttrftime("%Y-%m-%d")


f=open(current_date+'.csv','w+',newLine='')
lnwriter=csv.writer(f)



while True:
    _,frame=video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=small_frame[:,:,::-1]
    if s:
        face_locations=face_recognition.face_locations(rgb_small_frame)
        face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names=[]
        for face_encoding in face_encodings:
            matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance=face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index=np.argmin(face_distance)
            if matches[best_match_index]:
                name=known_faces_names[best_match_index]

                face_names.append(name)
                if name in known_faces_names:
                    if name in students:
                        students.remove(name)
                        print(students)
                        current_time=now.strftime("%H-%M-%S")
                        lnwriter.writerow([name,current_time])
    cv2.imshow("attendance system",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
