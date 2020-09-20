# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:12:04 2020

@author: Aruna
"""
        
import psutil
import face_recognition
import cv2




############### FACE CAPTURE FOR LOGIN #################
# define a video capture object 

vid = cv2.VideoCapture(0) 
  
while(True): 
      
    # Capture the video frame by frame 
    ret, frame = vid.read() 
    # Display the resulting frame 
    cv2.imshow('frame', frame) 
      
    #'q' button is set as the quitting button----can be replaced by capture button on UI
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
# After the loop, save the login pic for authorisation step
    file_name_path = './' + 'loginUser' + '.png'
    cv2.imwrite(file_name_path, frame)
    login_user= face_recognition.load_image_file("loginUser.png")

vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows()  



###############USING FACE ENCODINGS#########################
##checks if user matches to any database existing and gives true of false
face_encoding_to_check=face_recognition.face_encodings(login_user)[0]
#users=['user1.png','user2.png','user3.png','user4.png']
users=[]
databaseEncodings=[]
count=1


#######user database size will be updated automatically as registraion happens on app

sizeOfUserDatabase= 4

for count in range(1,sizeOfUserDatabase+1):
    user='./user'+str(count)+'.png'
    users.append(user)
    #print("users",users)
    #print("user",user)


for user in users:
    #print(user)
    count=count+1
    database= face_recognition.load_image_file(user)
    face_encoding_to_check=face_recognition.face_encodings(login_user)[0]
    
    ########save encodings of user database in a seperate code and import when needed
    known_face_encodings=face_recognition.face_encodings(database)[0]
    print(known_face_encodings)
    databaseEncodings.append(known_face_encodings)
    ####is able to idenntify with specs also but better remove. Tolerance is set
    decision=face_recognition.compare_faces([known_face_encodings], face_encoding_to_check,tolerance=0.45)
    if decision==[True]:
        eligible=user
        img=cv2.imread('./'+eligible)
####Displaying user registered Face Id
        cv2.imshow('user logged in',login_user)
        cv2.imshow('registered user face ID',img)             
    print("Same?",decision)
    encoded=open('encoded.txt','w')
    encoded.write(str(databaseEncodings))
    encoded.close()
        
###############USING EUCLIDEAN DISTANCE CHECK COMPARISON WITH SIMILARITY MEASURE############
###for 2 or more faces detected and matched in database, check which has closer match to its resp.matching face

eucli_dist=face_recognition.api.face_distance(face_encoding_to_check,databaseEncodings)
print("distance=",eucli_dist)
print("match found")



