import streamlit as st

def app():
    st.title('Total Period Cost')
    
    st.subheader("Variable Selling and Administrative Expense per unit")
    colSalesCommissions, colVariableAdministrativeExpense = st.columns(2)  
    with colSalesCommissions:
        sales_commissions = st.number_input("Enter the sales commissions cost per unit($): ")
    with colVariableAdministrativeExpense:
        variable_administrative_expense = st.number_input("Enter the variable administrative expense per unit($): ")
    
    st.subheader("Total Variable Selling and Administrative Expense")
    colUnitsSold = st.columns(1)  
    units_sold = st.number_input("Enter the number of units sold: ")
    
    st.subheader("Average Fixed Selling and Administrative Expense per unit")
    colFixedSelling, colFixedAdministrative = st.columns(2)
    with colFixedSelling:
        fixed_selling_expense_per_unit = st.number_input("Enter the fixed selling expense per unit: ")
    with colFixedAdministrative:
        fixed_administrative_expense_per_unit = st.number_input("Enter the fixed administrative expense per unit: ")
    
    
    try:
        variable_selling_and_administrative_per_unit = sales_commissions + variable_administrative_expense
        total_variable_selling_and_administrative_expense = variable_selling_and_administrative_per_unit * units_sold
        avg_fixed_selling_and_administrative_expense_per_unit = fixed_selling_expense_per_unit + fixed_administrative_expense_per_unit
        total_fixed_selling_and_administrative_expense = avg_fixed_selling_and_administrative_expense_per_unit * units_sold
        total_period_cost = total_variable_selling_and_administrative_expense + total_fixed_selling_and_administrative_expense
    except ZeroDivisionError:
        variable_selling_and_administrative_per_unit = 0
        total_variable_selling_and_administrative_expense = 0
        avg_fixed_selling_and_administrative_expense_per_unit = 0
        total_fixed_selling_and_administrative_expense = 0
        total_period_cost = 0
    
    st.markdown("Variable Selling and Administrative Expense per unit: " + str(round(variable_selling_and_administrative_per_unit,2)))
    st.markdown("Total Variable Selling and Administrative Expense: " + str(round(total_variable_selling_and_administrative_expense,2)))
    st.markdown("Average Fixed Selling and Administrative Expense per unit: " + str(round(avg_fixed_selling_and_administrative_expense_per_unit,2)))
    st.markdown("Total Fixed Selling and Administrative Expense: " + str(round(total_fixed_selling_and_administrative_expense,2)))
    
    st.header("**Answer**")
    st.write("Total Period (manufacturing) Cost = Total Variable Selling and Administrative Expense + Total Fixed Selling and Administrative Expense")
    st.subheader("Total Period (manufacturing) Cost: " + str(round(total_period_cost,2)))