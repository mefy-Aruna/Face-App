# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:50:14 2020

@author: Aruna
"""
import face_recognition
import cv2
###############This code saves face encodings at the time of registration########################

####Capture button on UI where q takes the picture of user
vid = cv2.VideoCapture(0) 
count=1 #########Count to store user faceID received from app 
  
while(True): 
      
    # Capture the video frame by frame 
    ret, frame = vid.read() 
    #cv2.putText(vid, "Please click on capture", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
    cv2.putText(frame,'please click on capture', (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)

    # Display the resulting frame 
    cv2.imshow('Capture Frame', frame) 
      
    #'q' button is set as the quitting button----can be replaced by capture button on UI
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
# After the loop, save the login pic for authorisation step
#####But to save storage space, directly encode face from frame obtained

    #file_name_path = './' + 'User' + str(count)+'.png'
    #cv2.imwrite(file_name_path, frame) #delete after face encoded
    #User= face_recognition.load_image_file(file_name_path)

vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows()  
database_face_encoding=face_recognition.face_encodings(frame)[0]

# face_encoding_to_check=face_recognition.face_encodings(User)
encoded=open('encoded_user'+str(count)+'.txt','w')
encoded.write(str(database_face_encoding))
encoded.close()
# encoded=open('encoded_user'+str(count)+'.txt','r')
# print(encoded.read())
# encoded.close()
