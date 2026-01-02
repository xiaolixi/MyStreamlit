import streamlit as st
import pandas as pd
import numpy as np

# 页面配置
st.set_page_config(
    page_title="Streamlit组件案例库 | 完全指南",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ===================== 主标题区 =====================
st.markdown("# 📚 **Streamlit组件案例库**")
st.markdown("### 🚀 一站式学习所有Streamlit组件的完整解决方案")

st.divider()

# ===================== 项目介绍卡片 =====================
with st.container(border=True):
    st.markdown("## 🌟 关于这个项目")
    
    st.markdown("""
    这是我精心打造的**Streamlit组件学习平台。**

    
    ### 🎯 适合谁使用？
    - 👶 **Streamlit新手**：从零开始系统学习
    """)

# ===================== 核心特点展示 =====================
st.divider()

st.markdown("## ✨ 平台核心特点")

# 使用3列展示特点
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True, height=180):
        st.markdown("### 📖 **基础组件全覆盖**")


with col2:
    with st.container(border=True, height=180):
        st.markdown("### 🎮 **即看即用**")


with col3:
    with st.container(border=True, height=180):
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

# ===================== 底部信息 =====================
st.divider()
