import pandas as pd
import os
import constants

# Empty list to store the dataframes 
portfolio_list = []

# Loop through portfolio 
for crypto in constants.crypto_names:

    crypto_name = crypto.split('_', 1)[0]

    returns_file = os.path.join('./clean_data', crypto)


    returns_data = pd.read_csv(returns_file,
                               parse_dates=True,
                               infer_datetime_format=True)

    # Reset date to deal with mixed date/times
    returns_data['date'] = returns_data['date'].str[0:10]
    returns_data = returns_data.drop_duplicates(subset=['date'])
    
    returns_data['date'] = pd.to_datetime(returns_data['date'])
    returns_data = returns_data.set_index('date')
    returns_data = returns_data.sort_index(ascending=True)

    # Recalculate daily return
    returns_data['daily_return'] = returns_data['close'].pct_change()

    # Rename columns
    returns_data = returns_data.rename(columns={'close': constants.symbols[crypto_name]+'_close', 'daily_return': constants.symbols[crypto_name]+'_return'})

    # Drop irrelevant columns
    returns_data = returns_data.drop(list(returns_data.filter(regex='Volume')), axis=1)
    returns_data = returns_data.drop(columns=['symbol'])

    portfolio_list.append(returns_data)
    

returns_df = pd.concat(portfolio_list, axis=1, join='outer')

returns_df.to_csv('./data/portfolio_data.csv')