import yfinance as yf

def print_stock_data(stock_symbol):
    """
    Prints open, close, intraday high & low, and the 200-day moving average
    for the given stock symbol from the previous day.
    """
    stock = yf.Ticker(stock_symbol)

    # Fetching historical data
    historical_data = stock.history(period='1d')

    # Fetching the 200-day moving average from stock info
    stock_info = stock.info
    two_hundred_MDA = round(stock_info.get('twoHundredDayAverage', 0), 2)  # Using .get() for safe access

    if not historical_data.empty:
        date = historical_data.index[0].strftime('%Y-%m-%d')
        open_price = round(historical_data['Open'].iloc[0], 2)
        close_price = round(historical_data['Close'].iloc[0], 2)
        intraday_high = round(historical_data['High'].iloc[0], 2)
        intraday_low = round(historical_data['Low'].iloc[0], 2)

        print(f"Date: {date}\nOpen Price: {open_price}\nClose Price: {close_price}\n"
              f"Intraday High: {intraday_high}\nIntraday Low: {intraday_low}\n200-Day Moving Average: {two_hundred_MDA}")
    else:
        print(f"No recent trading data available for {stock_symbol}.")

def print_stock_history_columns(stock_symbol):
    """
    Prints the column names of the historical data for the given stock symbol.
    """
    stock = yf.Ticker(stock_symbol)
    historical_data = stock.history(period='1mo')  # Adjust the period as needed

    print(historical_data.columns)

# Example usage
print_stock_history_columns("MSFT")

