import streamlit as st

def app():
    st.title('Working Capital')
    
    st.subheader("Current Assets")
    colAssets = st.columns(1)
    assets = st.number_input("Enter the total current assets($): ", min_value=0.0, format='%f')
    
    st.subheader("Current Liabilities")
    colLiabilities = st.columns(1)
    liabilities = st.number_input("Enter the total current liabilities($): ", min_value=0.0, format='%f')
    
    
    try:
        working_capital = assets - liabilities
    except ZeroDivisionError:
        working_capital = 0
    
    st.header("**Answer**")
    st.write("Working Capital = Assets - Liabilities")
    st.subheader("Working Capital: " + str(round(working_capital,2)))