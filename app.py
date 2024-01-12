import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

# Function to generate asymmetrical Gaussian distribution
def asymmetrical_gaussian(low, estimate, high, size=1):
    sigma = (high - low) / 6
    mean = estimate
    a, b = (low - mean) / sigma, (high - mean) / sigma
    return truncnorm.rvs(a, b, loc=mean, scale=sigma, size=size)

# Sample data
data = {
    "Input Name": ["Input1", "Input2", "Input3", "Input4", "Input5"],
    "Low": [10, 20, 30, 40, 50],
    "Estimate": [15, 25, 35, 45, 55],
    "High": [20, 30, 40, 50, 60],
    "Data Source": ["Source1", "Source2", "Source3", "Source4", "Source5"]
}
df = pd.DataFrame(data)

# Streamlit layout
st.title("Streamlit AgGrid Demo")

# Data table for inputs
st.sidebar.header("Input Data")
grid_response = AgGrid(df, editable=True)

# Slider for the number of simulations
num_simulations = st.sidebar.slider("Number of Simulations", 1, 10000, 1000)

# Button to run the simulation
if st.sidebar.button("Run Simulation"):
    updated_df = pd.DataFrame(grid_response['data'])
    simulation_results = []

    for _ in range(num_simulations):
        simulated_values = [asymmetrical_gaussian(row['Low'], row['Estimate'], row['High']) for _, row in updated_df.iterrows()]
        simulation_results.append(sum(simulated_values))

    # Plotting the results
    plt.hist(simulation_results, bins=30, edgecolor='black')
    st.pyplot(plt)
