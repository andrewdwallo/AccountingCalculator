import streamlit as st

def app():
    st.title('Accounts Receivable Turnover')
    
    colSales = st.columns(1)
    st.subheader("Sales")
    sales = st.number_input("Enter the sales on account($): ", min_value=0.0, format='%f')
    
    st.subheader("Average Accounts Receivable")
    colReceivablesLastYear, colReceivablesThisYear = st.columns(2)  
    with colReceivablesLastYear:
        receivables_last_year = st.number_input("Enter the total amount of accounts receivable for last year($): ", min_value=0.0, format='%f')
    with colReceivablesThisYear:
        receivables_this_year = st.number_input("Enter the total amount of accounts receivable for this year($): ", min_value=0.0, format='%f')
        
    try:
        average_accounts_receivable = (receivables_last_year + receivables_this_year) / 2
        accounts_receivable_turnover = sales / average_accounts_receivable
    except ZeroDivisionError:
        average_accounts_receivable = 0
        accounts_receivable_turnover = 0
    
    st.markdown("Average Accounts Receivable: " + str(round(average_accounts_receivable,2)))
    
    st.header("**Answer**")
    st.write("Accounts Receivable Turnover = Sales / Average Accounts Receivable")
    st.subheader("Accounts Receivable Turnover: " + str(round(accounts_receivable_turnover,2)))