import streamlit as st
from audio_recorder_streamlit import audio_recorder
import pandas as pd 
import numpy as np
from keras.models import load_model
import librosa

labels =["Angry","Disgust","Fear","Happy","Neutral","Surprise","Sad"]
def extract_mfcc(filename):
    y, sr = librosa.load(filename,duration=3,offset=0.5)
    mfcc = np.mean(librosa.feature.mfcc(y=y,sr=sr,n_mfcc=40).T,axis=0)
    return mfcc

df=pd.read_csv('songs.csv')
classifier =load_model('./speech_emote.h5')
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

col1, padding, col2 = st.columns((10,2,10))
with col1:
    audio = audio_recorder(text="",icon_size="6x",)
    st.caption("Click to Record")
    if audio:
        st.audio(audio, format="audio/wav")
        # To save audio to a file:
        wav_file = open("audio.mp3", "wb")
        wav_file.write(audio)
        x=extract_mfcc("audio.mp3")
        x=np.array(x)
        x=np.expand_dims(x,-1)
        prediction = classifier.predict(x)
        output=np.sum(prediction,axis=0)
        label=labels[prediction.argmax()]
        st.write(f" ### {label}",unsafe_allow_html=True)

        indx=[]
        for i in range (49):
            if df.emotion[i] == label:
                indx.append(i)
        for i in range(7):
            with col2:
                path="./Music/"+df.code[indx[i]]+".mp3"
                st.write(f'<p style="text-align:center">{df.name[indx[i]]}</p>',unsafe_allow_html=True)
                st.audio(path)
        



