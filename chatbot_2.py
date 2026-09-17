import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# Streamlit page setup
st.title("GROQ AI Chatbot")
st.caption("Ask anything below")

st.divider()

# Retrieve API key securely from Streamlit secrets
# Make sure you have added GROQ_API_KEY in your Streamlit Cloud App Settings -> Secrets
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error("GROQ_API_KEY not found in Streamlit Secrets. Please configure it in your app settings.")
    st.stop()

# Chat form
with st.form("chat_form"):
    user_input = st.text_area(
        "Your Message",
        placeholder="Type your question here..."
    )

    submitted = st.form_submit_button("Send")

# Run only when submitted and input is provided
if submitted and user_input:
    
    # Initialize ChatGroq with the secure API key and model parameters
    llm = ChatGroq(
        groq_api_key=groq_api_key, # Pass the key explicitly here
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    # Messages
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=user_input)
    ]

    # Generate response
    with st.spinner("Thinking..."):
        response = llm.invoke(messages)

    # Display response
    st.divider()
    st.subheader("Response")
    st.write(response.content)
