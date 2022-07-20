import streamlit as st

def app():
    st.title('Simple Rate of Return Method')
    
    colNewPurchase, colOldAnnualOperating, colNewAnnualOperating, colSalvageValue, colYears = st.columns(5)
    
    with colNewPurchase:
        NewPurchase = st.number_input("Enter the amount of money for new purchase considered($): ", min_value=0.0, format='%f')
        
    with colOldAnnualOperating:
        OldAnnualOperating = st.number_input("Enter the annual operating cost of old purchase($): ", min_value=0.0, format='%f')
        
    with colNewAnnualOperating:
        NewAnnualOperating = st.number_input("Enter the annual operating cost of new purchase($): ", min_value=0.0, format='%f')
    
    with colSalvageValue:
        SalvageValue = st.number_input("Enter the salvage value of old purchase($): ", min_value=0.0, format='%f')
    
    with colYears:
        Years = st.number_input("Enter the useful life of new purchase($): ", min_value=0.0, format='%f')
    
    try:
        depreciation_expense = NewPurchase / Years
        incremental_operating_income = OldAnnualOperating - NewAnnualOperating - depreciation_expense
        initial_investment = NewPurchase - SalvageValue
        simple_rate_of_return = (incremental_operating_income / initial_investment) * 100
    except ZeroDivisionError:
        depreciation_expense = 0
        incremental_operating_income = 0
        initial_investment = 0
        simple_rate_of_return = 0
        
        
    st.header("**Answers**")
    st.subheader("Depreciation Expense: " + str(round(depreciation_expense,2)))
    st.subheader("Incremental Net Operating Income: " + str(round(incremental_operating_income,2)))
    st.subheader("Initial Investment: " + str(round(initial_investment,2)))
    st.subheader("Simple Rate of Return: " + str(round(simple_rate_of_return,3)) + "%")
    
