import pandas as pd 
import os

df = pd.read_csv('../../data/btc.csv',
                infer_datetime_format=True,
                parse_dates=True,
                header=1)


def generate_empty_portfolio():
	folder_path = '../../data'
	csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

	csv_dict = {}
	for file_name in csv_files:
		key = file_name.replace('.csv', '')
		file_path = os.path.join(folder_path, file_name)
		csv_dict[key] = 0
	
	return csv_dict

def clean_data(df, drop_cols = ['unix', 'open', 'high', 'low']):
	"""Cleans the cryptocurrency price data in the dataframe.
	
	Args:
		df (pd.DataFrame): The cryptocurrency price data in a pandas dataframe
		
	Returns:
		df (pd.DataFrame): The cleaned cryptocurrency price data in a pandas dataframe
	"""
	# Convert date strings to datetime objects
    df['date'] = pd.to_datetime(df['date'])
	
	# Remove irrelevant columns and duplicates
    df = df.drop(columns=drop_cols)
	df = df.drop_duplicates()
	
	# Add returns
	df['daily_return'] = df['close'].pct_change()
	
    return df

def filter_data(df, start_date, end_date):
	
	# Convert date strings to datetime objects
	start_date = pd.to_datetime(start_date)
	end_date = pd.to_datetime(end_date)
	
	df[(df['date'] >= start_date) & (df['Date'] <= end_date)]
	
	return df

def calculate_portfolio_returns(dfs, portfolio):
	portfolio_dfs = 