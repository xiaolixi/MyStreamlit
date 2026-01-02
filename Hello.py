import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")
st.logo('new_nag/1.png', icon_image="new_nag/2.png",
    link="https://streamlit.io/gallery")
st.sidebar.markdown("Hi!")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

print(st.session_state)
print(type(st.session_state))

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")
st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)
st.divider()  # 👈 Draws a horizontal rule

st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
st.divider()  # 👈 Draws a horizontal rule


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")
st.divider()  # 👈 Draws a horizontal rule


with st.echo():
    st.write('This code will be printed')

st.divider()  # 👈 Draws a horizontal rule


def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

st.divider()
