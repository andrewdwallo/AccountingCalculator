import streamlit as st
import re
import functools as ft

def app():
    st.title('Payback Period')
    
    inv = float(st.number_input('Enter initial investment amount:'))
    
    collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
    numbers = st.text_input("Enter cash inflows for each year separated by a comma (i.e 25000, 17000, 28000)")
    cash_flow = collect_numbers(numbers)
    disc_cash_flow = [x for x in range(0,len(cash_flow))]
    disc_rate = float(st.number_input('Enter discount rate:'))
    dif = []
    cumulative = []
    i = 0
    while i<len(cash_flow):
        disc_cash_flow[i] = cash_flow[i]/pow(1+(disc_rate/100),i+1)
        dif.append(inv-ft.reduce(lambda x,y:x+y,disc_cash_flow))
        cumulative.append(ft.reduce(lambda x,y:x+y,disc_cash_flow))
        i += 1
        
    dif = list(map(lambda x:x>=0,dif))
    def minimum(lst):
        try:
            i = lst.index(min(lst))
            return i + 1
        except ValueError:
            i = 0
    
    try:
        year = minimum(dif)+(inv-cumulative[minimum(dif)-1])/disc_cash_flow[minimum(dif)-1]
    except TypeError:
        year = 0
    
    st.header("**Answer**")
    st.write("Payback Period = Years Before Breakeven + (Unrecovered Amount/Cash Inflow in Recovery Year)")
    st.subheader('Payback Period: {} years'.format(round(year,2)))