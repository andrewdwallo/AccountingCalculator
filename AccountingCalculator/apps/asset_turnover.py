import streamlit as st

def app():
    st.title('Total Asset Turnover')
    
    colSales = st.columns(1)
    st.subheader("Sales")
    sales = st.number_input("Enter the sales on account($): ", min_value=0.0, format='%f')
    
    st.subheader("Average Total Assets")
    colAssetsLastYear, colAssetsThisYear = st.columns(2)  
    with colAssetsLastYear:
        assets_last_year = st.number_input("Enter the total amount of assets for last year($): ", min_value=0.0, format='%f')
    with colAssetsThisYear:
        assets_this_year = st.number_input("Enter the total amount of assets for this year($): ", min_value=0.0, format='%f')
        
    try:
        average_total_assets = (assets_last_year + assets_this_year) / 2
        total_asset_turnover = sales / average_total_assets
    except ZeroDivisionError:
        average_total_assets = 0
        total_asset_turnover = 0
    
    st.markdown("Average Total Assets: " + str(round(average_total_assets,2)))
    
    st.header("**Answer**")
    st.write("Total Asset Turnover = Sales / Average Total Assets")
    st.subheader("Total Asset Turnover: " + str(round(total_asset_turnover,2)))