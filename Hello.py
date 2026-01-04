import streamlit as st
import pandas as pd
import numpy as np
st.logo('new_nag/logo1.png', icon_image="new_nag/logo1.png",
    link="https://streamlit.io/")
st.sidebar.markdown("Hi!")
# 页面配置
st.set_page_config(
    page_title="Streamlit组件案例库 | 完全指南",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ===================== 主标题区 =====================
st.image("new_nag/logo1.png" )
st.markdown("# 📚 **Streamlit组件案例库**")
st.markdown("### 🚀 一站式学习所有Streamlit组件的完整解决方案") 

# ===================== 项目介绍卡片 =====================
with st.container(border=True):
    st.markdown("## 🌟 关于这个项目")
    
    st.markdown("""
    这是我精心打造的**Streamlit组件学习平台。**

    
    ### 🎯 适合谁使用？
    - 👶 **Streamlit新手**：从零开始系统学习
    - 👶 https://myapp-lixi.streamlit.app/
    """)
# ===================== 核心特点展示 =====================
st.divider()

st.markdown("## ✨ 平台核心特点")

# 使用3列展示特点
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("### 📖 **基础组件**")


with col2:
    with st.container(border=True):
        st.markdown("### 🎮 **即看即用**")


with col3:
    with st.container(border=True):
        st.markdown("### 💡 **实用导向**")


# ===================== 数据统计 =====================
st.divider()

st.markdown("## 📊 资源概览")

# 统计卡片
stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.metric("📦 组件总数", "21")

with stats_col2:
    st.metric("📝 案例代码", "20")

with stats_col3:
    st.metric("🎯 实用场景", "3")

with stats_col4:
    st.metric("🔄 最后更新", "今日")

# ===================== 快速入口 =====================
st.divider()

st.markdown("## 🚀 开始探索")
st.info("🚀 **新手快速入门**")
st.info("""
        - streamlit每次点击之后都会重新执行一遍脚本，这是它的一个出乎意料但官网却不怎么着重说明的一个特性
        - 因为上面的这个特性，streamlit提供了一个session_state来存储状态，它实际上就是一个dict
        - 为了避免脚本全都重新执行，可以使用@st.fragment()注解方法，避免全部更新，
        - streamlit还提供了缓存的注解，避免重新执行脚本加载的耗时
        - 使用 `with st.echo()`可以打印脚本内容，还可以执行脚本。
        - streamlit有两种方式实现多页的应用程序。1是使用streamlit约定的目录形式，但是它没有缩进。2是使用st.navigation组件手动构建组件，这个有缩进。
        - stremlit编程最大的不适应，或者说难点，就是上面streamlit会重新执行脚本

 """)
# ===================== 底部信息 =====================
st.divider()
