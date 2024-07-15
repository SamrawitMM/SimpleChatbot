from tracemalloc import start
import streamlit as st
import requests
from PIL import Image

# st.title("Chatbot")
# logo_path = "./assets/logo.png"  # Update with your logo image path
# logo_image = Image.open(logo_path)


# # Sidebar
# with st.sidebar:
#     # Display the logo at the top
#     st.image(logo_image, width=150)  # Adjust width as needed

# #     # Create navigation options
# #     st.title("Navigation")
# #     selection = st.radio(
# #         "Go to",
# #         ["Overview", "Chatbot"]
# #     )

# #     # Radio buttons for user types
# #     st.subheader("Select User Type")
# #     user_type = st.radio(
# #         "User Type",
# #         ["Type 1", "Type 2"]
# #     )

# # # Main content based on the selection
# # if selection == "Overview":
# #     st.title("Overview")
# #     st.write("This is the overview section.")

# # elif selection == "Chatbot":
# #     st.title("Chatbot")
# #     st.write(f"You selected {user_type}.")
# #     # Add more chatbot functionality here


# # sidebar start

# # Function to handle navigation
# def navigate(page):
#     st.session_state.page = page

# # Sidebar setup
#     logo_image = "./assets/logo.png"  # Update with your logo path
#     st.sidebar.image(logo_image, use_column_width=True)

#     if st.sidebar.button("Chatbot"):
#         navigate("Chatbot")

# # Main content based on the selection
# page = st.session_state.get("page", "Overview")

# if page == "Overview":
#     st.title("Overview")
#     st.write("This is the overview section.")

# elif page == "Chatbot":
#     st.title("Chatbot")

#     # # Display radio button for user type selection only on Chatbot page
#     # st.sidebar.subheader("Select User Type")
#     # user_type = st.sidebar.radio(
#     #     "User Type",
#     #     ["Type 1", "Type 2"]
#     # )
#     # st.session_state.user_type = user_type

#     # st.write(f"You selected {st.session_state.user_type}.")

#     # if 'messages' not in st.session_state:
#     #     st.session_state['messages'] = []

#     # user_message = st.text_input("You: ")

#     # if st.button("Send"):
#     #     if user_message:
#     #         response = requests.post("http://backend:8000/chat/", json={"user_message": user_message})
#     #         data = response.json()
#     #         st.session_state['messages'].append((user_message, data["bot_response"]))
#     #         st.session_state['last_response'] = data["bot_response"]
#     #         st.session_state['show_radio'] = True
#     #         user_message = ""
#     #     else:
#     #         st.session_state['show_radio'] = False

#     # st.write("Chat History:")
#     # for user_msg, bot_msg in st.session_state['messages']:
#     #     st.write(f"You: {user_msg}")
#     #     st.write(f"Bot: {bot_msg}")

#     # if 'show_radio' in st.session_state and st.session_state['show_radio']:
#     #     options = ["Yes", "No"]
#     #     feedback = st.radio("Was this response helpful?", options)
#     #     if feedback:
#     #         st.write(f"You selected: {feedback}")
#     #         st.session_state['show_radio'] = False

# sidebar end

# if 'messages' not in st.session_state:
#     st.session_state['messages'] = []

# user_message = st.text_input("You: ")

# if st.button("Send"):
#     if user_message:
#         response = requests.post("http://backend:8000/chat/", json={"user_message": user_message})
#         data = response.json()
#         st.session_state['messages'].append((user_message, data["bot_response"]))
#         user_message = ""

# st.write("Chat History:")
# for user_msg, bot_msg in st.session_state['messages']:
#     st.write(f"You: {user_msg}")
#     st.write(f"Bot: {bot_msg}")


# start

# import streamlit as st
# from PIL import Image
# import base64


# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(png_file):
#     with open(png_file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()


# def build_markup_for_logo(
#     png_file,
#     background_position="50% 10%",
#     margin_top="0",
#     image_width="60%",
#     image_height="",
# ):
#     binary_string = get_base64_of_bin_file(png_file)
#     return """
#             <style>
#                 [data-testid="stSidebarNav"] {
#                     background-image: url("data:image/png;base64,%s");
#                     background-repeat: no-repeat;
#                     background-position: %s;
#                     margin-top: %s;
#                     background-size: %s %s;
#                 }
#             </style>
#             """ % (
#         binary_string,
#         background_position,
#         margin_top,
#         image_width,
#         image_height,
#     )


# def add_logo(png_file):
#     logo_markup = build_markup_for_logo(png_file)
#     st.markdown(
#         logo_markup,
#         unsafe_allow_html=True,
#     )

# add_logo("./assets/logo.png")

# # Load the logo image
# logo_path = "./assets/logo.png"  # Ensure this path is correct
# logo_image = Image.open(logo_path)


# # Function to display the Overview page content
# def show_overview():
#     # setup_sidebar()  # Set up the sidebar when on the Overview page
#     st.title("Overview")
#     st.write("This is the overview section.")
#     # Add additional description or content here
#     st.write("Here is some additional information about the overview.")
#     st.write("You can navigate to the Chatbot page using the sidebar.")

# # Main application setup
# def main():
#     if "page" not in st.session_state:
#         st.session_state.page = "Overview"

#     if st.session_state.page == "Overview":
#         show_overview()
#     elif st.session_state.page == "Chatbot":
#         st.write("You are on the Chatbot page. Navigate from the Chatbot page.")  # Placeholder message for the Chatbot page

# if __name__ == "__main__":
#     main()


# ------------------------------------------


import base64
import streamlit as st
from utils.sidebarImg import build_markup_for_logo

# # Function to display the Overview page content
def show_overview():
    # setup_sidebar()  # Set up the sidebar when on the Overview page
    st.title("Overview")
    st.write("This is the overview section.")
    # Add additional description or content here
    st.write("Here is some additional information about the overview.")
    st.write("You can navigate to the Chatbot page using the sidebar.")

# Main application setup
def main():


    if "page" not in st.session_state:
        st.session_state.page = "Overview"

    if st.session_state.page == "Overview":
        show_overview()
    elif st.session_state.page == "Chatbot":
        st.write("You are on the Chatbot page. Navigate from the Chatbot page.")  # Placeholder message for the Chatbot page

if __name__ == "__main__":
    logo_css = build_markup_for_logo("./assets/logo.png")
    st.markdown(logo_css, unsafe_allow_html=True)

    main()







# end