import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import pandas as pd
import numpy as np

def generate_data(n=100):
    return pd.DataFrame({
        'Category': np.random.choice(['A', 'B', 'C'], n),
        'Value': np.random.rand(n)
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

    # Display updated data
    st.write("### Updated Data")
    st.dataframe(st.session_state.df)

if __name__ == "__main__":
    main()
