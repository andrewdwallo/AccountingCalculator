import streamlit as st

def app():
    st.title('Current Ratio')
    
    st.subheader("Current Assets")
    colAssets = st.columns(1)
    assets = st.number_input("Enter the total current assets($): ", min_value=0.0, format='%f')
    
    st.subheader("Current Liabilities")
    colLiabilities = st.columns(1)
    liabilities = st.number_input("Enter the total current liabilities($): ", min_value=0.0, format='%f')
    
    
    try:
        current_ratio = assets / liabilities
    except ZeroDivisionError:
        current_ratio = 0
    
    st.header("**Answer**")
    st.write("Current Ratio = Assets/Liabilities")
    st.subheader("Current Ratio: " + str(round(current_ratio,2)))