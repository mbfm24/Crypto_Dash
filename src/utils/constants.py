import os

crypto_names = [f for f in os.listdir('./clean_data') if f.endswith('.csv')]
symbols = {'Bitcoin': 'BTC', 'Chainlink': 'LINK', 'Doge': 'DOGE', 'Ethereum': 'ETH', 'Litecoin': 'LTC', 'ZCash': 'ZEC'}