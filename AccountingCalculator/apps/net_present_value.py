import streamlit as st
import re

def app():
    st.title('Net Present Value')
    
    cf0 = float(st.number_input('Enter initial investment amount:'))
    r = float(st.number_input('Enter discount rate:'))
    collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
    numbers = st.text_input("Enter cash inflows for each year separated by a comma (i.e 25000, 17000, 28000)")
    cashflows = collect_numbers(numbers)
    sum = 0
    t=0
       
    for cf in cashflows:
        t = t+1
        pv = float(cf)/(1+r)**t
        sum = sum + pv
    
    npv = sum - cf0
    
    st.header("**Answer**")
    st.subheader('Net Present Value: ' + str(round(npv,2)))