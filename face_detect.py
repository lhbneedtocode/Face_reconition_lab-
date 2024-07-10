import sys
import cv2
import numpy as np
import face_recognition
import json

library_name=[]
library_encoding=[]
file=".//编码//all_face_encodings.json"

with open(file, 'r') as f:
    face_encoding_list = json.load(f)


def load_image(image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    return encodings


def compare_faces(image_encodings, local_encodings, tolerance=0.6, max_matches=1):
    matches = []
    for image_encoding in image_encodings:
        distances = face_recognition.face_distance(list(local_encodings.values()), image_encoding)
        sorted_indices = np.argsort(distances)
        for index in sorted_indices:
            if distances[index] <= tolerance:
                matches.append(list(local_encodings.keys())[index])
                if len(matches) >= max_matches:
                    break
    return matches


def check(face_encodings):
    # Load local encodings
    local_encodings = face_encoding_list

    # Load image and get encodings

    # Compare faces
    matches = compare_faces(face_encodings, local_encodings)

    # Print results
    if matches:
        pass
        #print(f"Matches found: {', '.join(matches)}")
    else:
        pass
        #print("No matches found.")
    return matches