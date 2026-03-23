import streamlit as st
from PIL import Image 
st.title("Helloo!")
st.header("header")
st.subheader("subheader")
st.text("text")
st.markdown("### This is the markdown")
st.success("success")
st.info("information")
st.warning("warning")
st.error("error")
exp = ZeroDivisionError("you are trying to divide zero")
st.exception(exp)
st.write("Text with write")
st.write(range(10))
img = Image.open("image.png")
st.image(img, width=200)
if st.checkbox("Show/Hide"):
    st.text("showing the widget")

status = st.radio("select gender:",['Male','Female'])
if status=='Male':
    st.success("male")
else:
    st.success("Female")
hobby = st.selectbox("Select your hobby:",['Dancing','Singing','Drawing','Reading'])
st.write("Your hobby is:",hobby)

hobbies = st.multiselect("Select your hobbies:",['Dancing','Singing','Drawing','Reading'])
st.write("you selected: ",len(hobbies),"hobbies")

st.button("Click me!")
if st.button("about"):
    st.text("Hello Everyone!")

name = st.text_input("enter your name:","Type here")
if st.button("submit"):
    result = name.title() 
    st.write(result)

level = st.slider("Select your level:" ,min_value=0,max_value=10)
st.write(f"Selected level:{level}")
