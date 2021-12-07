import yfinance as yf
data = yf.download(tickers="TSLA", start="2021-11-30", end="2021-12-07", period="1d")
data = data.drop(["Adj Close", "Volume"], axis=1)
data.to_csv('last_week_stocks.csv')