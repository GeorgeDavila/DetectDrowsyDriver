#Algorithm to calculate Eye Aspect Ratio Stats of User 
#aka it runs for a while to see what a persons average eye aspect ratio is. 
#This prevents people with naturally slimmer eyes from setting off the alarm unduly often 

#streamlit_drowsiness

'''This script detects if a person is drowsy or not,using dlib and eye aspect ratio
calculations. Uses webcam video feed as input.'''

#Import necessary libraries
import streamlit as st 
from scipy.spatial import distance
from imutils import face_utils
import numpy as np
import time
import dlib
import cv2
import pandas as pd 

st.title('Eye Aspect Ratio Statistics')

numberOfDatapointsToCollect = 500 #Number of times to collect data about users eyes, only if it sees their eyes 

#Minimum threshold of eye aspect ratio below which alarm is triggerd
EYE_ASPECT_RATIO_THRESHOLD = 0.3

#Load face cascade which will be used to draw a rectangle around detected faces.
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

#This function calculates and return eye aspect ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])  
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])

    ear = (A+B) / (2*C)
    return ear

#Load face detector and predictor, uses dlib shape predictor file
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

#Extract indexes of facial landmarks for the left and right eye
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

#Start webcam video capture
cap = cv2.VideoCapture(0)
FRAME_WINDOW = st.image([])
#Give some time for camera to initialize(not required)
time.sleep(2)

#build lists for stats
leftEyeAspectRatioLIST = []
rightEyeAspectRatioLIST = []
avgBothEyeAspectRatioLIST = []

index_count = 0 
#Streamlit columns to write out findings 
'''col1, col2, col3, col4 = st.beta_columns(4)
col1.header("index")
col2.header("Averaged Eye Aspect Ratio (both eyes averaged)")
col3.header("Left Eye Aspect Ratio")
col4.header("Right Eye Aspect Ratio")

^leave that here and put foloowing at end of the for faces in faces loop to get data columns 
col1.write( str(index_count) ) #start writing  at index_count = 1
    col2.write( str( eyeAspectRatio ) )

    col3.write( str( leftEyeAspectRatio ) )
    col4.write( str( rightEyeAspectRatio ) )
'''

while(True):
    #Read each frame and flip it, and convert to grayscale
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    #FRAME_WINDOW.image(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect facial points through detector function
    faces = detector(gray, 0)

    #Detect faces through haarcascade_frontalface_default.xml
    face_rectangle = face_cascade.detectMultiScale(gray, 1.3, 5)

    #Draw rectangle around each face detected
    for (x,y,w,h) in face_rectangle:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    #Detect facial points
    for face in faces:

        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        #Get array of coordinates of leftEye and rightEye
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        #Calculate aspect ratio of both eyes
        leftEyeAspectRatio = eye_aspect_ratio(leftEye)
        rightEyeAspectRatio = eye_aspect_ratio(rightEye)

        eyeAspectRatio = (leftEyeAspectRatio + rightEyeAspectRatio) / 2 #average eye aspect ratio
        
        #Use hull to remove convex contour discrepencies and draw eye shape around eyes
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)


        leftEyeAspectRatioLIST.append(leftEyeAspectRatio)
        rightEyeAspectRatioLIST.append(rightEyeAspectRatio)
        avgBothEyeAspectRatioLIST.append(eyeAspectRatio)


        index_count += 1

    #Show video feed
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Convert back to standard RGB
    cv2.putText(frame, "index_count = " + str(index_count), (150,200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 2)    
    #cv2.imshow('Video', frame)
    FRAME_WINDOW.image(frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

    if index_count == numberOfDatapointsToCollect:
        break 

st.write( "Number of datapoints collected = " + str(len(avgBothEyeAspectRatioLIST)) )

#Construct pandas dataframe from dictionary  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
d = {'Both Eyes': avgBothEyeAspectRatioLIST, 'Left Eye': leftEyeAspectRatioLIST , 'Right Eye': rightEyeAspectRatioLIST} 
df = pd.DataFrame(data=d)
#st.write takes dataframes automatically, so just enter it straight into st.write 
st.write(df)

st.write( "LEFT eye aspect ratio average = ", np.mean(leftEyeAspectRatioLIST) )
st.write( "RIGHT eye aspect ratio average = ", np.mean(rightEyeAspectRatioLIST) )
st.write( "BOTH eye aspect ratio average = ", np.mean(avgBothEyeAspectRatioLIST) )

st.write( "LEFT eye aspect ratio standard deviation = ", np.std(leftEyeAspectRatioLIST) )
st.write( "RIGHT eye aspect ratio standard deviation = ", np.std(rightEyeAspectRatioLIST) )
st.write( "BOTH eye aspect ratio standard deviation = ", np.std(avgBothEyeAspectRatioLIST) )


#Finally when video capture is over, release the video capture and destroyAllWindows
cap.release()
cv2.destroyAllWindows()

print( "LEFT eye aspect ratio average = ", np.mean(leftEyeAspectRatioLIST) )
print( "RIGHT eye aspect ratio average = ", np.mean(rightEyeAspectRatioLIST) )
print( "BOTH eye aspect ratio average = ", np.mean(avgBothEyeAspectRatioLIST) )