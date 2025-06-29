import requests
import pandas as pd

# Читаем тикеры из файла
with open('tickers.txt', 'r', encoding='utf-8') as f:
    tickers = [line.strip() for line in f if line.strip()]

if not tickers:
    raise SystemExit('No tickers in tickers.txt')

# Формируем URL
symbols = ','.join(tickers)
url = f'https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbols}'

# Получаем данные
resp = requests.get(url)
resp.raise_for_status()
data = resp.json()['quoteResponse']['result']

# Формируем DataFrame
df = pd.DataFrame([{
    'ticker': item.get('symbol'),
    'price': item.get('regularMarketPrice'),
    'pe': item.get('trailingPE'),
    'pb': item.get('priceToBook'),
    'peg': item.get('pegRatio'),
} for item in data])

# Сохраняем CSV
df.to_csv('data/stocks.csv', index=False)