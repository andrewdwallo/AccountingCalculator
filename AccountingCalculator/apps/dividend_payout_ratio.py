import streamlit as st

def app():
    st.title('Dividend Payout Ratio')
    
    colNetIncome = st.columns(1)
    st.subheader("Net Income")
    net_income = st.number_input("Enter the net income($): ", min_value=0.0, format='%f')
    
    st.subheader("Average Common Shares")
    colStockLastYear, colStockThisYear = st.columns(2)  
    with colStockLastYear:
        stock_last_year = st.number_input("Enter the common stock for last year($): ", min_value=0.0, format='%f')
    with colStockThisYear:
        stock_this_year = st.number_input("Enter the common stock for this year($): ", min_value=0.0, format='%f')
    
    st.subheader("Dividends Per Share")
    colDividendsPerShare = st.columns(1)
    dividends_per_share = st.number_input("Enter the dividends per share of common stock($): ", min_value=0.0, format='%f')
    
    
    try:
        average_common_shares = (stock_last_year + stock_this_year) / 2
        earnings_per_share = net_income / average_common_shares
        dividend_payout_ratio = (dividends_per_share / earnings_per_share) * 100
    except ZeroDivisionError:
        average_common_shares = 0
        earnings_per_share = 0
        dividend_payout_ratio = 0
    
    st.markdown("Average Common Shares: " + str(round(average_common_shares,2)))
    st.markdown("Earnings Per Share: " + str(round(earnings_per_share,2)))
    
    st.header("**Answer**")
    st.write("Dividend Payout Ratio = (Dividends Per Share/Earnings Per Share) * 100%")
    st.subheader("Dividend Payout Ratio: " + str(round(dividend_payout_ratio,2)) + "%")