import yfinance as yf
import streamlit as st
import pandas as pd

st.title('Stock Data App')
import time

# Title
st.title('3-Month Stock Ticker Tracker')

# User input for stock ticker
ticker = st.text_input('Enter the stock ticker you want to track:', 'AAPL')

# Time interval for refresh in seconds (set to 60 seconds)
refresh_time = 60

st.write(f"Refreshing data every {refresh_time} seconds.")

run = st.button('Run')
stop = st.empty()  # Placeholder for the 'Stop' button

if run:
    st.write("Fetching and displaying data.")
    
    while True:
        # Fetch 3 months of stock data at 1-day intervals
        data = yf.download(ticker, period="3mo", interval="1d")
        
        if data.empty:
            st.write("Received empty data for ticker ", ticker)
            st.stop()

        # Plot
        st.subheader(f"{ticker} Price Data for the Past 3 Months")
        st.line_chart(data['Close'])

        # Stop button and sleep
        if stop.button('Stop'):
            st.write("Stopped.")
            break

        time.sleep(refresh_time)


