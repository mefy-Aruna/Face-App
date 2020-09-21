# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:12:04 2020

@author: Aruna
"""
        
import psutil
import face_recognition
import cv2
import csv
import pandas as pd

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
    # file_name_path = './' + 'loginUser' + '.png'
    # cv2.imwrite(file_name_path, frame)
    # login_user= face_recognition.load_image_file("loginUser.png")

vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows()  

unknown=[]


###############USING FACE ENCODINGS#########################
##checks if user matches to any database existing and gives true of false
face_encoding_to_check=face_recognition.face_encodings(frame)[0]
df1 = pd.DataFrame(face_encoding_to_check, columns=["colummn"])
df1.to_csv('login'+'.csv', index=False)
#print([face_encoding_to_check])

#users=['user1.png','user2.png','user3.png','user4.png']
#print("login encodings",face_encoding_to_check)
users=[]

sizeOfUserDatabase=9######dynamic and received from app database
for i in range(1,sizeOfUserDatabase+1):
    user='./user'+str(i)+'.csv'
    users.append(user)
    #print("users",user
#print("users",users)
count=0


#######user database size will be updated automatically as registraion happens on app


for user in users:
    count=count+1
    #face_encoding_to_check=face_recognition.face_encodings(login_user)[0]
    # with open("registered_user"+str(count)+".csv", "r") as csv_file:
    # with open("registered_user1.csv", "r") as csv_file:
    
    #     csv_reader = csv.reader(csv_file)
    # for lines in csv_reader:
    #   print(lines[0])
    
    
    ##################READ CSV FILE FOR REGISTERED USER ENCODINGS##########################
    col_list = ["colummn"]
    usercsv=pd.read_csv(user, usecols=col_list)
    userEncodings = usercsv.colummn.tolist()

    logincsv=pd.read_csv('login.csv', usecols=col_list)
    unknown.append(usercsv)
    loginEncodings = logincsv.colummn.tolist()
    #print(len(loginEncodings))
    # print("login encodings:      ")   
    # print("              ",loginEncodings)
    # print("              ")
    # print("user encodings"+str(count)+":      ")   
    # print("              ",userEncodings)
    # print("              ")

    #print("unknown list",unknown)
    # with open(user, newline='') as f:
    #       reader = csv.reader(f)
    #       data = list(reader)

    #print(reader)
    #print(logincsv)
    # print(usercsv)
    ###reshape the file 

    
#     known_face_encodings = 
    
    
    decision=face_recognition.compare_faces([userEncodings], face_encoding_to_check,tolerance=0.35)
    
#     if decision==[True]:
#         eligible=user
#         img=cv2.imread('./'+eligible)
# ####Displaying user registered Face Id
#     #     cv2.imshow('user logged in',login_user)
#     #     cv2.imshow('registered user face ID',img)             
    print("Same?",decision)
    
    ##################   IF NO MATCH, DENY LOGIN         #################
#     # encoded=open('encoded.txt','w')
#     # encoded.write(str(databaseEncodings))
#     # encoded.close()
        
# ###############USING EUCLIDEAN DISTANCE CHECK COMPARISON WITH SIMILARITY MEASURE############
# ###for 2 or more faces detected and matched in database, check which has closer match to its resp.matching face

# eucli_dist=face_recognition.api.face_distance(face_encoding_to_check,databaseEncodings)
# print("distance=",eucli_dist)
# print("match found")



