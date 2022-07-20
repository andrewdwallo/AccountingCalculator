import streamlit as st

def app():
    st.title('Gross Margin Percentage')
    
    colSales = st.columns(1)
    st.subheader("Sales")
    sales = st.number_input("Enter the sales on account($): ", min_value=0.0, format='%f')
    
    colGM = st.columns(1) 
    st.subheader("Gross Margin") 
    gross_margin = st.number_input("Enter the gross margin($): ", min_value=0.0, format='%f')
        
    try:
        gross_margin_percentage = (gross_margin / sales) * 100
    except ZeroDivisionError:
        gross_margin_percentage = 0
    
    st.header("**Answer**")
    st.write("Gross Margin Percentage = (Gross Margin/Sales) * 100")
    st.subheader("Gross Margin Percentage: " + str(round(gross_margin_percentage,2)) + "%")