import streamlit as st
import datetime
import pandas as pd
import numpy as np

# 为了让st.data_editor有示例数据
df = pd.DataFrame(np.random.randn(3, 3), columns=["a", "b", "c"])

st.title("📦 Streamlit Input Widgets 官方分类演示")

# ===================== 按钮类元素 =====================
st.write("## 🔘 按钮类元素 (Button elements)")

# Button
st.write("#### st.button")
with st.echo():
    if st.button("点我一下",icon="😃", width="stretch", type="primary"):
        st.success("按钮被点击了！")
st.divider()

# Download button
st.write("#### st.download_button")
with st.echo():
    sample_data = "这是一段示例文本，用于演示下载。"
    st.download_button(
        "下载文本文件",
        data=sample_data,
        file_name="example.txt",
        mime="text/plain",icon="😃", width="stretch", type="primary")

st.divider()

# Form button
st.write("#### st.form_submit_button")
with st.echo():
    with st.form("signup_form"):
        st.write("**注册表单**")
        email = st.text_input("邮箱")
        submitted = st.form_submit_button("提交注册",icon="😃", width="stretch", type="primary")
        if submitted:
            st.write(f"感谢注册！邮箱：{email}")

st.divider()

# Link button
st.write("#### st.link_button")
with st.echo():
    st.link_button("前往 Streamlit 官网", "https://streamlit.io",icon="😃", width="stretch", type="primary")

st.divider()

# Page link (多页面应用)
st.write("#### st.page_link")
with st.echo():
    # 假设这是多页面应用
    st.page_link("Hello.py", label="主页", icon="🏠")
    st.page_link("pages/6_🍕_media.py", label="仪表板", icon="📊")

# ===================== 选择类元素 =====================
st.divider()
st.write("## ✅ 选择类元素 (Selection elements)")

# Checkbox
st.write("#### st.checkbox")
with st.echo():
    agree = st.checkbox("我同意服务条款")
    if agree:
        st.write("✅ 您已同意")

st.divider()

# Color picker
st.write("#### st.color_picker")
with st.echo():
    color = st.color_picker("选择一个颜色", "#00FFAA")
    st.write(f"选中的颜色值：{color}")

st.divider()

# Feedback (新功能)
st.write("#### st.feedback")
with st.echo():
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

st.divider()

# Multiselect
st.write("#### st.multiselect")
with st.echo():
    options = st.multiselect(
        "选择你喜欢的水果",
        ["苹果", "香蕉", "橙子", "葡萄", "草莓"],
        default=["苹果", "香蕉"]
    )
    st.write(f"你的选择：{options}")

st.divider()

# Pills (新组件)
st.write("#### st.pills")
with st.echo():
    tag = st.pills("选择文章标签", ["科技", "体育", "财经", "娱乐", "健康"])
    if tag:
        st.write(f"你选择的标签：{tag}")

st.divider()

# Radio
st.write("#### st.radio")
with st.echo():
    choice = st.radio("选择一个宠物", ["猫", "狗", "兔子"], index=0)
    st.write(f"你更喜欢：{choice}")

st.divider()

# Segmented control (新组件)
st.write("#### st.segmented_control")
with st.echo():
    status_filter = st.segmented_control(
        "筛选状态",
        ["全部", "进行中", "已完成", "已取消"],
        default="全部"
    )
    st.write(f"当前筛选：{status_filter}")

st.divider()

# Select slider
st.write("#### st.select_slider")
with st.echo():
    size = st.select_slider("选择T恤尺码", ["XS", "S", "M", "L", "XL"])
    st.write(f"你的尺码：{size}")

st.divider()

# Selectbox
st.write("#### st.selectbox")
with st.echo():
    country = st.selectbox(
        "选择国家",
        ["中国", "美国", "日本", "德国", "法国"],
        index=0
    )
    st.write(f"选择的国家：{country}")

st.divider()

# Toggle
st.write("#### st.toggle")
with st.echo():
    dark_mode = st.toggle("启用深色模式")
    st.write(f"深色模式：{'开启' if dark_mode else '关闭'}")

st.divider()

# ===================== 数字输入元素 =====================
st.write("## 🔢 数字输入元素 (Numeric input elements)")

# Number input
st.write("#### st.number_input")
with st.echo():
    quantity = st.number_input("输入数量", min_value=0, max_value=100, value=1)
    st.write(f"数量：{quantity}")

st.divider()

# Slider
st.write("#### st.slider")
with st.echo():
    age = st.slider("选择年龄", 0, 100, 25)
    st.write(f"年龄：{age} 岁")

st.divider()

# ===================== 日期时间输入元素 =====================
st.write("## 📅 日期时间输入元素 (Date and time input elements)")

# Date input
st.write("#### st.date_input")
with st.echo():
    birthday = st.date_input("选择生日", datetime.date(1990, 1, 1))
    st.write(f"生日：{birthday}")

# Datetime input (新组件)
st.write("#### st.datetime_input")
with st.echo():
    event_time = st.datetime_input(
        "安排会议时间",
        datetime.datetime(2025, 1, 1, 9, 0)
    )
    st.write(f"会议时间：{event_time}")

# Time input
st.write("#### st.time_input")
with st.echo():
    meeting = st.time_input("会议时间", datetime.time(14, 30))
    st.write(f"会议时间：{meeting}")

# ===================== 文本输入元素 =====================
st.write("## 📝 文本输入元素 (Text input elements)")

# Text input
st.write("#### st.text_input")
with st.echo():
    name = st.text_input("请输入姓名", "张三")
    st.write(f"你好，{name}！")

# Text area
st.write("#### st.text_area")
with st.echo():
    message = st.text_area("留言板", "在这里输入你的留言...", height=100)
    if message:
        st.write("你的留言：", message)

st.divider()

# Chat input (新组件)
st.write("#### st.chat_input")
with st.echo():
    prompt = st.chat_input("说点什么吧...")
    if prompt:
        st.write(f"用户说：{prompt}")

st.divider()

# ===================== 其他输入元素 =====================
st.write("## 🎛️ 其他输入元素 (Other input elements)")

# Audio input
st.write("#### st.audio_input")
with st.echo():
    audio = st.audio_input("录制语音消息")
    if audio:
        st.audio(audio)

st.divider()

# Data editor
st.write("#### st.data_editor")
with st.echo():
    edited_df = st.data_editor(df, num_rows="dynamic")
    st.write("编辑后的数据：")
    st.write(edited_df)

st.divider()

# File uploader
st.write("#### st.file_uploader")
with st.echo():
    uploaded_file = st.file_uploader("上传文件", type=["txt", "csv", "png"])
    if uploaded_file:
        st.write(f"已上传文件：{uploaded_file.name}")

st.divider()

# Camera input
st.write("#### st.camera_input")
with st.echo():
    camera_img = st.camera_input("拍照")
    if camera_img:
        st.image(camera_img, caption="你的照片", width=300)

st.divider()

# ===================== 第三方组件 =====================
st.write("## 🧩 第三方组件 (Third-party components)")
st.info("以下为社区开发的流行第三方组件，需要单独安装。")

# Streamlit Elements 示例
st.write("#### Streamlit Elements")
with st.echo():
    # 注意：需要先安装 streamlit-elements
    # pip install streamlit-elements
    try:
        from streamlit_elements import elements, mui, html
        
        with elements("demo"):
            mui.Typography("使用 Streamlit Elements 可以嵌入 Material-UI 组件")
            mui.Button("Material-UI 按钮", variant="contained")
    except ImportError:
        st.warning("需要安装 streamlit-elements: pip install streamlit-elements")

# Streamlit Tags 示例
st.write("#### Streamlit Tags")
with st.echo():
    # 注意：需要先安装 streamlit-tags
    # pip install streamlit-tags
    try:
        from streamlit_tags import st_tags
        
        keywords = st_tags(
            label='输入关键词：',
            text='按回车添加更多',
            value=['示例1', '示例2'],
            suggestions=['Python', 'Streamlit', '数据科学', '机器学习'],
            maxtags=5
        )
        st.write(f"输入的关键词：{keywords}")
    except ImportError:
        st.warning("需要安装 streamlit-tags: pip install streamlit-tags")

# Stqdm 示例
st.write("#### Stqdm")
with st.echo():
    # 注意：需要先安装 stqdm
    # pip install stqdm
    try:
        from stqdm import stqdm
        import time
        
        st.write("进度条演示：")
        for i in stqdm(range(10)):
            time.sleep(0.1)  # 模拟耗时操作
        st.success("处理完成！")
    except ImportError:
        st.warning("需要安装 stqdm: pip install stqdm")

# ===================== 使用提示 =====================
st.divider()
st.write("## 📌 使用提示")
st.success("""
1. **新组件**：`st.feedback`、`st.pills`、`st.segmented_control`、`st.datetime_input`、`st.chat_input` 是较新的组件，确保你的 Streamlit 版本是最新的
2. **第三方组件**：使用前需要通过 `pip` 安装对应的包
3. **布局建议**：在实际应用中，可以使用 `st.columns()`、`st.expander()` 等来组织这些组件
4. **状态管理**：所有小部件的值在用户交互后会保存在 `st.session_state` 中
5. **表单提交**：将相关小部件放在 `st.form` 中，可以使用 `st.form_submit_button` 一次性提交所有输入
""")

# 显示当前 Streamlit 版本
st.caption(f"当前 Streamlit 版本：{st.__version__}")