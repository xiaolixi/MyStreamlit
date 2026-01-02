import streamlit as st
import streamlit as st

st.set_option("client.toolbarMode", 'viewer')
# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': None
#     }
# )
print("========================--------------------")
# wrong example
# if "step" not in st.session_state:
#     st.session_state["step"] = 1
# if st.session_state.step == 1:
#     st.write("This is step 1 info")
#     if st.button(label="Go to next step"):
#         st.session_state["step"] = 2
#         print(1)
# elif st.session_state.step == 2:
#     st.write("This is step 2 info")
#     if st.button(label="Go to prev step"):
#         st.session_state["step"] = 1
#         print(2)



# # correct version
if "step" not in st.session_state:
    st.session_state["step"] = 1


def goto_step(step_num: int):
    st.session_state["step"] = step_num
    print(step_num)
    # st.write(text)


if st.session_state.step == 1:
    st.title("Step 1 page")
    st.button(label="Go to next step", on_click=goto_step, args=(2,))
    
    print('Step 1 page')


if st.session_state.step == 2:
    st.title("Step 2 page")
    st.button(label="Go to prev step", on_click=goto_step, args=(1,))
    print('Step 2 page')











