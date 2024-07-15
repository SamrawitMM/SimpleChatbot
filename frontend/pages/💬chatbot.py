import streamlit as st
import requests
from utils.sidebarImg import build_markup_for_logo

def main():
    st.title("Chatbot")
    
    st.sidebar.subheader("Select User Type")
    user_type = st.sidebar.radio(
        "User Type",
        ["Normal User", "IREX User"]
    )
    st.session_state.user_type = user_type

    st.write(f"You selected {st.session_state.user_type}.")

    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    user_message = st.text_input("You: ")

    if st.button("Send"):
        if user_message:
            response = requests.post("http://backend:8000/chat/", json={"user_message": user_message})
            data = response.json()
            st.session_state['messages'].append((user_message, data["bot_response"]))
            st.session_state['last_response'] = data["bot_response"]
            st.session_state['show_radio'] = True
            user_message = ""
        else:
            st.session_state['show_radio'] = False

    st.write("Chat History:")
    for user_msg, bot_msg in st.session_state['messages']:
        st.write(f"You: {user_msg}")
        st.write(f"Bot: {bot_msg}")

    if 'show_radio' in st.session_state and st.session_state['show_radio']:
        options = ["Yes", "No"]
        feedback = st.radio("Was this response helpful?", options)
        if feedback:
            st.write(f"You selected: {feedback}")
            st.session_state['show_radio'] = False

if __name__ == "__main__":
    logo_css = build_markup_for_logo("./assets/logo.png")
    st.markdown(logo_css, unsafe_allow_html=True)

    main()




