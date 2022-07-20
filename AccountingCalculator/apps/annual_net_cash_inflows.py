import streamlit as st

def app():
    st.title('Annual Net Cash Inflow')
    
    st.subheader("Net Operating Income")
    colNetIncome = st.columns(1)
    net_income = st.number_input("Enter the amount of net operating income($): ", min_value=0.0, format='%f')
    
    st.subheader("Depreciation")
    colDepreciation = st.columns(1)
    depreciation = st.number_input("Enter the amount of depreciation($): ", min_value=0.0, format='%f')
    
    
    try:
        annual_net_cash_inflow = net_income + depreciation
    except ZeroDivisionError:
        annual_net_cash_inflow = 0
    
    st.header("**Answer**")
    st.write("Annual Net Cash Inflow = Net Operating Income + Noncash Deduction for Depreciation")
    st.subheader("Annual Net Cash Inflow: " + str(round(annual_net_cash_inflow,2)))