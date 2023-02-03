import pandas as pd
import streamlit as st
import sys
import datetime as dt
import os
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objs as go

sys.path.append('./src/utils')
import data_loader_portfolio 


st.set_page_config(page_title='Portfolio Builder', page_icon='📊')

st.markdown('# Portfolio Building Tool')
st.sidebar.header('Portfolio Builder')
st.sidebar.write('If weights sum to over 100%, it will be normalized by dividing by the sum.')

st.write(
    """This application allows you to enter a customized portfolio of cryptocurrencies and view information about their historical performance and their projected future performance based on the result of a Monte Carlo simulation. 
    """
)

def input_interface():
    """Creates an input interface for the streamlit application for users to enter portfolio weights.

    Returns:
        portfolio (dict): A dictionary representing the portfolio of cryptocurrencies. 

    """
    # Create an empty portfolio 
    portfolio = data_loader_portfolio.generate_empty_portfolio()

    # Get the names
    crypto_names = portfolio.keys()

    # Loop through the names and create number input boxes to collect weights
    for crypto in crypto_names:
        weight = st.sidebar.number_input(f'Weight (%) for {crypto}', min_value =0, max_value=100, value=0, step=1)
        
        portfolio[crypto] = weight / 100
        portfolio_sum = sum(portfolio.values())

        # Normalize the weights
        if portfolio_sum > 1:
            portfolio = {crypto: weight / portfolio_sum for crypto, weight in portfolio.items()}



    return {'portfolio': portfolio}

user_input = input_interface()

# Enter start/end date information
st.write('Enter the backtest start and end dates:')

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input('Start Date:', key='start_date_1',value=dt.datetime(2018, 1, 1), min_value=dt.datetime(2015, 10, 9), max_value=dt.datetime(2023, 2, 1))

with col2: 
    end_date = st.date_input('End Date:', key='end_date_1', value=dt.datetime(2023, 2, 1), min_value=dt.datetime(2015, 10, 9), max_value=dt.datetime(2023, 2, 1))

# Load data
df = pd.read_csv('./data/portfolio_data.csv',
                index_col=0,
                parse_dates=True,
                infer_datetime_format=True)

if (sum(user_input['portfolio'].values()) > 0):
    df = data_loader_portfolio.portfolio_returns(df, user_input['portfolio'])

    mini_df = data_loader_portfolio.filter_data(df, start_date, end_date)
    mini_df['cumulative_return'] = (1 + mini_df['portfolio_return']).cumprod() - 1

    fig = px.line(mini_df, x=mini_df.index, y='cumulative_return', title='Cumulative Return (%)')
    fig.update_yaxes(tickformat='%')
    fig


