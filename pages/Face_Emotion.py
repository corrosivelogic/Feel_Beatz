import av
import cv2
from keras.models import load_model
import numpy as np
from keras.utils.image_utils import img_to_array
from streamlit_webrtc import webrtc_streamer
import streamlit as st
import pandas as pd 
from PIL import Image


df=pd.read_csv('songs.csv')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cascade2 = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
classifier =load_model('./model.h5')
st.markdown(
    """
    <style>
    .centered-heading {
            text-align: center;
            margin-top: -50px;
    } 

    </style>
    """,
    unsafe_allow_html=True)
st.markdown('<h1 class="centered-heading">Feal Beatz</h1>', unsafe_allow_html=True)
def video_frame_callback(frame):
        frm = frame.to_ndarray(format="bgr24")
        img_gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(img_gray)
        for x,y,w,h in faces:
            cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,255), 2)
            roi_gray = img_gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                prediction = classifier.predict(roi)[0]
                label=emotion_labels[prediction.argmax()]
                cv2.putText(frm,label,(x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        return av.VideoFrame.from_ndarray(frm, format='bgr24')

col1, padding, col2 = st.columns((10,2,10))
with col1:
    webrtc_streamer(key="key", video_frame_callback=video_frame_callback,media_stream_constraints={"video":True,"audio":False},rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})
    img_file_buffer = st.camera_input(" ")

    if img_file_buffer is not None:
        img=Image.open(img_file_buffer)
        img_array = np.array(img)
        gray = cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
        faces = cascade2.detectMultiScale(gray)
        for x,y,w,h in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                prediction = classifier.predict(roi)[0]
                label=emotion_labels[prediction.argmax()]
                st.write(f"#### {label}")
                
                indx=[]
                for i in range (49):
                    if df.emotion[i] == label:
                        indx.append(i)
                for i in range(7):
                    with col2:
                        path="./Music/"+df.code[indx[i]]+".mp3"
                        st.write(f'<p style="text-align:center">{df.name[indx[i]]}</p>',unsafe_allow_html=True)
                        st.audio(path)
                    
                         

