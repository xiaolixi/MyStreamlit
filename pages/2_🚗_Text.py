import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streamlit 文本元素演示")

st.title("📝 Streamlit 文本元素演示")

# ===================== 标题与正文文本 =====================
st.write("## 🏷️ 标题与正文文本 (Headings and body text)")

# Title
st.write("#### st.title")
with st.echo():
    st.title("这是应用的主标题")
    st.write("这是应用的主要内容区域...")

# Header
st.write("#### st.header")
with st.echo():
    st.header("这是章节标题")
    st.write("章节内容...")

# Subheader
st.write("#### st.subheader")
with st.echo():
    st.subheader("这是子标题")
    st.write("子章节内容...")

# Markdown
st.write("#### st.markdown")
with st.echo():
    st.markdown("""
    ## Markdown 支持
    
    Streamlit 完全支持 **Markdown** 语法：
    
    - **加粗文字**
    - *斜体文字*
    - `代码片段`
    - [链接](https://streamlit.io)
    - 列表项
        - 子项1
        - 子项2
    
    > 引用文本
    
    表格示例：
    
    | 列1 | 列2 | 列3 |
    |-----|-----|-----|
    | 数据1 | 数据2 | 数据3 |
    """)

# ===================== 格式化文本 =====================
st.write("## ✨ 格式化文本 (Formatted text)")

# Badge
st.write("#### st.badge")
with st.echo():
    st.write("这是一个带徽章的项目")
    st.badge("New")
    st.badge("Success", icon=":material/check:", color="green")

    st.markdown(
        ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
    )
    st.write("支持多种颜色：blue, red, green, orange, violet, gray")

# Caption
st.write("#### st.caption")
with st.echo():
    st.caption("这是一个小字号的说明文字，通常用于图片说明或注释")
    st.image("https://via.placeholder.com/400x200", caption="图片标题")
    st.caption("图1: 这是一个示例图片的详细说明")

# Code block
st.write("#### st.code")
with st.echo():
    st.code("""
import streamlit as st
import pandas as pd

# 创建DataFrame
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
})

# 显示数据
st.dataframe(data)
""", language="python")
    
    st.code("""
SELECT * FROM users 
WHERE age > 25 
ORDER BY created_at DESC 
LIMIT 10;
""", language="sql")

# Echo
st.write("#### st.echo")
with st.echo():
    st.write("下面的代码会在页面上显示并执行：")
    
    with st.echo():
        # 这段代码会被显示并执行
        x = 10
        y = 20
        result = x + y
        st.write(f"{x} + {y} = {result}")
        
# Preformatted text
st.write("#### st.text")
with st.echo():
    st.text("这是等宽字体文本，适合显示：")
    st.text("""
    固定宽度的文本内容
    第二行文本
    第三行文本
    
    格式化的输出：
    Name: John Doe
    Age: 30
    Email: john@example.com
    """)

# LaTeX
st.write("#### st.latex")
with st.echo():
    st.latex(r"""
    数学公式示例：\\
    
    1. 二次方程公式：
    x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\\
    
    2. 积分：
    \int_a^b f(x)\,dx = F(b) - F(a)\\
    
    3. 求和：
    \sum_{i=1}^{n} i = \frac{n(n+1)}{2}\\
    
    4. 矩阵：
    A = \begin{pmatrix}
    a & b \\
    c & d
    \end{pmatrix}\\
    
    5. 极限：
    \lim_{x \to \infty} \frac{1}{x} = 0
    """)

# Divider
st.write("#### st.divider")
with st.echo():
    st.write("这是第一部分内容")
    st.divider()
    st.write("这是分隔线之后的内容")
    st.divider()
    st.write("这是另一部分内容")

# ===================== 实用工具 =====================
st.write("## 🔧 实用工具 (Utilities)")

# Get help
st.write("#### st.help")
with st.echo():
    st.write("查看函数的帮助文档：")
    if st.button("显示 st.write 的帮助信息"):
        st.help(st.write)
    
    if st.button("显示 pandas.DataFrame 的帮助信息"):
        df_example = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        st.help(df_example)

# Render HTML
st.write("#### st.html")
with st.echo():
    st.html("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    ">
        <h3>自定义 HTML 内容</h3>
        <p>使用 st.html 可以渲染自定义的 HTML 和 CSS。</p>
        <ul>
            <li>自定义样式</li>
            <li>特殊布局</li>
            <li>嵌入外部组件</li>
        </ul>
        <button style="
            background: white;
            color: #667eea;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        " onclick="alert('Hello from HTML!')">点击我</button>
    </div>
    """)

# ===================== 第三方组件 =====================
st.write("## 🧩 第三方组件 (Third-party components)")

# Annotated text
st.write("#### annotated_text")
with st.echo():
    try:
        from streamlit_annotated_text import annotated_text
        
        annotated_text(
            "这是一个",
            ("带注释的", "形容词", "#faa"),
            "文本示例，",
            ("不同的", "形容词", "#afa"),
            ("部分", "名词", "#8ef"),
            "可以有",
            ("不同的颜色", "", "#faa"),
            "和",
            ("标签", "名词", "#fea"),
            "。"
        )
    except ImportError:
        st.warning("需要安装 streamlit-annotated-text: pip install streamlit-annotated-text")
        st.code("pip install streamlit-annotated-text")

# Drawable Canvas
st.write("#### st_canvas")
with st.echo():
    try:
        from streamlit_drawable_canvas import st_canvas
        from PIL import Image
        
        st.write("可绘制的画布：")
        
        # 设置画布参数
        stroke_width = st.slider("画笔粗细: ", 1, 25, 3)
        stroke_color = st.color_picker("画笔颜色: ", "#FF0000")
        bg_color = st.color_picker("背景颜色: ", "#FFFFFF")
        
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color=bg_color,
            height=300,
            drawing_mode="freedraw",
            key="canvas",
        )
        
        if canvas_result.image_data is not None:
            st.image(canvas_result.image_data)
    except ImportError:
        st.warning("需要安装 streamlit-drawable-canvas: pip install streamlit-drawable-canvas")
        st.code("pip install streamlit-drawable-canvas")

# Tags (再次展示，与前一个示例略有不同)
st.write("#### st_tags")
with st.echo():
    try:
        from streamlit_tags import st_tags
        
        st.write("关键词标签输入：")
        keywords = st_tags(
            label='输入项目标签：',
            text='按回车添加，最多5个',
            value=['Python', '数据分析'],
            suggestions=['机器学习', '深度学习', '可视化', 'Streamlit', 'Web应用'],
            maxtags=5,
            key='tags1'
        )
        st.write(f"当前标签：{keywords}")
    except ImportError:
        st.warning("需要安装 streamlit-tags: pip install streamlit-tags")
        st.code("pip install streamlit-tags")

# ===================== 综合示例 =====================
st.divider()
st.write("## 🎯 综合应用示例")

with st.echo():
    # 创建一个完整的数据报告页面
    st.title("📊 数据分析报告")
    
    # 使用徽章标记状态
    col1, col2, col3 = st.columns(3)
    with col1:
        st.badge("更新于: 2025-01-02", color="gray")
    with col2:
        st.badge("状态: 活跃", color="green")
    with col3:
        st.badge("版本: 2.0", color="blue")
    
    st.divider()
    
    # 报告摘要
    st.header("执行摘要")
    st.markdown("""
    本报告展示了如何使用 **Streamlit 文本元素** 创建专业的数据分析报告：
    
    - ✅ **清晰的层级结构**：使用标题、副标题组织内容
    - ✅ **丰富的内容格式**：支持Markdown、代码、数学公式等
    - ✅ **交互式元素**：可折叠区域、工具提示等
    - ✅ **美观的排版**：分隔线、徽章等视觉元素
    """)
    
    # 代码示例部分
    st.subheader("代码实现")
    with st.expander("查看实现代码"):
        st.code("""
        # 创建数据分析报告
        st.title("数据分析报告")
        
        # 添加状态徽章
        st.badge("最新数据", "green")
        
        # 添加Markdown内容
        st.markdown("## 主要发现")
        st.markdown("- 发现1: ...")
        
        # 添加代码示例
        st.code("import pandas as pd", language="python")
        """, language="python")
    
    # 数学公式部分
    st.subheader("统计分析")
    st.latex(r"""
    \begin{aligned}
    \text{均值} &= \frac{1}{n}\sum_{i=1}^{n} x_i \\
    \text{方差} &= \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2 \\
    \text{标准差} &= \sqrt{\text{方差}}
    \end{aligned}
    """)
    
    st.caption("图注: 基本的统计量计算公式")

# ===================== 最佳实践建议 =====================
st.divider()
st.write("## 💡 最佳实践与建议")

st.info("""
### 使用建议：

1. **层级清晰**：
   - 使用 `st.title()` 作为应用主标题
   - 使用 `st.header()` 作为主要章节
   - 使用 `st.subheader()` 作为子章节

2. **内容格式化**：
   - 技术文档：使用 `st.code()` 展示代码
   - 学术内容：使用 `st.latex()` 展示公式
   - 简单文本：使用 `st.text()` 或 `st.markdown()`

3. **视觉增强**：
   - 使用 `st.badge()` 高亮重要状态
   - 使用 `st.divider()` 分隔不同部分
   - 使用 `st.caption()` 添加说明文字

4. **交互功能**：
   - 使用 `st.echo()` 创建教程和示例
   - 使用 `st.help()` 提供内置帮助
   - 使用 `st.html()` 自定义复杂布局
""")

# 显示当前使用的包版本
st.divider()
st.caption(f"Streamlit 版本: {st.__version__} | pandas 版本: {pd.__version__}")