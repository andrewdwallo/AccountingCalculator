import streamlit as st

def app():
    st.title('Dividend Yield Ratio')
    
    st.subheader("Dividends Per Share")
    colDividendsPerShare = st.columns(1)
    dividends_per_share = st.number_input("Enter the dividends per share of common stock($): ", min_value=0.0, format='%f')
    
    st.subheader("Market Price Per Share")
    colMarketPricePerShare = st.columns(1)
    market_price_per_share = st.number_input("Enter the market value of the company's common stock at the end of the year (Market Price Per Share)($): ", min_value=0.0, format='%f')
    
    
    try:
        dividend_yield_ratio = (dividends_per_share / market_price_per_share) * 100
    except ZeroDivisionError:
        dividend_yield_ratio = 0
    
    st.header("**Answer**")
    st.write("Dividend Yield Ratio = (Dividends Per Share/Market Price Per Share) * 100%")
    st.subheader("Dividend Yield Ratio: " + str(round(dividend_yield_ratio,2)) + "%")