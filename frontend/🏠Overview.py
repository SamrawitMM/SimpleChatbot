import streamlit as st
from utils.sidebarImg import build_markup_for_logo

def show_overview():
    st.title("Overview")
    st.write("This is the overview section.")
    st.write("Here is some additional information about the overview.")
    st.write("You can navigate to the Chatbot page using the sidebar.")

def main():
    if "page" not in st.session_state:
        st.session_state.page = "Overview"

    if st.session_state.page == "Overview":
        show_overview()
  
if __name__ == "__main__":
    logo_css = build_markup_for_logo("./assets/logo.png")
    st.markdown(logo_css, unsafe_allow_html=True)

    main()







