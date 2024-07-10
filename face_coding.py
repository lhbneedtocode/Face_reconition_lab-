import face_recognition
import json
import os
import cv2
import numpy as np
# 图片所在的文件夹路径
image_folder = './编码/'

def to_encoding():
    # 读取人名文件
    with open('./编码/name.txt', 'r') as f:
        names = [line.strip() for line in f]

    # 存储所有特征编码的字典
    all_face_encodings = {}

    # 遍历每个人名
    for name in names:
        # 图片文件名
        filename = f"{name}.jpg"
        image_path = os.path.join(image_folder, filename)

        # 检查图片文件是否存在
        if not os.path.exists(image_path):
            print(f"File {filename} not found.")
            continue

        # 载入图片
        image = face_recognition.load_image_file(image_path)

        # 获取人脸特征编码
        face_encodings = face_recognition.face_encodings(image)
        print(face_encodings[0])
        # 假设每张图片中只有一个人脸
        if face_encodings:
            face_encoding = face_encodings[0]
            all_face_encodings[name] = face_encoding.tolist()
        else:
            print(f"No face found in {filename}")
    #faceall = coding[0]
    #all_face_encodings[log_name] = faceall.tolist()
    # 保存所有特征编码到JSON文件
    with open('./编码/all_face_encodings.json', 'w') as f:
        json.dump(all_face_encodings, f)
    os.startfile('./编码/all_face_encodings.json')

def download_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        # Perform face recognition
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)

        # Draw rectangles around faces
        if face_locations:
            face_encodin = face_recognition.face_encodings(frame, known_face_locations=face_locations)
            #print(face_encodings)
    return face_encodin
#download_image()
#to_encoding()