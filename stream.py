import streamlit as st
from PIL import Image
import pandas as pd
import time

st.title('신한울 1,2호기 분석결과')
option = st.sidebar.selectbox("옵션을 선택하세요.", ["Jet_ANIM", "Jet_XVID", "Reds_ANIM", "Reds_XVID", "Seismic_ANIM", "Seismic_XVID", "Rainbow_ANIM", "Rainbow_XVID", "Set2_ANIM", "Set2_XVID"])
df= pd.DataFrame({
    '노드번호':range(1,37),
    '노드설명':["Reactor Cavity & Reactor Vessel Annulus", "ICI Chase", "Corium Chamber Room",
                "Reactor Cavity Access Area", "Holdup Volume Tank","S/G#2 Compartment - EL.100'",
                "S/G#2 Compartment - EL.136.5'", "S/G#1 Compartment - EL.100'", "S/G#1 Compartment - EL.136.5'",
                "Annular Compartment #2 NW - EL.100'", "Annular Compartment #1 SW - EL.100'", "Annular Compartment #2 NW - EL.114'",
                "Annular Compartment #1 SW - EL.114'", "Annular Compartment #2 NW - EL.136.5'", "Annular Compartment #1 SW - EL.136.5'",
                "Refueling Pool", "Containment Dome - EL.254.5'", "Upper Containment #2",
                "Upper Containment #1", "Reactor Drain Tank Room", "Letdown Heat Exchanger Room",
                "Regenerative Heat Exchanger Room", "IRWST NE - Non Sparger", "Pressurizer Compartment",
                "Pressurizer Spray Valve Room & Letdown Line Valve Room", "IRWST NW - Sparger", "Upper Containment Dome - EL.291.5'",
                "IRWST SW - Sparger", "IRWST SE - Non Sparger", "Annular Compartment #4 NE - EL.100'",
                "Annular Compartment #3 SE - EL.100'", "Annular Compartment #2 NE - EL.114', ", "Annular Compartment #1 SE - EL.114'",
                "Annular Compartment #2 NE - EL.136.5'", "Annular Compartment #1 SE - EL.136.5'", "Upper Reactor Vessel Annulus"]
})
df.set_index("노드번호", inplace=True)
st.write(df)

progress_bar = st.sidebar.progress(0)
frame_text = st.sidebar.empty()
st.sidebar.button("Run")
placeholder=st.empty()
if option == "Jet_ANIM":
    placeholder=st.empty()
    for i in range(306):
        img=Image.open("Jet/fig_"+str(i)+".png")
        placeholder.image(img)
        time.sleep(0.1)
        progress_bar.progress(i/306)
        frame_text.text("Frame "+str(round(i*100/306))+" %")
        img.close()
if option == "Reds_ANIM":
    placeholder=st.empty()
    for i in range(306):
        img=Image.open("Reds/fig_"+str(i)+".png")
        placeholder.image(img)
        progress_bar.progress(i/306)
        frame_text.text("Frame "+str(round(i*100/306))+" %")
        img.close()
if option == "Seismic_ANIM":
    placeholder=st.empty()
    for i in range(306):
        img=Image.open("Seismic/fig_"+str(i)+".png")
        placeholder.image(img)
        time.sleep(0.1)
        progress_bar.progress(i/306)
        frame_text.text("Frame "+str(round(i*100/306))+" %")
        img.close()
if option == "Rainbow_ANIM":
    placeholder=st.empty()
    for i in range(306):
        img=Image.open("Rainbow/fig_"+str(i)+".png")
        placeholder.image(img)
        time.sleep(0.1)
        progress_bar.progress(i/306)
        frame_text.text("Frame "+str(round(i*100/306))+" %")
        img.close()
if option == "Set2_ANIM":
    placeholder=st.empty()
    for i in range(306):
        img=Image.open("Set2/fig_"+str(i)+".png")
        placeholder.image(img)
        time.sleep(0.1)
        progress_bar.progress(i/306)
        frame_text.text("Frame "+str(round(i*100/306))+" %")
        img.close()

if option == "Jet_XVID":
    video_file = open('Jet/Sum_XVID_FPS3_Jet.mp4', 'rb')
    st.video(video_file.read())
if option == "Reds_XVID":
    video_file = open('Reds/Sum_XVID_FPS3_Reds.mp4', 'rb')
    st.video(video_file.read())
if option == "Seismic_XVID":
    video_file = open('Seismic/Sum_XVID_FPS3_Seismic.mp4', 'rb')
    st.video(video_file.read())
if option == "Rainbow_XVID":
    video_file = open('Rainbow/Sum_XVID_FPS3_Rainbow.mp4', 'rb')
    st.video(video_file.read())
if option == "Set2_XVID":
    video_file = open('Set2/Sum_XVID_FPS3_Set2.mp4', 'rb')
    st.video(video_file.read())
