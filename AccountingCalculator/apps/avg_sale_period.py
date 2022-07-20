import streamlit as st

def app():
    st.title('Average Sale Period')
    
    colCOGS = st.columns(1)
    st.subheader("Cost of Goods Sold")
    cost_of_goods_sold = st.number_input("Enter the cost of goods sold($): ", min_value=0.0, format='%f')
    
    st.subheader("Average Inventory Balance")
    colInventoryLastYear, colInventoryThisYear = st.columns(2)  
    with colInventoryLastYear:
        inventory_last_year = st.number_input("Enter the total amount of inventory for last year($): ", min_value=0.0, format='%f')
    with colInventoryThisYear:
        inventory_this_year = st.number_input("Enter the total amount of inventory for this year($): ", min_value=0.0, format='%f')
        
    try:
        average_inventory_balance = (inventory_last_year + inventory_this_year) / 2
        inventory_turnover = cost_of_goods_sold / average_inventory_balance
        avg_sale_period = 365 / inventory_turnover
    except ZeroDivisionError:
        average_inventory_balance = 0
        inventory_turnover = 0
        avg_sale_period = 0
    
    st.markdown("Average Inventory Balance: " + str(round(average_inventory_balance,2)))
    st.markdown("Inventory Turnover: " + str(round(inventory_turnover,2)))
    
    st.header("**Answer**")
    st.write("Average Sale Period = 365 days / Inventory Turnover")
    st.subheader("Average Sale Period: " + str(round(avg_sale_period,2)))