import requests
import datetime
import streamlit as st
from PIL import Image
from newsapi import NewsApiClient

# Loading icon image using PIL
img = Image.open('./Images/1f4f0.png')

# Adding title and icon image to app
st.set_page_config(page_title='News', page_icon = img)

# Remove main menu and footer defaults
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.title("Headlines")

# Hardcoded api key for testing purposes
newsapi = NewsApiClient(api_key='YOUR_API_KEY_HERE')

# List of coins
coins =['Bitcoin', 'Ethereum', 'Litecoin', 'ZCash', 'Chainlink']

# Create checkboxes in the sidebar
selected_coins = st.sidebar.multiselect('Coins', coins)
#selected_coins = st.sidebar.selectbox("Coins", options, format_func=lambda x: x.capitalize())


# Only display headlines for selected coins
if selected_coins:
    for coin in selected_coins:
        q = coin
        everything = newsapi.get_everything(q=q,
                                            language='en',
                                            sort_by='relevancy',
                                            page_size=5)
        st.header(coin)
        for article in everything['articles']:
            st.write("[{}]({})".format(article['title'], article['url']), unsafe_allow_html=True)

# Specify date range to display 
today = datetime.datetime.now()
week_ago = today - datetime.timedelta(days=7)

# Bitcoin top-headlines
everything = newsapi.get_everything(q='bitcoin', language='en', from_param=week_ago.strftime("%Y-%m-%d"), to=today.strftime("%Y-%m-%d"), page_size=5)

# Ethereium top-headlines
everything = newsapi.get_everything(q='ethereum', language='en', from_param=week_ago.strftime("%Y-%m-%d"), to=today.strftime("%Y-%m-%d"), page_size=5)

# Litecoin top-headlines
everything = newsapi.get_everything(q='litecoin', language='en', from_param=week_ago.strftime("%Y-%m-%d"), to=today.strftime("%Y-%m-%d"), page_size=5)

# ZCash top-headlines
everything = newsapi.get_everything(q='zcash', language='en', from_param=week_ago.strftime("%Y-%m-%d"), to=today.strftime("%Y-%m-%d"), page_size=5)

# Chainlink top-headlines
everything = newsapi.get_everything(q='Chainlink', language='en', from_param=week_ago.strftime("%Y-%m-%d"), to=today.strftime("%Y-%m-%d"), page_size=5)

#print(everything)

#This code uses the streamlit library to display news headlines related to Bitcoin, Ethereum, Litecoin, ZCash, and Chainlink. It imports the os, requests, datetime and streamlit libraries. It also imports the NewsApiClient from the newsapi library. The page title is set to 'News' and the page icon is set to a newspaper emoji. A hardcoded api key is used for testing purposes. A date range is specified for the articles that will be displayed. The code then uses a for loop to get the top-headlines related to each of the five cryptocurrencies mentioned above and displays them on the page with a link to each article.

