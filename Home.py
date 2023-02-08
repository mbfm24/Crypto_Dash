import streamlit as st

st.set_page_config(
    page_title = "Welcome",
    page_icon='👋'
)

# Remove main menu and footer defaults
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


st.write('# Welcome to Crypto Dash')
st.write('The #1 investment management tool for crypto experts and amateurs.')
st.write('Select an application on the left to get started.')
