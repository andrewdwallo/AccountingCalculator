import streamlit as st

def app():
    st.title('Operating Cycle')
    
    colSales = st.columns(1)
    st.subheader("Sales")
    sales = st.number_input("Enter the sales on account($): ", min_value=0.0, format='%f')
    
    colCOGS = st.columns(1)
    st.subheader("Cost of Goods Sold")
    cost_of_goods_sold = st.number_input("Enter the cost of goods sold($): ", min_value=0.0, format='%f')
    
    st.subheader("Average Accounts Receivable")
    colReceivablesLastYear, colReceivablesThisYear = st.columns(2)  
    with colReceivablesLastYear:
        receivables_last_year = st.number_input("Enter the total amount of accounts receivable for last year($): ", min_value=0.0, format='%f')
    with colReceivablesThisYear:
        receivables_this_year = st.number_input("Enter the total amount of accounts receivable for this year($): ", min_value=0.0, format='%f')
    
    st.subheader("Average Inventory Balance")
    colInventoryLastYear, colInventoryThisYear = st.columns(2)  
    with colInventoryLastYear:
        inventory_last_year = st.number_input("Enter the total amount of inventory for last year($): ", min_value=0.0, format='%f')
    with colInventoryThisYear:
        inventory_this_year = st.number_input("Enter the total amount of inventory for this year($): ", min_value=0.0, format='%f')
    
    
    try:
        average_accounts_receivable = (receivables_last_year + receivables_this_year) / 2
        average_inventory_balance = (inventory_last_year + inventory_this_year) / 2
        accounts_receivable_turnover = sales / average_accounts_receivable
        inventory_turnover = cost_of_goods_sold / average_inventory_balance
        avg_collection_period - 365 / accounts_receivable_turnover
        avg_sale_period = 365 / inventory_turnover
        operating_cycle = avg_collection_period + avg_sale_period
    except ZeroDivisionError:
        average_accounts_receivable = 0
        average_inventory_balance = 0
        accounts_receivable_turnover = 0
        inventory_turnover = 0
        avg_collection_period = 0
        avg_sale_period = 0
        operating_cycle = 0
    
    st.markdown("Average Accounts Receivable: " + str(round(average_accounts_receivable,2)))
    st.markdown("Accounts Receivable Turnover: " + str(round(accounts_receivable_turnover,2)))
    st.markdown("Average Inventory Balance: " + str(round(average_inventory_balance,2)))
    st.markdown("Inventory Turnover: " + str(round(inventory_turnover,2)))
    st.markdown("Average Collection Period: " + str(round(avg_collection_period,2)))
    st.markdown("Average Sale Period: " + str(round(avg_sale_period,2)))
    
    st.header("**Answer**")
    st.write("Operating Cycle = Average Collection Period + Average Sale Period")
    st.subheader("Operating Cycle: " + str(round(operating_cycle,2)))