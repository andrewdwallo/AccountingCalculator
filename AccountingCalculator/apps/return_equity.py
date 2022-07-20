import streamlit as st

def app():
    st.title('Return on Equity')
    
    colNetIncome = st.columns(1) 
    st.subheader("Net Income") 
    net_income = st.number_input("Enter the net income($): ", min_value=0.0, format='%f')
    
    st.subheader("Average Stockholder's Equity")
    colEquityLastYear, colEquityThisYear = st.columns(2)  
    with colEquityLastYear:
        equity_last_year = st.number_input("Enter the total amount of stockholder's equity for last year($): ", min_value=0.0, format='%f')
    with colEquityThisYear:
        equity_this_year = st.number_input("Enter the total amount of stockholder's equity for this year($): ", min_value=0.0, format='%f')
    

    try:
        average_stockholders_equity = (equity_last_year + equity_this_year) / 2
        return_on_equity = (net_income / average_stockholders_equity) * 100 
    except ZeroDivisionError:
        average_stockholders_equity = 0
        return_on_equity = 0
    
    st.markdown("Average Stockholder's Equity: " + str(round(average_stockholders_equity,2)))
    
    st.header("**Answer**")
    st.write("Return on Equity = (Net Income/Average Stockholder's Equity) * 100%")
    st.subheader("Return on Equity: " + str(round(return_on_equity,2)) + "%")