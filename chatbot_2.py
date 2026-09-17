import os
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Streamlit page
st.title("GROQ AI Chatbot")
st.caption("Ask anything below")

st.divider()

# Chat form
with st.form("chat_form"):
    user_input = st.text_area(
        "Your Message",
        placeholder="Type your question here..."
    )

    submitted = st.form_submit_button("Send")

# Run only when submitted
if submitted and user_input:

    
    # ----Answer----
  if submitted:
    llm = ChatGroq(
        model="llama-3.1-8b-instant",  # <--- Change this line here
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