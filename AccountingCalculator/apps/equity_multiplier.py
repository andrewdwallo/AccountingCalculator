import streamlit as st

def app():
    st.title('Equity Multiplier')
    
    st.subheader("Average Total Assets")
    colAssetsLastYear, colAssetsThisYear = st.columns(2)  
    with colAssetsLastYear:
        assets_last_year = st.number_input("Enter the total amount of assets for last year($): ", min_value=0.0, format='%f')
    with colAssetsThisYear:
        assets_this_year = st.number_input("Enter the total amount of assets for this year($): ", min_value=0.0, format='%f')
    
    st.subheader("Average Stockholder's Equity")
    colEquityLastYear, colEquityThisYear = st.columns(2)  
    with colEquityLastYear:
        equity_last_year = st.number_input("Enter the total amount of stockholder's equity for last year($): ", min_value=0.0, format='%f')
    with colEquityThisYear:
        equity_this_year = st.number_input("Enter the total amount of stockholder's equity for this year($): ", min_value=0.0, format='%f')
    
    
    try:
        average_total_assets = (assets_last_year + assets_this_year) / 2
        average_stockholders_equity = (equity_last_year + equity_this_year) / 2
        equity_multiplier = average_total_assets / average_stockholders_equity
    except ZeroDivisionError:
        average_total_assets = 0
        average_stockholders_equity = 0
        equity_multiplier = 0
    
    st.markdown("Average Total Assets: " + str(round(average_total_assets,2)))
    st.markdown("Average Stockholder's Equity: " + str(round(average_stockholders_equity,2)))
    
    st.header("**Answer**")
    st.write("Equity Multiplier = Average Total Assets/Average Stockholder's Equity")
    st.subheader("Equity Multiplier: " + str(round(equity_multiplier,2)))