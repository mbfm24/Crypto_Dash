import os
import requests
import datetime
import streamlit as st
from newsapi import NewsApiClient

# Retrieve the API key from the environment variable
# NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

# Hardcoded api key for testing purposes
newsapi = NewsApiClient(api_key='f52b9a0c753c4abb934b9b491356fe22')

# Specify date range to display 
today = datetime.datetime.now()
week_ago = today - datetime.timedelta(days=7)

# Bitcoin top-headlines
everything = newsapi.get_everything(q='bitcoin', from_param=week_ago.strftime("%Y-%m-%d"), to=today.strftime("%Y-%m-%d"), page_size=5)
                                          #language='en')
                                          #category='business',
                                          #country='us')
                                          #sources='bbc-news,the-verge'
                                          #country='us',

st.write("Bitcoin News")
#for headline in everything['articles']:
    #st.write(headline['title'])
#    st.write(headline['description'])

for article in everything['articles']:
    st.write("[{}]({})".format(article['title'], article['url']), unsafe_allow_html=True)

# Ethereium top-headlines
everything = newsapi.get_everything(q='ethereum', from_param=week_ago.strftime("%Y-%m-%d"), to=today.strftime("%Y-%m-%d"), page_size=5)
st.write("Ethereum News")

for article in everything['articles']:
    st.write("[{}]({})".format(article['title'], article['url']), unsafe_allow_html=True)

# Litecoin top-headlines
everything = newsapi.get_everything(q='litecoin', from_param=week_ago.strftime("%Y-%m-%d"), to=today.strftime("%Y-%m-%d"), page_size=5)
st.write("Litecoin News")

for article in everything['articles']:
    st.write("[{}]({})".format(article['title'], article['url']), unsafe_allow_html=True)

# ZCash top-headlines
everything = newsapi.get_everything(q='zcash', from_param=week_ago.strftime("%Y-%m-%d"), to=today.strftime("%Y-%m-%d"), page_size=5)
st.write("ZCash News")

for article in everything['articles']:
    st.write("[{}]({})".format(article['title'], article['url']), unsafe_allow_html=True)

# Chainlink top-headlines
everything = newsapi.get_everything(q='Chainlink', from_param=week_ago.strftime("%Y-%m-%d"), to=today.strftime("%Y-%m-%d"), page_size=5)
st.write("Chainlink News")

for article in everything['articles']:
    st.write("[{}]({})".format(article['title'], article['url']), unsafe_allow_html=True)

print(everything)