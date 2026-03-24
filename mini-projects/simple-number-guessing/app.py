import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

# User input
guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

# Check button
if st.button("Check"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")

# Reset button
if st.button("Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.success("Game Reset! Start guessing again.")