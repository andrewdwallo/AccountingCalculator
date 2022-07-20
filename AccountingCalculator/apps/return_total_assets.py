import streamlit as st

def app():
    st.title('Return on Total Assets')
    
    colNetIncome = st.columns(1) 
    st.subheader("Net Income") 
    net_income = st.number_input("Enter the net income($): ", min_value=0.0, format='%f')
    
    colInterestExpense = st.columns(1)
    st.subheader("Interest Expense")
    interest_expense = st.number_input("Enter the interest expense($): ", min_value=0.0, format='%f')
    
    colTaxRate = st.columns(1)
    st.subheader("Tax Rate")
    tax_rate = st.number_input("Enter the tax rate (in decimal form): ", min_value=0.0, format='%f')
    
    st.subheader("Average Total Assets")
    colAssetsLastYear, colAssetsThisYear = st.columns(2)  
    with colAssetsLastYear:
        assets_last_year = st.number_input("Enter the total amount of assets for last year($): ", min_value=0.0, format='%f')
    with colAssetsThisYear:
        assets_this_year = st.number_input("Enter the total amount of assets for this year($): ", min_value=0.0, format='%f')
    
    
    try:
        interest_expense_rate = interest_expense * (1-tax_rate)
        average_total_assets = (assets_last_year + assets_this_year) / 2
        return_on_total_assets = ((net_income + interest_expense_rate) / average_total_assets) * 100
    except ZeroDivisionError:
        interest_expense_rate = 0
        average_total_assets = 0
        return_on_total_assets = 0
    
    st.markdown("Interest Expense Rate: " + str(round(interest_expense_rate,2)))
    st.markdown("Average Total Assets: " + str(round(average_total_assets,2)))
    
    st.header("**Answer**")
    st.write("Return on Total Assets = ((Net Income + Interest Expense Rate) / Average Total Assets) * 100%")
    st.subheader("Return on Total Assets: " + str(round(return_on_total_assets,2)) + "%")