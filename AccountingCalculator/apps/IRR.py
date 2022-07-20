import streamlit as st

def app():
    st.title('Internal Rate of Return')

    st.write('To calculate the Internal Rate of Return, you must first determine the Present Value Factor')
    
    colInitialInvestment2, colNetAnnualCashFlow = st.columns(2)
    
    with colInitialInvestment2:
        InitialInvestment2 = st.number_input("Enter the Initial Investment($): ", min_value=0.0, format='%f')
    with colNetAnnualCashFlow:
        NetAnnualCashFlow = st.number_input("Enter the net annual cash flow($): ", min_value=0.0, format='%f')
        
    try:
        present_value_factor = InitialInvestment2 / NetAnnualCashFlow
    except ZeroDivisionError:
        present_value_factor = 0
    
    st.header("**Answer**")
    st.subheader("Present Value Factor: " + str(round(present_value_factor,2)))
    
    st.write('Take the Useful Life (periods, years, months, etx) to determine the row from where you need to find the value that is closest to the Present Value Factor')
    
    st.write('As an example, if the investment had a Useful Life of 5 Years with a Present Value Factor of 3.8961,... then the Internal Rate of Return would be 9%')
    
    
    
    
