import streamlit as st


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

# Input box for user message
user_input = st.text_input("Type your question here...", key="user_input")

# Send button
if st.button("Send"):
    if user_input.strip():
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        # Placeholder bot response (replace with actual model call)
        bot_response = "This is a placeholder response. (Integrate your model here.)"
        st.session_state.chat_history.append({"role": "bot", "content": bot_response})
        st.session_state.user_input = ""  # Clear input box
        st.rerun()