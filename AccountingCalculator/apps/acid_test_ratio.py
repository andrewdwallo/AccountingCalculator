import streamlit as st

def app():
    st.title('Acid-test Ratio')
    
    st.subheader("Current Liabilities")
    colLiabilities = st.columns(1)
    liabilities = st.number_input("Enter the total current liabilities($): ", min_value=0.0, format='%f')
    
    st.subheader("Cash")
    colCash = st.columns(1)
    cash = st.number_input("Enter the total cash($): ", min_value=0.0, format='%f')
    
    st.subheader("Marketable Securities")
    colMarketableSecurities = st.columns(1)
    marketable_securities = st.number_input("Enter the total amount of marketable securities($): ", min_value=0.0, format='%f')
    
    st.subheader("Accounts Receivable")
    colAccountsReceivable = st.columns(1)
    accounts_receivable = st.number_input("Enter the total amount of accounts receivable($): ", min_value=0.0, format='%f')
    
    
    try:
        acid_test_ratio = (cash + marketable_securities + accounts_receivable) / liabilities
    except ZeroDivisionError:
        acid_test_ratio = 0
    
    st.header("**Answer**")
    st.write("Acid-test Ratio = (Cash + Marketable Securities + Accounts Receivable)/Liabilities")
    st.subheader("Acid-test Ratio: " + str(round(acid_test_ratio,2)))