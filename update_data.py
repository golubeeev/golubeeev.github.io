import requests
import pandas as pd

# Читаем тикеры из файла
with open('tickers.txt', 'r', encoding='utf-8') as f:
    tickers = [line.strip() for line in f if line.strip()]

if not tickers:
    raise SystemExit('No tickers in tickers.txt')

# Формируем URL для Yahoo Finance API
symbols = ','.join(tickers)
url = (
    'https://query1.finance.yahoo.com/v7/finance/quote'
    f'?symbols={symbols}'
)

# Делаем запрос
resp = requests.get(url)
resp.raise_for_status()
json_data = resp.json()

# Извлекаем список результатов
results = json_data.get('quoteResponse', {}).get('result', [])

# Формируем DataFrame только с нужными полями
rows = []
for item in results:
    rows.append({
        'ticker': item.get('symbol'),
        'price': item.get('regularMarketPrice'),
        'pe': item.get('trailingPE'),
        'market_cap': item.get('marketCap'),
        'eps': item.get('epsTrailingTwelveMonths'),
    })

if not rows:
    raise SystemExit('No data fetched from Yahoo Finance')

# Сохраняем в CSV
df = pd.DataFrame(rows)
df.to_csv('data/stocks.csv', index=False)