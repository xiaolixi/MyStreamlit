import streamlit as st
import numpy as np
import time

st.write("## st.columns相当于HLayout")

with st.echo():
    vertical_alignment = st.selectbox(
        "Vertical alignment", ["top", "center", "bottom"], index=2
    )

    left, middle, right = st.columns(3, vertical_alignment=vertical_alignment,border=True)
    left.image("https://static.streamlit.io/examples/cat.jpg")
    middle.image("https://static.streamlit.io/examples/dog.jpg")
    right.image("https://static.streamlit.io/examples/owl.jpg")




st.write("## st.container相当于VLayout")
with st.echo():
    with st.container(border=True):
        st.write("This is inside the container")

        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))

    st.write("This is outside the container")




st.write("## st.dialog ")
with st.echo():
    @st.dialog("Cast your vote")
    def vote(item):
        st.write(f"Why is {item} your favorite?")
        reason = st.text_input("Because...")
        if st.button("Submit"):
            st.session_state.vote = {"item": item, "reason": reason}
            st.rerun()

    if "vote" not in st.session_state:
        st.write("Vote for your favorite")
        if st.button("A"):
            vote("A")
        if st.button("B"):
            vote("B")
    else:
        f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"



st.write("## st.empty 空的单一元素的容器，但是可以在它里面用 container ")
@st.fragment()
def use_empty():
    if st.button("show empty"):    
        with st.echo():
            placeholder = st.empty()
            placeholder.markdown("Hello")
            time.sleep(1)

            placeholder.progress(0, "Wait for it...")
            time.sleep(1)
            placeholder.progress(50, "Wait for it...")
            time.sleep(1)
            placeholder.progress(100, "Wait for it...")
            time.sleep(1)

            with placeholder.container():
                st.line_chart({"data": [1, 5, 2, 6]})
                time.sleep(1)
                st.markdown("3...")
                time.sleep(1)
                st.markdown("2...")
                time.sleep(1)
                st.markdown("1...")
                time.sleep(1)

            placeholder.markdown("Poof!")
            time.sleep(1)

            placeholder.empty()
use_empty()



st.write("## st.expander 可以折叠的多元素的容器")
with st.echo():
    with st.expander("See explanation"):
        st.write('''
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        ''')
        st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

st.divider()





with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)


with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")

st.write("Your name:", name)


left, middle, right = st.columns(3)

left.space("medium")
left.button("Left button", width="stretch")

middle.space("small")
middle.text_input("Middle input")

right.audio_input("Right uploader")


tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
