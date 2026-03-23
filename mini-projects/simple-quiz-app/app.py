import streamlit as st

st.title("Quiz App")
q1 = st.radio(
    "1. What is 2+2?",
    ['4','2','6']
    )
q2 = st.radio(
    "2. Capital of India?",
    ["Mumbai", "Delhi", "Chennai"]
)
q3 = st.radio(
    "3. Python is a?",
    ["Snake", "Programming Language", "Game"]
)

if st.button("submit"):
    score=0
    if q1 == "4":
        score +=1
    if q2 == "Delhi":
        score +=1
    if q3 == "Programming Language":
        score += 1

    st.write(f"your score is {score}/3")

    if score == 3:
        st.success("perfect!!")
    else:
        st.success("Good Try!")