import streamlit as st
import datetime

st.logo('1.png', icon_image="2.png",
    link="https://streamlit.io/gallery")
st.sidebar.markdown("Hi!")



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


def date_change(*args):
    print(args)
@st.dialog("添加记录")
def addRecord():
    with st.form("my_form"):
        type_d = st.selectbox("类型", ['111', '222'])
        dt3 = datetime.datetime(2024, 12, 25, 14, 30, 45, 123456)  # 带微秒
        d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
        event_time = st.datetime_input(
            "时间", value="now")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit", on_click=date_change)

        if submitted:
            st.write("slider", d)


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
if st.button("添加", key='addRecord'):
    addRecord()



a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True, help='你好啊')
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)



import streamlit as st

st.json(
    {
        "foo": "bar",
        "stuff": [
            "stuff 1",
            "stuff 2",
            "stuff 3",
        ],
        "level1": {"level2": {"level3": {"a": "b"}}},
    },
    expanded=2,width=600
)
