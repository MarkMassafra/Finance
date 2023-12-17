import yfinance as yf

ticker = yf.Ticker("MSFT")

info = ticker.info

for key in info:
    print(key, ":",info[key])

