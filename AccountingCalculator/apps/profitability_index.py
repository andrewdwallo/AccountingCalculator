import streamlit as st

def app():
    st.title('Profitability Index')
    
    colPVNetAnnualCashFlow, colInitialInvestment = st.columns(2)
    
    with colPVNetAnnualCashFlow:
        PVNetAnnualCashFlow = st.number_input("Enter the present value of net annual cash flows($): ", min_value=0.0, format='%f')
        
    with colInitialInvestment:
        InitialInvestment = st.number_input("Enter the initial investment($): ", min_value=0.0, format='%f')
        
    try:
        profitability_index = PVNetAnnualCashFlow / InitialInvestment
    except ZeroDivisionError:
        profitability_index = 0
        
    st.header("**Answer**")
    st.subheader("Profitability Index: " + str(round(profitability_index,2)))