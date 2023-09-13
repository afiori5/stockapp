import yfinance as yf
import streamlit as st

st.title('Stock Data App')

ticker = st.text_input('Enter a stock ticker', 'AAPL')
data = yf.Ticker(ticker)
st.write(f"{ticker} stock data: {data.info}")

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.history(period="1d")
    latest_close = stock_info['Close'][0]
    volume = stock_info['Volume'][0]
    return latest_close, volume

if __name__ == "__main__":
    tickers = ["AAPL", "GOOGL", "AMZN"]  # You can add more tickers here

    print("Fetching stock data...")
    for ticker in tickers:
        latest_close, volume = fetch_stock_data(ticker)
        print(f"{ticker}: Latest Close Price = ${latest_close}, Volume = {volume}")

import time

run = st.button("Run")
stop = st.button("Stop")

if run:
    st.write("Loop started.")
    for i in range(100):
        # Your loop content here
        if stop:
            st.write("Stopped at iteration ", i)
            st.stop()


while True:
    for ticker in tickers:
        latest_close, volume = fetch_stock_data(ticker)
        print(f"{ticker}: Latest Close Price = ${latest_close}, Volume = {volume}")
    time.sleep(60)  # Sleep for 60 seconds


