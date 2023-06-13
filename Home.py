import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Feel-Beatz",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "### This is a emotion based music recommendation app"
    }
)


if 'page' not in st.session_state:
    st.session_state['page'] = 'home'
    

# Display the centered heading
st.markdown('<h1 class="centered-heading">Feal Beatz</h1>', unsafe_allow_html=True)

if st.session_state['page'] == 'home':
    st.markdown(
    """
    <style>
    .stButton>button {
        display: block;
        margin: 0 auto;
        padding: 12px 24px;
        font-size: 51px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        color: black;
        background-color: #ffffff;
        border-radius: 6px;
        transition: background-color 0.3s ease;
    }
    button:hover{
        background-color: #f5f5f5;
        color: #333333;
    }
    .centered-heading {
            text-align: center;
            margin-top: -100px;
            color: white;
            font-size: 100px;
    } 
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1468186402854-9a641fd7a7c4?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=900&ixid=MnwxfDB8MXxyYW5kb218MHx8bmlnaHR8fHx8fHwxNjg2NDY5Mzk2&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1600");
        background-size:cover;
    }
    .css-18ni7ap{
        background: rgba(0,0,0,0);
    }

    [data-testid="stToolbar"]{{
        right:2rem;
    }}

    </style>
    """,
    unsafe_allow_html=True
)
    col1, col2, col3 = st.columns(3)
    image = Image.open("logo.png")
    with col2:
        st.image(image,use_column_width=True)
    if st.button("Play"):
        st.session_state['page'] = 'app'


        
elif st.session_state['page'] == 'app':
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
    st.write("##### Feel Beatz is a Music Recommender App which recoomends music to you based on your face and voice emotions. It Takes live video and audio input , detects emotion and suggests songs which you can listen to and enjoy songs that suit your mood.")
    st.write(" ")
    st.write("##### How to use:")
    st.write("##### 1.Go to SideBar")
    st.write("##### 2.Select Either of the 2 options")
    st.write("##### 3.For Face Emotion Detection Turn on webstream for live face emotion detection and click picture for recommendation")
    st.write("##### 4.For Speech Emotion Detection Record Audio for recommendation")
    st.write("##### 5.After Getting recommended you can play and listen to the songs recommended")
    st.divider()
    st.caption("All songs have been taken from NCS Music Library and are non copy-righted")
        
  
        








