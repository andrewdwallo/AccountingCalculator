import streamlit as st

def app():
    st.title('Price Earnings Ratio')
    
    colNetIncome = st.columns(1)
    st.subheader("Net Income")
    net_income = st.number_input("Enter the net income($): ", min_value=0.0, format='%f')
    
    st.subheader("Average Common Shares")
    colStockLastYear, colStockThisYear = st.columns(2)  
    with colStockLastYear:
        stock_last_year = st.number_input("Enter the common stock for last year($): ", min_value=0.0, format='%f')
    with colStockThisYear:
        stock_this_year = st.number_input("Enter the common stock for this year($): ", min_value=0.0, format='%f')
    
    st.subheader("Market Price Per Share")
    colMarketPricePerShare = st.columns(1)
    market_price_per_share = st.number_input("Enter the market value of the company's common stock at the end of the year (Market Price Per Share)($): ", min_value=0.0, format='%f')
    
    
    try:
        average_common_shares = (stock_last_year + stock_this_year) / 2
        earnings_per_share = net_income / average_common_shares
        price_earnings_ratio = market_price_per_share / earnings_per_share
    except ZeroDivisionError:
        average_common_shares = 0
        earnings_per_share = 0
        price_earnings_ratio = 0
    
    st.markdown("Average Common Shares: " + str(round(average_common_shares,2)))
    st.markdown("Earnings Per Share: " + str(round(earnings_per_share,2)))
    
    st.header("**Answer**")
    st.write("Price Earnings Ratio = Market Price Per Share/Earnings Per Share")
    st.subheader("Price Earnings Ratio: " + str(round(price_earnings_ratio,2)))