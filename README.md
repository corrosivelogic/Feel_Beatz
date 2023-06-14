# Feel_Beatz
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://corrosivelogic-feel-beatz-home-xgi8v2.streamlit.app/)

Project Submission for Nebula|MDG

## About

Feal_Beatz is a music app which recommends and plays musics based on your emotions.The app captures emotions from audio and video and suggests you a playlist catered to your emotions.

The uncopy-righted music is provided by NCS Music Library.

## Face_Emotion Detection
 
The app utilizes a CNN model to categorize facial emotion into seven categories namely : Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise

The dataset used for the model: https://www.kaggle.com/jonathanoheix/face-expression-recognition-dataset

## Speech Emotion Detection

The app utilizes an LSTM model to categorize speech emotion into seven categories namely : Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise

The dataset used for the model: https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess

## App Deployment 

The App has been deployed on the streamlit community servers and can be accessed on the following url : https://corrosivelogic-feel-beatz-home-xgi8v2.streamlit.app/ 

## Problems Encountered 

Several Problems were encountered with the streamlit library as it's a relatively new library and some features are still having bugs . Major problem occured when the streamlit_webrtc component does not allow variable values to be trasferred out of the event loop thus a seperate picture capture had to be setup. 

## Future Scope

1. To develop a  UserAnalytics feature that can graphically show the users the change in moods overa a period of time and songs prefferd.
2. To develop a classifier to self classify songs emotions.
3. Add a recommendation feature to recommend songs based on past songs, moods and include Topic Modelling.
