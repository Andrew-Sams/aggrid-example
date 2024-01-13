import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
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

def generate_data(n=5):
    return pd.DataFrame({
        "Input Name": [f"Input{i+1}" for i in range(n)],
        "Low": np.random.randint(10, 20, size=n),
        "Estimate": np.random.randint(20, 30, size=n),
        "High": np.random.randint(30, 40, size=n),
        "Data Source": [f"Source{i+1}" for i in range(n)]
    })

def main():
    st.title('Editable Data Table with ag-Grid')

    # Using Streamlit's session state to store the dataframe
    if 'df' not in st.session_state:
        st.session_state.df = generate_data()

    # Grid options builder
    gb = GridOptionsBuilder.from_dataframe(st.session_state.df)
    gb.configure_default_column(editable=True, resizable=True, autoHeight=True)
    gb.configure_grid_options(enableRangeSelection=True)

    grid_options = gb.build()

    # Displaying the grid
    grid_response = AgGrid(
        st.session_state.df, 
        gridOptions=grid_options,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        fit_columns_on_grid_load=True,
        height=300,
        width='100%',
        allow_unsafe_jscode=True
    )

    # Update session state
    st.session_state.df = grid_response['data']

    # Slider for the number of simulations
    num_simulations = st.slider("Number of Simulations", 1, 10000, 1000)

    # Button to run the simulation
    # Button to run the simulation
    if st.button("Run Simulation"):
        updated_df = pd.DataFrame(st.session_state.df)
        simulation_results = []
    
        for _ in range(num_simulations):
            simulated_values = [asymmetrical_gaussian(row['Low'], row['Estimate'], row['High']) for _, row in updated_df.iterrows()]
            simulation_results.append(sum(simulated_values))
    
        # Plotting the results as a histogram
        plt.hist(simulation_results, bins=30, edgecolor='black')
        st.pyplot(plt)

        # Plotting the results
        plt.hist(simulation_results, bins=30, edgecolor='black')
        st.pyplot(plt)

    # Display updated data
    st.write("### Updated Data")
    st.dataframe(st.session_state.df)

if __name__ == "__main__":
    main()

