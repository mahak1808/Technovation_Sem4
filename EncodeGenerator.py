# To generate all the 128 encodings for each face
import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://faceattendancerealtime-19c9e-default-rtdb.firebaseio.com/",
    "storageBucket": "faceattendancerealtime-19c9e.appspot.com"
})

# importing all the kids' images into a list
folderPath = "Images"
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = os.path.join(folderPath, path)
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    # print(path)
    # print(os.path.splitext(path)[0])   Splitting and getting the 1st element
print(studentIds)  # To check if images have been imported

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
# print(encodeListKnown)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

# generating pickle file
file = open("EncodeFile.p",'wb')  # name and permissions
# dump lists in this file
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
