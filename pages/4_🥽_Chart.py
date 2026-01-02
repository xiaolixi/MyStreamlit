import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
st.logo('new_nag/1.png', icon_image="new_nag/2.png",
    link="https://streamlit.io/")

st.set_page_config(page_title="Streamlit 图表大全")
st.title("📈 Streamlit 图表元素完全指南")

# 准备示例数据
@st.cache_data
def load_chart_data():
    """生成用于各种图表的示例数据"""
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=60, freq='D')
    
    # 主要时间序列数据
    trend_data = pd.DataFrame({
        '日期': dates,
        '产品A': np.random.randn(60).cumsum() + 50,
        '产品B': np.random.randn(60).cumsum() + 30,
        '产品C': np.sin(np.linspace(0, 20, 60)) * 10 + 40,
        '产品D': np.linspace(20, 80, 60) + np.random.randn(60) * 5
    })
    
    # 分类数据
    category_data = pd.DataFrame({
        '类别': ['电子产品', '服装', '食品', '家居', '图书'],
        '销售额': [120, 85, 150, 65, 45],
        '利润': [40, 25, 60, 20, 15],
        '增长率': [0.12, 0.08, 0.18, 0.05, 0.03]
    })
    
    # 地理数据
    city_data = pd.DataFrame({
        '城市': ['北京', '上海', '广州', '深圳', '杭州', '成都', '武汉', '西安'],
        '纬度': [39.9042, 31.2304, 23.1291, 22.5431, 30.2741, 30.5728, 30.5928, 34.3416],
        '经度': [116.4074, 121.4737, 113.2644, 114.0579, 120.1551, 104.0668, 114.3055, 108.9398],
        '销售额': [500, 450, 300, 350, 200, 250, 180, 150],
        '店铺数量': [50, 45, 30, 35, 20, 25, 18, 15]
    })
    
    # 散点图数据
    scatter_data = pd.DataFrame({
        '广告投入': np.random.uniform(10, 100, 100),
        '销售额': np.random.uniform(50, 200, 100) * 0.8 + np.random.randn(100) * 15,
        '产品线': np.random.choice(['A线', 'B线', 'C线'], 100),
        '月份': np.random.choice(['1月', '2月', '3月', '4月'], 100)
    })
    
    return {
        'trend': trend_data,
        'category': category_data,
        'geo': city_data,
        'scatter': scatter_data
    }

data = load_chart_data()

st.markdown("""
本演示涵盖了Streamlit支持的所有图表类型，从简单的原生图表到高级的交互式图表库。
所有图表均使用统一的示例数据，方便对比不同图表类型的特点和适用场景。
""")

# ===================== 简单图表元素 =====================
st.header("1️⃣ 简单图表元素 (Simple chart elements)")

st.markdown("Streamlit内置的简单图表，无需额外安装库，适合快速数据可视化。")

# 区域图
st.subheader("📊 st.area_chart")
with st.echo():
    st.write("**堆叠区域图 - 显示总量和构成趋势**")
    area_data = data['trend'].set_index('日期')
    st.area_chart(area_data, width="stretch")
    
    with st.expander("区域图使用技巧"):
        st.markdown("""
        - **适用场景**：显示时间序列数据的总量和各部分构成
        - **数据格式**：DataFrame，索引为时间，每列为一个系列
        - **堆叠方式**：默认堆叠，可通过`stacked=False`取消堆叠
        - **颜色主题**：自动使用Streamlit主题色
        """)

# 条形图
st.subheader("📊 st.bar_chart")
with st.echo():
    st.write("**分组条形图 - 对比不同类别数据**")
    
    # 重塑数据以适应条形图
    bar_data = data['category'].melt(id_vars='类别', 
                                     value_vars=['销售额', '利润'],
                                     var_name='指标', 
                                     value_name='数值')
    
    bar_chart_data = bar_data.pivot(index='类别', columns='指标', values='数值')
    st.bar_chart(bar_chart_data, width="stretch")


# 折线图
st.subheader("📈 st.line_chart")
with st.echo():
    st.write("**多系列折线图 - 显示趋势和变化**")
    line_data = data['trend'].set_index('日期')
    st.line_chart(line_data, width="stretch")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("总数据点数", len(line_data))
    with col2:
        st.metric("数据系列数", len(line_data.columns))

# 散点图
st.subheader("🔵 st.scatter_chart")
with st.echo():
    st.write("**散点图 - 展示变量间关系**")
    
    # 准备散点图数据
    scatter_df = data['scatter'].copy()
    st.scatter_chart(
        scatter_df,
        x='广告投入',
        y='销售额',
        color='产品线',
        size='销售额',  # 点的大小基于销售额
        width="stretch"
    )
    
    # 相关性分析
    correlation = scatter_df['广告投入'].corr(scatter_df['销售额'])
    st.metric("广告与销售额相关系数", f"{correlation:.3f}")

