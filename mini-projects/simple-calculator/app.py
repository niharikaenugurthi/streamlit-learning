import streamlit as st

st.title("Simple Calculator App")

num1 = st.number_input("Enter the number 1:",value=0.0)
num2 = st.number_input("Enter the number 2:",value=0.0)

op = st.selectbox("select operation:",("Addition +","Substracion -","multiplication *","division /","remainder %"))

if st.button("Calculate"):
    if op == "Addition +":
        result = num1+num2
    elif op == "Substracion -":
        result = num1-num2
    elif op == "remainder %":
        result= num1%num2
    elif op == "division /":
        if num2==0:
            st.error("cannot divided by zero")
        else:
            result = num1/num2
    elif op=="multiplication *":
        result = num1*num2
    if result is not None:
        st.success(f"result: {result}")
