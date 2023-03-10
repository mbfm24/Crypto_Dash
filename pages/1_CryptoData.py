import streamlit as st
import pandas as pd
from PIL import Image

# Loading icon image using PIL
img = Image.open('./Images/1f4c8.png')

# Adding title and icon image to app
st.set_page_config(
    page_title='Overview',
    page_icon=img
)

# Remove main menu and footer defaults
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.title("Data")

# Define a list of cryptocurrencies to display
CRYPTOS = ["Bitcoin", "Ethereum", "Litecoin", "ZCash", "Chainlink","Doge"]

# Load the data for each cryptocurrency from a CSV file
def load_crypto_data(crypto):
    file_name = f"./data/{crypto}.csv"
    df = pd.read_csv(file_name)
    df["crypto"] = crypto
    return df

# Concatenate all the data into a single dataframe
df = pd.concat([load_crypto_data(crypto) for crypto in CRYPTOS])

# Create a function for displaying the data for a selected cryptocurrency
def display_crypto_data(selected_crypto):
    st.write(df[df['crypto'] == selected_crypto])
    st.line_chart(df[df['crypto'] == selected_crypto]['open'])
    st.line_chart(df[df['crypto'] == selected_crypto]['close'])

# Create a sidebar with links to different parts of the website
sidebar = st.sidebar

bitcoin_data = sidebar.checkbox("Bitcoin")
if bitcoin_data:
    display_crypto_data("Bitcoin")

ethereum_data = sidebar.checkbox("Ethereum")
if ethereum_data:
    display_crypto_data("Ethereum")

litecoin_data = sidebar.checkbox("Litecoin")
if litecoin_data:
    display_crypto_data("Litecoin")

zcash_data = sidebar.checkbox("ZCash")
if zcash_data:
    display_crypto_data("ZCash")

chainlink_data = sidebar.checkbox("Chainlink")
if chainlink_data:
    display_crypto_data("Chainlink")
    
    
