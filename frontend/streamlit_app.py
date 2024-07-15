import streamlit as st
import requests

st.title("Chatbot")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

user_message = st.text_input("You: ")

if st.button("Send"):
    if user_message:
        response = requests.post("http://backend:8000/chat/", json={"user_message": user_message})
        data = response.json()
        st.session_state['messages'].append((user_message, data["bot_response"]))
        user_message = ""

st.write("Chat History:")
for user_msg, bot_msg in st.session_state['messages']:
    st.write(f"You: {user_msg}")
    st.write(f"Bot: {bot_msg}")
