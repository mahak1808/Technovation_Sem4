import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://faceattendancerealtime-19c9e-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "180802":
        {
            "name": "Mahak Kaur Chhabra",
            "major": "BTech (CSE)",
            "total_attendance": 36,
            "year": 2,
            "last_attendance_time": "2023-04-26 08:54:34"
        },
    "160100":
        {
            "name": "Meet Singh Chhabra",
            "major": "BCom",
            "total_attendance": 28,
            "year": 4,
            "last_attendance_time": "2023-04-26 08:54:34"
        },
    "271201":
        {
            "name": "Lokansh Nama",
            "major": "BTech",
            "total_attendance": 30,
            "year": 2,
            "last_attendance_time": "2023-04-26 08:54:34"
        },
    "123456":
        {
            "name": "Manish Tiwari",
            "major": "BTech",
            "total_attendance": 30,
            "year": 2,
            "last_attendance_time": "2023-04-26 08:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)