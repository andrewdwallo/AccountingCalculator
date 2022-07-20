import streamlit as st

def app():
    st.title('Total Product Cost')
    
    st.subheader("Variable Manufacturing Cost per unit")
    colDM, colDL, colVMOH = st.columns(3)  
    with colDM:
        dm = st.number_input("Enter the direct materials cost per unit($): ")
    with colDL:
        dl = st.number_input("Enter the direct labor cost per unit($): ")
    with colVMOH:
        vmoh = st.number_input("Enter the variable manufacturing cost per unit($): ")
    
    st.subheader("Total Variable Manufacturing Costs")
    colUnitsProduced = st.columns(1)  
    units_produced = st.number_input("Enter the number of units produced: ")
    
    st.subheader("Fixed Manufacturing Overhead Cost per unit")
    colFMOH = st.columns(1)
    fmoh = st.number_input("Enter the fixed manufacturing overhead cost per unit")
    
    try:
        vmoh_cost_per_unit = dm + dl + vmoh
        total_variable_manufacturing_cost = vmoh_cost_per_unit * units_produced
        fmoh_cost_per_unit = fmoh
        total_fixed_manufacturing_cost = fmoh_cost_per_unit * units_produced
        total_product_cost = total_variable_manufacturing_cost + total_fixed_manufacturing_cost
    except ZeroDivisionError:
        vmoh_cost_per_unit = 0
        total_variable_manufacturing_cost = 0
        fmoh_cost_per_unit = 0
        total_fixed_manufacturing_cost = 0
        total_product_cost = 0
    
    st.markdown("Variable Manufacturing Cost per unit: " + str(round(vmoh_cost_per_unit,2)))
    st.markdown("Total Variable Manufacturing Cost: " + str(round(total_variable_manufacturing_cost,2)))
    st.markdown("Average Fixed Manufacturing Cost per unit: " + str(round(fmoh_cost_per_unit,2)))
    st.markdown("Total Fixed Manufacturing Cost: " + str(round(total_fixed_manufacturing_cost,2)))
    
    st.header("**Answer**")
    st.write("Total Product (manufacturing) Cost = Total Variable Manufacturing Cost + Total Fixed Manufacturing Cost")
    st.subheader("Total Product (manufacturing) Cost: " + str(round(total_product_cost,2)))