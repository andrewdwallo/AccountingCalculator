import streamlit as st

def app():
    st.title('Times Interest Earned Ratio')
    
    colNetIncome = st.columns(1) 
    st.subheader("Net Operating Income") 
    net_income = st.number_input("Enter the net operating income before interest expense and income taxes($): ", min_value=0.0, format='%f')
    
    colInterestExpense = st.columns(1)
    st.subheader("Interest Expense")
    interest_expense = st.number_input("Enter the interest expense($): ", min_value=0.0, format='%f')
    
    try:
        times_interest_earned_ratio = net_income / interest_expense
    except ZeroDivisionError:
        times_interest_earned_ratio = 0
    
    st.header("**Answer**")
    st.write("Times Interest Earned Ratio = Earnings before interest expense and income taxes/Interest Expense")
    st.subheader("Times Interest Earned Ratio: " + str(round(times_interest_earned_ratio,2)))