import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
st.logo('new_nag/1.png', icon_image="new_nag/2.png",
    link="https://streamlit.io/")
st.set_page_config(page_title="Streamlit 写入与魔法命令")

st.title("✍️ st.write 与魔法命令演示")

st.markdown("""
本页面演示了Streamlit中三种最核心的数据输出方式：
- `st.write()`：全能型写入函数
- `st.write_stream()`：流式输出（模拟打字机效果）
- **魔法命令 (Magic commands)**：自动显示变量
""")

# ===================== st.write =====================
st.divider()
st.header("1️⃣ st.write")

st.markdown("`st.write()` 是Streamlit最通用的输出命令，可以接受几乎任何类型的参数。")

# 示例1：基本文本和Markdown
st.subheader("📝 文本与Markdown")
with st.echo():
    st.write("你好，世界！")  # 纯文本
    st.write("这是 **加粗文字**，这是 *斜体文字*。")  # Markdown
    st.write("[这是一个链接](https://streamlit.io)")  # 链接也会被渲染

# 示例2：显示数据
st.subheader("📊 显示数据")
with st.echo():
    # 创建一个示例DataFrame
    df = pd.DataFrame({
        '姓名': ['张三', '李四', '王五'],
        '年龄': [25, 30, 35],
        '城市': ['北京', '上海', '广州']
    })
    
    st.write("### 员工信息表")
    st.write(df)  # 直接显示DataFrame，Streamlit会自动渲染成表格
    
    # 显示字典
    config = {'版本': '1.2.3', '作者': 'Streamlit团队', '发布时间': '2025年'}
    st.write("配置信息:", config)

# 示例3：显示图表和图形
st.subheader("📈 显示图表")
with st.echo():
    # 创建一个简单的matplotlib图表
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)
    ax.set_title("sin graph")
    
    st.write(fig)  # 直接显示matplotlib图形
    
    # 也可以显示多个对象
    st.write("### 多个对象一起显示")
    st.write("图表标题:", "正弦波", fig, "图表结束。")



# ===================== st.write_stream =====================
st.divider()
st.header("2️⃣ st.write_stream")

st.markdown("`st.write_stream()` 用于流式输出，可以逐字显示文本，适合显示生成内容或API响应。")

# 示例1：模拟流式文本生成
st.subheader("⏳ 模拟流式输出")
with st.echo():
    def simulate_streaming_text():
        """模拟流式文本生成器"""
        text = "Streamlit的st.write_stream函数可以逐字显示文本，模拟打字机效果。"
        for char in text:
            yield char
            time.sleep(0.1)  # 添加微小延迟以模拟流式效果
    
    if st.button("开始流式输出"):
        st.write_stream(simulate_streaming_text())

# 示例2：模拟LLM响应
st.subheader("🤖 模拟AI响应")
with st.echo():
    def simulate_llm_response(prompt):
        """模拟大型语言模型的流式响应"""
        responses = [
            f"你好！你问的是：'{prompt}'。",
            "\n\n这是一个模拟的AI响应。",
            "\n\n在真实应用中，这里会连接实际的AI模型API。",
            "\n\nStreamlit的流式输出功能非常适合展示这类内容。"
        ]
        
        for response in responses:
            for char in response:
                yield char
                time.sleep(0.1)
            time.sleep(0.5)  # 段落间的停顿
    
    prompt = st.text_input("输入一个问题:", "请解释Streamlit的用途")
    
    if st.button("获取AI响应"):
        st.write_stream(simulate_llm_response(prompt))

# 示例3：进度指示器
st.subheader("📊 带进度的流式输出")
with st.echo():
    def data_processing_stream():
        """模拟数据处理进度"""
        steps = [
            ("正在加载数据...", 10),
            ("数据预处理...", 20),
            ("训练模型...", 50),
            ("生成结果...", 20)
        ]
        
        for message, duration in steps:
            for i in range(duration):
                progress = (i + 1) / duration * 100
                yield f"{message} {progress:.0f} \n"
                time.sleep(0.05)
            yield f"✅ {message} 完成！\n\n"
    
    if st.button("开始处理数据"):
        st.write_stream(data_processing_stream())

# ===================== 魔法命令 =====================
st.divider()
st.header("✨ 魔法命令 (Magic Commands)")

st.markdown("""
魔法命令是Streamlit的特殊功能：**当变量或值单独出现在一行时，Streamlit会自动使用`st.write()`显示它**。
""")

# 示例1：直接显示变量
st.subheader("🎩 自动显示变量")
with st.echo():
    # 这些变量会自动显示
    magic_number = 42
    magic_text = "这是魔法！"
    magic_list = ["苹果", "香蕉", "橙子"]
    
    # 在脚本中直接放置变量，它们会自动显示
    magic_number
    magic_text
    magic_list

# 示例2：显示数据框和图表
st.subheader("🔮 显示复杂对象")
with st.echo():
    # 创建一些数据
    magic_df = pd.DataFrame(
        np.random.randn(5, 3),
        columns=['A列', 'B列', 'C列']
    )
    
    # 创建图表
    magic_fig, magic_ax = plt.subplots()
    magic_ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    magic_ax.set_title("magic graph")
    
    # 这些对象会自动显示
    "### 魔法数据框"
    magic_df
    
    "### 魔法图表"
    magic_fig

# 示例3：组合使用
st.subheader("🔄 混合使用")
with st.echo():
    # 魔法命令和常规代码混合
    "---"
    "## 混合示例"
    "下面是一个随机数矩阵:"
    
    random_matrix = np.random.rand(3, 3)
    random_matrix
    
    "矩阵的形状是:"
    random_matrix.shape

# ===================== 综合对比 =====================
st.divider()
st.header("🆚 三种方式对比")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("st.write()")
    st.markdown("""
    **优点：**
    - 最灵活，完全控制
    - 可以混合多种类型
    - 明确的代码意图
    
    **适用场景：**
    - 需要格式化输出时
    - 混合文本和对象时
    - 生产代码中推荐使用
    """)

with col2:
    st.subheader("st.write_stream()")
    st.markdown("""
    **优点：**
    - 流式输出，体验好
    - 模拟打字机效果
    - 适合长内容生成
    
    **适用场景：**
    - AI/LLM响应
    - 进度指示
    - 实时数据流
    """)

with col3:
    st.subheader("魔法命令")
    st.markdown("""
    **优点：**
    - 代码最简洁
    - 快速原型设计
    - 交互式探索
    
    **适用场景：**
    - Jupyter风格探索
    - 教程和演示
    - 快速调试
    """)

# ===================== 最佳实践 =====================
st.divider()
st.header("💡 最佳实践")

st.markdown("""
### 使用建议：

1. **生产代码**：
   - 优先使用 `st.write()`，代码意图更明确
   - 避免在重要逻辑中使用魔法命令

2. **快速原型**：
   - 使用魔法命令快速探索数据和想法
   - 类似Jupyter笔记本的体验

3. **用户体验**：
   - 对AI响应、进度更新使用 `st.write_stream()`
   - 为用户提供实时反馈

4. **代码清晰度**：
   - 混合使用时保持一致性
   - 复杂输出用 `st.write()`，简单显示用魔法命令
""")

# ===================== 实际应用示例 =====================
st.divider()
st.header("🚀 实际应用示例")

with st.echo():
    # 模拟一个数据分析报告
    st.title("数据分析报告")
    
    # 使用魔法命令快速显示
    report_data = {
        "总记录数": 10000,
        "平均年龄": 34.5,
        "城市分布": {"北京": 3000, "上海": 3500, "广州": 2000, "其他": 1500}
    }
    
    "## 报告概览"
    report_data
    
    # 使用st.write进行格式化输出
    st.write("### 📈 关键指标")
    st.write(f"数据集中共有 **{report_data['总记录数']}** 条记录")
    st.write(f"平均年龄为 **{report_data['平均年龄']}** 岁")
    
    # 使用st.write_stream模拟报告生成
    def generate_report_insights():
        insights = [
            "\n## 🔍 深度分析\n",
            "基于数据挖掘，我们发现以下洞察：\n\n",
            "1. **地域分布**：上海的用户最多，占总数的35%\n",
            "2. **年龄特征**：主要用户群体集中在30-40岁之间\n",
            "3. **增长趋势**：过去季度用户增长率为15%\n\n",
            "建议下一步行动：深入分析用户行为模式。"
        ]
        
        for insight in insights:
            for char in insight:
                yield char
                time.sleep(0.01)
    
    if st.button("生成深度分析报告"):
        st.write_stream(generate_report_insights())

# 显示版本信息
st.divider()
st.caption(f"Streamlit版本: {st.__version__} | 最后更新: 2025-01-02")