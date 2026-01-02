import streamlit as st
import time
st.logo('new_nag/1.png', icon_image="new_nag/2.png",
    link="https://streamlit.io/")
st.write("## st.success ")
with st.echo():
    st.success('This is a success message!', icon="✅")
st.divider()


st.write("## st.info")
with st.echo():
    st.info('This is a info', icon="⚠️")
st.divider()

st.write("## st.warning")
with st.echo():
    st.warning('This is a warning', icon="⚠️")
st.divider()

st.write("## st.error")
with st.echo():
    st.error('This is a error', icon="⚠️")
st.divider()

st.write("## st.error")

with st.echo():
    e = RuntimeError("This is an exception of type RuntimeError")
    st.exception(e)

st.divider()

@st.fragment()
def use_progress():
    with st.echo():
        if st.button("show progress", key="progress11"):
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text + f" {percent_complete}%")
            time.sleep(1)
            my_bar.empty()

        # st.rerun()

st.markdown("## st.progress")
use_progress()
st.divider()

@st.fragment()
def use_spinner():
    with st.echo():
        if st.button("show spinner", key="spinner22"):
            with st.spinner("Wait for it...", show_time=True):
                time.sleep(5)
                st.success("Done!")

st.markdown("## st.spinner")
use_spinner()
st.divider()


st.toast("Your edited image was saved!", icon="😍")


with st.echo():
    def cook_breakfast():
        msg = st.toast("Gathering ingredients...", icon="😍")
        time.sleep(1)
        msg.toast("Cooking...", icon="😍")
        time.sleep(5)
        msg.toast("Ready!!!!!!!!!!!!!!!!!!!!! not show. becase timeout.", icon="🥞")

@st.fragment()
def use_toast():
    if st.button("Cook breakfast"):
        cook_breakfast()

st.markdown("## st.toast")
use_toast()
st.divider()

@st.fragment()
def stats():
    if st.button("show status with expanded"):
        with st.status("Downloading data...", expanded=True) as status:
            st.write("Searching for data...")
            time.sleep(2)
            st.write("Found URL.")
            time.sleep(1)
            st.write("Downloading data...")
            time.sleep(1)
            status.update(
                label="Download complete!", state="complete", expanded=False
            )

        

st.markdown("## st.status")
stats()
st.divider()

@st.fragment()
def use_ballons():
    with st.echo():
        if st.button("show balloons"):
            st.balloons()

st.markdown("## balloons")
use_ballons()
st.divider()


@st.fragment()
def use_snow():
    with st.echo():
        if st.button("show snow"):
            st.snow()

st.markdown("## snow")
use_snow()
st.divider()

