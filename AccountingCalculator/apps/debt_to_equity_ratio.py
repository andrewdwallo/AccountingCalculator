import streamlit as st

def app():
    st.title('Debt-to-Equity Ratio')
    
    colLiabilities = st.columns(1) 
    st.subheader("Total Liabilities") 
    liabilities = st.number_input("Enter the total liabilities($): ", min_value=0.0, format='%f')
    
    colEquity = st.columns(1)
    st.subheader("Total Stockholder's Equity")
    equity = st.number_input("Enter the total stockholder's equity($): ", min_value=0.0, format='%f')
    
    try:
        debt_to_equity_ratio = liabilities / equity
    except ZeroDivisionError:
        debt_to_equity_ratio = 0
    
    st.header("**Answer**")
    st.write("Debt-to-Equity Ratio = Total Liabilities/Stockholder's Equity")
    st.subheader("Debt-to-Equity Ratio: " + str(round(debt_to_equity_ratio,2)))