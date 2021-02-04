import cv2
import pickle
import face_recognition
import numpy as np
from flask import Flask,jsonify
from flask_restful import Api,Resource
from PIL import Image, ImageDraw
import os
import os.path
import time
model_list = []

def getFileName(model_dir):
    for class_dir in os.listdir(model_dir):
        model_list.append(class_dir)
    print(model_list)




def predict(X_frame, knn_clf=None, model_path=None, distance_threshold=0.4):
    if knn_clf is None and model_path is None:
        raise Exception("Must supply knn classifier either thourgh knn_clf or model_path")

    # Load a trained KNN model (if one was passed in)
    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)

    X_face_locations = face_recognition.face_locations(X_frame)

    # If no faces are found in the image, return an empty result.
    if len(X_face_locations) == 0:
        return []

    # Find encodings for faces in the test image
    faces_encodings = face_recognition.face_encodings(X_frame, known_face_locations=X_face_locations)

    # Use the KNN model to find the best matches for the test face
    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_face_locations))]
    
    # Predict classes and remove classifications that aren't within the threshold
    return [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches)]




app=Flask(__name__)
api=Api(app)
class Predict(Resource):

    def get(self,url):
        start=time.time()
        count=0
        fail=0
        a=len(os.listdir("models"))
        print(url)
        if(url=="0"):
            urll=int(url)
        else:
            urll = "rtsp://"+url+"/stream"
        getFileName("models")
        process_this_frame = 0
        cap = cv2.VideoCapture(urll)
        while 1 > 0:
            
            ret, frame = cap.read()
            if ret:
                # Different resizing options can be chosen based on desired program runtime.
                # Image resizing for more stable streaming

                process_this_frame = process_this_frame + 1
                if process_this_frame % 1 == 0:
                    predictions = predict(frame, model_path="models/"+model_list[count])
                    try:
                        print(predictions[0][0])
                        if predictions[0][0] == "unknown" and fail<a:
                            count+=1
                            fail+=1
                            pass
                            #predictions = predict(frame, model_path="models/"+model_list[count])
                        if predictions[0][0] != "unknown":
                            
                            return jsonify(predictions[0][0])
                        if fail>=a:
                            return jsonify("unknown")
                    except(IndexError):
                        count = 0
                        print("No face")
                        fail=0

                    except:
                        print("Error")
                        pass
                end=time.time()
                print(str(end-start))
        
api.add_resource(Predict,"/predict/<string:url>")

if __name__ == "__main__":
    app.run(port=7777,debug=True)
    




