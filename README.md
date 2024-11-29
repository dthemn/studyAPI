# Why I write this project 
#### I'm learning work with API

`main.py` take some crypto markets from [kanga.exchange](kanga.exchange)

from API https://api.kanga.exchange/api/v2/market/changes?marke=BTC-USDT 

then format the data and push it to my [Airtable](https://airtable.com/app4Ek1SgSV0CwCjU/shremohLAshLYZim2) 
that's all 

## Set up .env file
```
AIRTABLE_API_TOKEN = "xxxxxxxxxx.xxxxxxxxxxxxxx"
AIRTABLE_BASE_ID = "xxxxxxxxxxxxxxx"
AIRTABLE_TABLE_ID = "xxxxxxxxxxxxxx"
```
## 
For package management I'm using [**uv**](https://github.com/astral-sh/uv)

Install uv from [github/astral-sh/uv](https://github.com/astral-sh/uv)

