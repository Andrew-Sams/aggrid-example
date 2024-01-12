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

    # Explicit column definitions
    column_defs = [
        {'headerName': 'Category', 'field': 'Category', 'editable': True},
        {'headerName': 'Value', 'field': 'Value', 'editable': True}
    ]

    # Grid options builder
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(editable=True)
    gb.configure_column("Category", editable=True)
    gb.configure_column("Value", editable=True)
    gb.configure_grid_options(columnDefs=column_defs)

    grid_options = gb.build()

    # Displaying the grid
    grid_response = AgGrid(
        df, 
        gridOptions=grid_options,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        fit_columns_on_grid_load=True,
        height=300,
        width='100%'
    )

    # Retrieving updated data
    updated_df = grid_response['data']
    st.write("### Updated Data")
    st.dataframe(updated_df)

if __name__ == "__main__":
    main()
