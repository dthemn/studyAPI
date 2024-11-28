from dotenv import load_dotenv
import os
from pyairtable import Api
import requests
import json

CRYPTO = ['BTC-USDT', 'ETH-USDT', 'SOL-USDT', 'TON-USDT', 'BNB-USDT', 'ADA-USDT', 'DOGE-USDT']

load_dotenv()

api_token = os.environ['AIRTABLE_API_TOKEN']
api = Api(api_token)

# Get crypto data from `https://api.kanga.exchange/api/v2/market/changes?market=${market}`
def fetch_crypto_data(market):
    url = f'https://api.kanga.exchange/api/v2/market/changes?market={market}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

# Function to prepare data for Airtable
def prepare_airtable_record(market, data):
    return {
        'market': market,
        'price': data['price'],
        'timestamp': data['timestamp'],
        'volume': data['volume'],
        'minPrice': data['minPrice'],
        'maxPrice': data['maxPrice'],
        'change': data['change'],
        'changeQuantity': data['changeQuantity'],
        'volume24': data['volume24'],
        'quantityVolume24': data['quantityVolume24'],
        'weeklyVolume': data['weeklyVolume'],
        'monthlyVolume': data['monthlyVolume'],
        'lowestAsk': data['lowestAsk'],
        'highestBid': data['highestBid']
    }

def main():
    app_id = os.environ['AIRTABLE_BASE_ID']
    table_id = os.environ['AIRTABLE_TABLE_ID']
    table = api.table(app_id, table_id)

    for market in CRYPTO:
        data = fetch_crypto_data(market)
        if data:
            record = prepare_airtable_record(market, data)
            table.create(record)

if __name__ == "__main__":
    main()
