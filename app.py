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

    df = generate_data()

    # Grid options builder
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(editable=True, resizable=True, autoHeight=True)
    gb.configure_grid_options(enableRangeSelection=True)

    grid_options = gb.build()

    # Displaying the grid
    grid_response = AgGrid(
        df, 
        gridOptions=grid_options,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        fit_columns_on_grid_load=True,
        height=300,
        width='100%',
        allow_unsafe_jscode=True
    )

    # Retrieving updated data
    updated_df = grid_response['data']
    st.write("### Updated Data")
    st.dataframe(updated_df)

if __name__ == "__main__":
    main()
