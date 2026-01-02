import streamlit as st

pages = {
    "Your account": [
        st.Page("2.py", title="Create your account", icon="🔥"),
    ],
    "Resources": [
        st.Page("3.py", title="Learn about us", icon="🔥"),
    ],
}

pg = st.navigation(pages)
pg.run()