import streamlit as st


st.title("Zeta AI Chatbot")
st.header("This is st.header")
st.subheader("This is st.subheader")
st.caption("This is st.caption � small grey text")

st.divider()

st.subheader("Text")

st.text("Enter your Query to use this Chatbot")

st.write("st.write works with text, numbers, dicts, dataframes and more")

st.divider()

#form
st.subheader("Form")
st.text_input("name", placeholder="Enter your name")
st.text_input("email", placeholder="Enter your email")
st.text_area("message", placeholder="Enter your message")
st.text_input("age", placeholder="Enter your age")
st.selectbox("country", ["USA", "Canada", "UK", "Australia"])
st.multiselect("interests", ["AI", "Machine Learning", "Data Science", "Web Development"])
st.button("Submit")

#spinner
st.spinner("Loading...")
st.success("Loaded successfully!")

#percwentage calculator
st.subheader("Percentage Calculator")
total = st.number_input("Total Marks", value=100)
marks_obtained = st.number_input("Marks Obtained", value=0)
if total > 0:
    percentage = (marks_obtained / total) * 100
    st.write(f"Percentage: {percentage:.2f}%")
    st.button("Calculate Percentage")
    