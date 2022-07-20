import streamlit as st

def app():
    st.title('Net Profit Margin Percentage')
    
    colSales = st.columns(1)
    st.subheader("Sales")
    sales = st.number_input("Enter the sales on account($): ", min_value=0.0, format='%f')
    
    colNetIncome= st.columns(1) 
    st.subheader("Net Income") 
    net_income = st.number_input("Enter the net income($): ", min_value=0.0, format='%f')
        
    try:
        profit_margin_percentage = (net_income / sales) * 100
    except ZeroDivisionError:
        profit_margin_percentage = 0
    
    st.header("**Answer**")
    st.write("Net Profit Margin Percentage = (Net Income/Sales) * 100")
    st.subheader("Net Profit Margin Percentage: " + str(round(profit_margin_percentage,2)) + "%")