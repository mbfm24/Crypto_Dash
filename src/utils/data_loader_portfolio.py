import pandas as pd 
import os
import constants

def generate_empty_portfolio():
	folder_path = './data'
	csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

	csv_dict = {}
	for file_name in csv_files:
		if file_name != 'portfolio_data.csv':
			key = file_name.replace('.csv', '')
			csv_dict[key] = 0
		
	return csv_dict

def clean_data(df, drop_cols = ['open', 'high', 'low']):
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

	return df

def filter_data(df, start_date, end_date):
	
	# Convert date strings to datetime objects
	start_date = pd.to_datetime(start_date)
	end_date = pd.to_datetime(end_date)
	
	df = df.loc[start_date:end_date]
	
	return df

def portfolio_returns(returns_df, weights):
    returns_df['portfolio_return'] = 0
    for index, row in returns_df.iterrows():
        valid_weights = {crypto: weight for crypto, weight in weights.items() if not pd.isna(row[constants.symbols[crypto] + '_return'])}
        if valid_weights and sum(valid_weights.values()) > 0:
            normalized_weights = {crypto: weight / sum(valid_weights.values()) for crypto, weight in valid_weights.items()}
            return_on_date = 0
            for crypto, weight in normalized_weights.items():
                return_on_date += row[constants.symbols[crypto] + '_return'] * weight
            returns_df.loc[index, 'portfolio_return'] = return_on_date

        else:
            returns_df.loc[index, 'portfolio_return'] = 0

    return returns_df