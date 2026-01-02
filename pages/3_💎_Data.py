import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Streamlit 数据元素演示", layout="wide")
st.title("📊 Streamlit 数据元素演示")

# ===================== 核心数据展示元素 =====================
st.header("1️⃣ 核心数据展示元素")

# 准备示例数据
@st.cache_data
def load_sample_data():
    """生成示例数据"""
    dates = pd.date_range('20240101', periods=100)
    df = pd.DataFrame({
        '日期': dates,
        '产品A销量': np.random.randint(50, 200, 100).cumsum(),
        '产品B销量': np.random.randint(30, 150, 100).cumsum(),
        '产品C销量': np.random.randint(20, 100, 100).cumsum(),
        '单价': np.random.uniform(10, 100, 100).round(2),
        '库存': np.random.randint(100, 500, 100),
        '是否促销': np.random.choice(['是', '否'], 100)
    })
    return df

df = load_sample_data()

# Dataframes - 交互式表格
st.subheader("📋 st.dataframe")
with st.echo():
    st.write("**交互式DataFrame - 支持排序、搜索**")
    st.dataframe(df.head(10), use_container_width=True)
    
    # 显示数据统计信息
    st.write("**数据摘要:**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("总行数", len(df))
    with col2:
        st.metric("总列数", len(df.columns))
    with col3:
        st.metric("数据期间", f"{df['日期'].min().date()} 至 {df['日期'].max().date()}")

# Static tables - 静态表格
st.subheader("📄 st.table")
with st.echo():
    st.write("**静态表格 - 适合小数据集**")
    summary_df = df.describe().round(2)
    st.table(summary_df)

# ===================== 数据编辑元素 =====================
st.header("2️⃣ 数据编辑元素")

# Data editor
st.subheader("✏️ st.data_editor")
with st.echo():
    st.write("**可编辑的数据编辑器**")
    
    # 创建可编辑的副本
    editable_df = df.head(5).copy()
    
    edited_df = st.data_editor(
        editable_df,
        num_rows="dynamic",  # 允许动态添加/删除行
        use_container_width=True,
        hide_index=False,
        column_config={
            "日期": st.column_config.DateColumn("销售日期"),
            "单价": st.column_config.NumberColumn("价格(USD)", format="$%.2f"),
            "是否促销": st.column_config.SelectboxColumn("促销状态", options=["是", "否"])
        }
    )
    
    st.write("**编辑后的数据:**")
    st.dataframe(edited_df, use_container_width=True)
    
    # 显示更改统计
    changes = not edited_df.equals(editable_df)
    if changes:
        st.success("✅ 数据已被修改")
    else:
        st.info("📝 数据未被修改")

# ===================== 列配置系统 =====================
st.header("3️⃣ 列配置系统")

st.subheader("⚙️ st.column_config")
with st.echo():
    st.write("**高级列配置示例**")
    
    # 创建配置好的数据编辑器
    config_df = pd.DataFrame({
        "产品ID": ["P001", "P002", "P003", "P004"],
        "产品名称": ["笔记本电脑", "智能手机", "平板电脑", "智能手表"],
        "价格": [1299.99, 799.99, 499.99, 299.99],
        "库存数量": [45, 120, 80, 200],
        "折扣率": [0.1, 0.15, 0.05, 0.2],
        "发布日期": pd.to_datetime(["2024-01-15", "2024-02-20", "2024-03-10", "2024-04-05"]),
        "是否畅销": [True, True, False, True],
        "用户评分": [4.5, 4.8, 4.2, 4.6]
    })
    
    edited_config = st.data_editor(
        config_df,
        column_config={
            "产品ID": st.column_config.TextColumn("产品编号", disabled=True),
            "产品名称": st.column_config.TextColumn("产品名称", required=True),
            "价格": st.column_config.NumberColumn(
                "价格(USD)",
                min_value=0,
                max_value=10000,
                format="$%.2f",
                help="产品售价"
            ),
            "库存数量": st.column_config.NumberColumn(
                "库存",
                min_value=0,
                format="%d 件"
            ),
            "折扣率": st.column_config.ProgressColumn(
                "折扣率",
                min_value=0,
                max_value=1,
                format="%.0%%"
            ),
            "发布日期": st.column_config.DateColumn("上市日期"),
            "是否畅销": st.column_config.CheckboxColumn("热销产品"),
            "用户评分": st.column_config.NumberColumn(
                "评分",
                min_value=0,
                max_value=5,
                format="%.1f ⭐",
                help="用户评分(0-5)"
            )
        },
        hide_index=True,
        use_container_width=True
    )
    
    # 计算总价值
    total_value = (edited_config["价格"] * edited_config["库存数量"]).sum()
    st.metric("库存总价值", f"${total_value:,.2f}")

# ===================== 指标展示元素 =====================
st.header("4️⃣ 指标展示元素")

st.subheader("📈 st.metric")
with st.echo():
    st.write("**关键指标仪表板**")
    
    # 计算关键指标
    total_sales_A = df["产品A销量"].iloc[-1]
    total_sales_B = df["产品B销量"].iloc[-1]
    total_sales_C = df["产品C销量"].iloc[-1]
    
    prev_sales_A = df["产品A销量"].iloc[-30]
    prev_sales_B = df["产品B销量"].iloc[-30]
    prev_sales_C = df["产品C销量"].iloc[-30]
    
    # 创建指标行
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        delta_A = total_sales_A - prev_sales_A
        st.metric(
            "产品A总销量",
            f"{total_sales_A:,}",
            f"{delta_A:+,}",
            delta_color="normal"
        )
    
    with col2:
        delta_B = total_sales_B - prev_sales_B
        st.metric(
            "产品B总销量",
            f"{total_sales_B:,}",
            f"{delta_B:+,}",
            delta_color="normal"
        )
    
    with col3:
        delta_C = total_sales_C - prev_sales_C
        st.metric(
            "产品C总销量",
            f"{total_sales_C:,}",
            f"{delta_C:+,}",
            delta_color="normal"
        )
    
    with col4:
        total_all = total_sales_A + total_sales_B + total_sales_C
        prev_all = prev_sales_A + prev_sales_B + prev_sales_C
        delta_all = total_all - prev_all
        st.metric(
            "所有产品总销量",
            f"{total_all:,}",
            f"{delta_all:+,}",
            delta_color="normal"
        )

# ===================== JSON 展示元素 =====================
st.header("5️⃣ JSON 展示元素")

st.subheader("🔤 st.json")
with st.echo():
    st.write("**数据结构展示**")
    
    # 创建复杂数据结构
    business_data = {
        "公司信息": {
            "名称": "示例科技有限公司",
            "成立时间": "2020-01-15",
            "员工数": 150,
            "部门": ["研发", "销售", "市场", "人力资源", "财务"]
        },
        "财务数据": {
            "年度收入": {
                "2023": 5000000,
                "2024": 7500000,
                "2025": 9000000
            },
            "利润率": 0.25,
            "主要客户": ["客户A", "客户B", "客户C", "客户D"]
        },
        "产品线": [
            {
                "产品ID": "P001",
                "名称": "企业解决方案",
                "状态": "活跃",
                "月收入": 150000
            },
            {
                "产品ID": "P002",
                "名称": "云服务",
                "状态": "活跃",
                "月收入": 250000
            },
            {
                "产品ID": "P003",
                "名称": "数据分析工具",
                "状态": "测试",
                "月收入": 50000
            }
        ],
        "元数据": {
            "更新时间": datetime.now().isoformat(),
            "数据版本": "1.2.0",
            "格式": "JSON"
        }
    }
    
    # 显示JSON
    with st.expander("查看完整JSON数据"):
        st.json(business_data)


# ===================== 第三方组件 =====================
st.header("6️⃣ 第三方组件")

st.info("以下为社区开发的流行第三方数据组件，需要单独安装。")

# Streamlit AgGrid
st.subheader("🔢 Streamlit AgGrid")
with st.echo():
    try:
        from st_aggrid import AgGrid, GridOptionsBuilder
        
        st.write("**高级网格组件 - 支持复杂交互**")
        
        aggrid_data = pd.DataFrame({
            '员工ID': ['E001', 'E002', 'E003', 'E004', 'E005'],
            '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
            '部门': ['研发', '销售', '市场', '研发', '人力资源'],
            '工资': [80000, 70000, 65000, 85000, 60000],
            '入职日期': pd.date_range('20230101', periods=5),
            '绩效评分': [4.5, 3.8, 4.2, 4.7, 3.9]
        })
        
        # 配置网格选项
        gb = GridOptionsBuilder.from_dataframe(aggrid_data)
        gb.configure_pagination(paginationAutoPageSize=True)
        gb.configure_side_bar()
        gb.configure_default_column(
            editable=True,
            groupable=True,
            sortable=True,
            filter=True
        )
        
        grid_options = gb.build()
        
        grid_response = AgGrid(
            aggrid_data,
            gridOptions=grid_options,
            height=300,
            width='100%',
            fit_columns_on_grid_load=True,
            allow_unsafe_jscode=True
        )
        
        st.write("**选中的数据:**")
        if grid_response['selected_rows']:
            st.dataframe(grid_response['selected_rows'], use_container_width=True)
            
    except ImportError:
        st.warning("需要安装 streamlit-aggrid: `pip install streamlit-aggrid`")
        st.code("pip install streamlit-aggrid")

# Streamlit Folium
st.subheader("🗺️ Streamlit Folium")
with st.echo():
    try:
        import folium
        from streamlit_folium import st_folium
        
        st.write("**交互式地图组件**")
        
        # 创建地图
        m = folium.Map(
            location=[39.9042, 116.4074],  # 北京
            zoom_start=12,
            tiles="OpenStreetMap"
        )
        
        # 添加标记点
        locations = [
            {"name": "总部", "coords": [39.9042, 116.4074], "sales": 5000},
            {"name": "分店A", "coords": [39.9192, 116.4037], "sales": 3000},
            {"name": "分店B", "coords": [39.8892, 116.4177], "sales": 4500},
            {"name": "分店C", "coords": [39.9342, 116.3877], "sales": 3500}
        ]
        
        for loc in locations:
            folium.Marker(
                location=loc["coords"],
                popup=f"{loc['name']}<br>销售额: ${loc['sales']:,}",
                tooltip=f"{loc['name']} (点击查看详情)",
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(m)
        
        # 显示地图
        st_folium(m, width=800, height=500)
        
    except ImportError:
        st.warning("需要安装 streamlit-folium 和 folium: `pip install streamlit-folium folium`")
        st.code("pip install streamlit-folium folium")

# Pandas Profiling
st.subheader("📋 Pandas Profiling")
with st.echo():
    try:
        from pandas_profiling import ProfileReport
        from streamlit_pandas_profiling import st_profile_report
        
        st.write("**自动化数据探查报告**")
        
        if st.button("生成数据探查报告"):
            with st.spinner("正在生成报告..."):
                profile = ProfileReport(
                    df,
                    title="销售数据探查报告",
                    explorative=True,
                    minimal=False
                )
                
                st_profile_report(profile)
                
    except ImportError:
        st.warning("需要安装 streamlit-pandas-profiling 和 pandas-profiling: `pip install streamlit-pandas-profiling pandas-profiling`")
        st.code("pip install streamlit-pandas-profiling pandas-profiling")

# ===================== 性能优化提示 =====================
st.header("7️⃣ 性能优化提示")

st.markdown("""
### 🚀 最佳实践：

1. **数据缓存**：
   - 使用 `@st.cache_data` 缓存计算结果
   - 对静态数据使用 `@st.cache_resource`

2. **分页加载**：
   - 大数据集使用分页显示
   - 考虑使用虚拟滚动

3. **列配置优化**：
   - 只配置需要特殊处理的列
   - 使用合适的列类型减少内存占用

4. **第三方组件**：
   - 按需加载，避免不必要的依赖
   - 注意版本兼容性

5. **错误处理**：
   - 为数据加载添加异常处理
   - 提供友好的错误信息
""")

# 数据大小警告
data_size_mb = df.memory_usage(deep=True).sum() / (1024 * 1024)
if data_size_mb > 10:
    st.warning(f"⚠️ 当前数据集大小: {data_size_mb:.2f} MB，建议优化数据加载")


# 版本信息
st.divider()
st.caption(f"📊 Streamlit 数据元素演示 | Streamlit版本: {st.__version__} | 最后更新: 2026-01-02")