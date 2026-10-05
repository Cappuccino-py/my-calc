import streamlit as st

st.title("Python 计算器")

内容 = st.text_input("输入算式（支持 × ÷）：")

if 内容:
    内容 = 内容.replace("×", "*").replace("÷", "/")
    try:
        结果 = eval(内容)
        st.success(f"输出：{结果}")
    except:
        st.error("输入有误，请重新输入")
