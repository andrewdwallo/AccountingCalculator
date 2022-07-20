import streamlit as st

def app():
    st.title('Book Value Per Share')
    
    st.subheader("Stockholders Equity")
    colStockholdersEquity = st.columns(1)
    stockholders_equity = st.number_input("Enter the total stockholders equity($): ", min_value=0.0, format='%f')
    
    st.subheader("Common Stock")
    colCommonStockThisYear = st.columns(1)
    common_stock_this_year = st.number_input("Enter the common stock for this year($): ", min_value=0.0, format='%f')
    
    
    try:
        book_value_per_share = stockholders_equity / common_stock_this_year
    except ZeroDivisionError:
        book_value_per_share = 0
    
    st.header("**Answer**")
    st.write("Book Value Per Share = Stockholder's Equity/Common Stock")
    st.subheader("Book Value Per Share: " + str(round(book_value_per_share,2)))