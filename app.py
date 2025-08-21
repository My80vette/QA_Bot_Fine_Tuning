import streamlit as st
from bot import generate_response

# Set page config
st.set_page_config(page_title="Internal Policy Q/A Chatbot", layout="centered")

# Title
st.title("Internal Policy Q/A Chatbot")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for usability features
with st.sidebar:
    st.header("Options")
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()
    st.markdown("**Tip:** Use the chat window below to ask questions about internal policies.")

# Chat window
st.subheader("Chat Window")
for entry in st.session_state.chat_history:
    if entry["role"] == "user":
        st.markdown(f"**You:** {entry['content']}")
    else:
        st.markdown(f"**Bot:** {entry['content']}")

# Use a form with clear_on_submit=True to automatically clear the input after submission
with st.form(key="message_form", clear_on_submit=True):
    user_input = st.text_input("Type your question here...", key="user_input")
    submit_button = st.form_submit_button("Send")
    
    if submit_button and user_input.strip():
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        bot_response = generate_response(user_input)
        st.session_state.chat_history.append({"role": "bot", "content": bot_response})
        st.rerun()