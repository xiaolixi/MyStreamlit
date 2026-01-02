import streamlit as st



st.write("## st.audio ")
@st.fragment()
def use_audio():
    # 也可以使用
    with st.echo():
        path_audio = st.text_input("输入路径", value="new_nag/春野.mp3")
        st.audio(path_audio, format="audio/mp3")
use_audio()

st.write("## st.image ")
with st.echo():
    st.image("https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80", 
             caption="Sunrise by the mountains")


st.write("## st.video ")

with st.echo():
    video_path = "https://static.streamlit.io/examples/star.mp4"
    st.video(video_path, format="video/mp4")










