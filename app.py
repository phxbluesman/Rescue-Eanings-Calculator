import streamlit as st

# Compact page setup
st.set_page_config(page_title="Gig Calc", page_icon="💰", layout="centered")

st.title("💰 Gig Fuel & Earnings")
st.caption("Quickly calculate true net pay on the go.")

# Use a form to batch inputs and prevent laggy mobile reruns
with st.form("calc_form"):
    job_price = st.number_input("Job Offer Price ($)", min_value=0.0, value=17.50, step=1.75)
    miles_to_job = st.number_input("One-Way Miles to Job", min_value=0.0, value=10.0, step=0.1)
    
    # Put vehicle stats side-by-side to save vertical scrolling space
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        mpg = st.number_input("Vehicle MPG", min_value=0.1, value=22.0, step=0.1)
    with col_v2:
        fuel_cost = st.number_input("Fuel $/Gal", min_value=0.0, value=4.39, step=0.01)
        
    submit = st.form_submit_button("Calculate Earnings", use_container_width=True)

# Only run math and display results after clicking the button
if submit:
    # Calculations
    cost_1way = (miles_to_job / mpg) * fuel_cost
    cost_rt = ((miles_to_job * 2) / mpg) * fuel_cost
    
    net_1way = job_price - cost_1way
    net_rt = job_price - cost_rt

    st.markdown("---")
    
    # Clean, high-contrast display blocks for small screens
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.metric(label="🏁 One-Way Net", value=f"${net_1way:,.2f}")
        st.caption(f"Fuel Cost: ${cost_1way:.2f}")
        
    with res_col2:
        st.metric(label="🔄 Round Trip Net", value=f"${net_rt:,.2f}")
        st.caption(f"Fuel Cost: ${cost_rt:.2f}")
