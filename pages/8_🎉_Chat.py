import streamlit as st
import numpy as np
import pandas as pd
import time
import random

st.set_page_config(page_title="Streamlit 聊天元素演示", page_icon="💬")
st.title("💬 Streamlit 聊天元素演示")

# 初始化会话状态以保存聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 初始化处理状态
if "processing" not in st.session_state:
    st.session_state.processing = False

st.markdown("""
本页面演示了Streamlit聊天元素的核心组件，可用于构建对话式应用或AI助手界面。
- `st.chat_message()`：显示聊天消息容器
- `st.chat_input()`：显示聊天输入框
- `st.status()`：显示长任务状态
- `st.write_stream()`：流式输出（打字机效果）
""")


# ===================== 第二部分：高级聊天消息 =====================
st.divider()
st.header("2️⃣ 高级聊天消息展示")

st.subheader("👥 st.chat_message")
with st.echo():
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**用户消息示例:**")
        with st.chat_message("user"):
            st.write("👋 你好！")
            st.write("我需要一些数据分析帮助。")
            st.metric(label="当前指标", value="87%", delta="+2%")
    
    with col2:
        st.write("**助手消息示例:**")
        with st.chat_message("assistant"):
            st.write("🔍 你好！我可以帮你分析数据。")
            
            # 在聊天消息中嵌入表格
            sample_data = pd.DataFrame({
                '月份': ['1月', '2月', '3月', '4月'],
                '销售额': [12000, 15000, 11000, 18000],
                '增长率': ['+5%', '+12%', '-3%', '+20%']
            })
            st.dataframe(sample_data, width="stretch")
            
            # 在聊天消息中嵌入图表
            chart_data = pd.DataFrame(
                np.random.randn(10, 2),
                columns=['系列1', '系列2']
            )
            st.area_chart(chart_data)

# 自定义头像和名称
with st.echo():
    st.write("**自定义消息样式:**")
    
    # 使用emoji作为头像
    with st.chat_message("user", avatar="🧑‍💻"):
        st.write("我是开发人员，使用自定义头像！")
    
    # 使用系统角色
    with st.chat_message("system", avatar="⚙️"):
        st.write("系统通知：所有服务运行正常。")
        st.info("这是一个系统状态消息。")
    
    # 使用AI助手角色
    with st.chat_message("assistant", avatar="🤖"):
        st.write("我是AI助手，可以回答各种问题。")
        st.success("当前状态：在线且可用")

# ===================== 第三部分：状态容器 =====================
st.divider()
st.header("3️⃣ 长任务状态管理")

st.subheader("⏳ st.status")
with st.echo():
    if st.button("启动模拟数据处理任务"):
        st.session_state.processing = True
        
    if st.session_state.processing:
        with st.status("正在处理数据...", expanded=True) as status:
            # 步骤1：加载数据
            st.write("📥 步骤1: 加载数据集...")
            time.sleep(1.5)
            
            # 步骤2：数据清洗
            st.write("🧹 步骤2: 清洗和预处理数据...")
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)
            
            # 步骤3：模型训练
            st.write("🤖 步骤3: 训练机器学习模型...")
            time.sleep(2)
            
            # 步骤4：生成结果
            st.write("📊 步骤4: 生成分析报告...")
            time.sleep(1)
            
            # 完成
            status.update(label="数据处理完成！", state="complete", expanded=False)
            st.success("✅ 任务成功完成！")
            
            # 显示结果
            with st.chat_message("assistant"):
                st.write("## 分析报告摘要")
                st.write("数据处理已完成，以下是关键发现：")
                
                results = pd.DataFrame({
                    '指标': ['准确率', '召回率', 'F1分数', 'AUC'],
                    '值': [0.92, 0.88, 0.90, 0.94],
                    '状态': ['优秀', '良好', '优秀', '优秀']
                })
                st.dataframe(results)
        
        st.session_state.processing = False
 

# ===================== 第五部分：综合应用示例 =====================
st.divider()
st.header("5️⃣ 综合应用：AI数据分析助手")

st.markdown("结合所有聊天元素，创建一个完整的数据分析助手示例。")

# 初始化综合聊天记录
if "ai_messages" not in st.session_state:
    st.session_state.ai_messages = []

# 显示AI助手对话历史
for message in st.session_state.ai_messages:
    with st.chat_message(message["role"], avatar=message.get("avatar", "👤")):
        st.write(message["content"])
        if "data" in message:
            st.dataframe(message["data"])

# 模拟AI助手回复函数
def ai_data_analyst_response(user_query):
    """模拟AI数据分析助手的响应"""
    
    # 模拟思考过程
    with st.status("正在分析您的问题...", expanded=False) as status:
        st.write("🔍 理解问题意图...")
        time.sleep(0.5)
        st.write("📊 检索相关数据...")
        time.sleep(0.5)
        st.write("🥌 生成分析结果...")
        time.sleep(0.5)
        status.update(label="分析完成！", state="complete")
    
    # 根据问题类型生成响应
    if "销售" in user_query or "业绩" in user_query:
        # 生成销售数据
        sales_data = pd.DataFrame({
            '季度': ['Q1', 'Q2', 'Q3', 'Q4'],
            '销售额(万)': [120, 150, 130, 180],
            '同比增长': ['+5%', '+12%', '+8%', '+15%'],
            '达成率': ['95%', '102%', '98%', '105%']
        })
        
        response = f"根据您关于 **'{user_query}'** 的查询，这是最近四个季度的销售数据分析："
        
        # 流式输出响应
        def stream_response():
            for char in response:
                yield char
                time.sleep(0.01)
        
        return stream_response(), sales_data
    
    elif "图表" in user_query or "可视化" in user_query:
        # 生成图表数据
        chart_df = pd.DataFrame(
            np.random.randn(15, 3),
            columns=['产品A', '产品B', '产品C']
        )
        
        response = f"已为您生成数据可视化图表："
        
        def stream_response():
            for char in response:
                yield char
                time.sleep(0.01)
        
        return stream_response(), chart_df
    
    else:
        # 默认响应
        response = f"我已收到您的查询：'{user_query}'。这是一个通用的数据分析回复。您可以问我关于销售、图表或具体业务指标的问题。"
        
        default_data = pd.DataFrame({
            '功能': ['聊天交互', '数据展示', '流式输出', '状态管理'],
            '状态': ['✅ 可用', '✅ 可用', '✅ 可用', '✅ 可用'],
            '说明': ['实时对话', '表格和图表', '打字机效果', '长任务反馈']
        })
        
        def stream_response():
            for char in response:
                yield char
                time.sleep(0.01)
        
        return stream_response(), default_data

# AI助手聊天输入
st.subheader("🥌 与AI数据分析助手对话")

ai_prompt = st.chat_input("向AI助手提问数据分析问题...")

if ai_prompt:
    # 添加用户消息
    st.session_state.ai_messages.append({
        "role": "user", 
        "content": ai_prompt,
        "avatar": "🧑‍💼"
    })
    
    # 立即显示用户消息
    with st.chat_message("user", avatar="🧑‍💼"):
        st.write(ai_prompt)
    
    # 生成并显示AI回复
    with st.chat_message("assistant", avatar="🥌"):
        # 获取AI响应
        response_stream, response_data = ai_data_analyst_response(ai_prompt)
        
        # 流式输出文本
        st.write_stream(response_stream)
        
        # 显示数据
        if response_data is not None:
            st.dataframe(response_data)
            
            # 如果是图表数据，也显示图表
            if len(response_data.columns) >= 3:
                st.line_chart(response_data.iloc[:, :3])
    
    # 保存AI回复到历史记录
    st.session_state.ai_messages.append({
        "role": "assistant", 
        "content": f"已回答: {ai_prompt}",
        "avatar": "🥌",
        "data": response_data
    })
    
    # 重新运行
    st.rerun()

# ===================== 使用建议 =====================
st.divider()
st.header("💡 最佳实践与使用建议")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ✅ 推荐用法
    
    1. **组合使用**：将`chat_message`、`chat_input`和`write_stream`结合
    2. **明确角色**：使用不同avatar区分用户、助手、系统
    3. **实时反馈**：对长任务使用`st.status`提供进度
    4. **保存状态**：使用`st.session_state`保存聊天历史
    5. **丰富内容**：在消息中添加图表、表格、指标等
    """)

with col2:
    st.markdown("""
    ### ⚠️ 注意事项
    
    1. **性能优化**：大量消息时考虑分页或虚拟滚动
    2. **状态管理**：及时清理不再需要的会话状态
    3. **用户体验**：流式输出不宜过快或过慢
    4. **错误处理**：为长任务添加超时和错误处理
    5. **移动适配**：测试聊天界面在移动端的显示效果
    """)

# 清理功能
st.divider()
if st.button("🧹 清空所有聊天记录"):
    st.session_state.messages = []
    st.session_state.ai_messages = []
    st.session_state.processing = False
    st.success("聊天记录已清空！")
    st.rerun()

# 版本信息
st.caption(f"💬 Streamlit 聊天元素演示 | Streamlit版本: {st.__version__}")