import streamlit as st

# Force a clean mobile-friendly configuration
st.set_page_config(page_title="Gig Earnings Calc", page_icon="💰", layout="centered")

st.title("🚚 Job Fuel & Earnings")
st.write("Quickly check your actual take-home pay before accepting a job.")
st.markdown("---")

# Main screen inputs (Much easier to tap on mobile than opening a sidebar)
st.subheader("📊 Enter Details")

# Stacked numeric inputs with large tap targets
job_price = st.number_input("Job Offer Price ($)", min_value=0.0, value=150.0, step=5.0)
miles_to_job = st.number_input("Distance to Job (One-Way Miles)", min_value=0.0, value=25.0, step=1.0)
mpg = st.number_input("Vehicle MPG", min_value=0.1, value=18.0, step=0.5)
fuel_cost = st.number_input("Fuel Cost (per Gallon $)", min_value=0.0, value=3.75, step=0.05)

st.markdown("---")

# Math calculations
fuel_needed_1way = miles_to_job / mpg
fuel_cost_1way = fuel_needed_1way * fuel_cost
earnings_1way = job_price - fuel_cost_1way

fuel_needed_rt = (miles_to_job * 2) / mpg
fuel_cost_rt = fuel_needed_rt * fuel_cost
earnings_rt = job_price - fuel_cost_rt

# Display results sequentially (Optimal for vertical scrolling on mobile phones)
st.subheader("🏁 One-Way Trip Breakdown")
st.metric(label="Net Earnings", value=f"${earnings_1way:,.2f}")
st.caption(f"Fuel: {fuel_needed_1way:.2f} gal | Cost: ${fuel_cost_1way:.2f}")

st.markdown("---")

st.subheader("🔄 Round Trip Breakdown")
st.metric(label="Net Earnings", value=f"${earnings_rt:,.2f}")
st.caption(f"Fuel: {fuel_needed_rt:.2f} gal | Cost: ${fuel_cost_rt:.2f}")
