import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import pandas as pd
import numpy as np

@st.cache(allow_output_mutation=True)
def generate_data(n=100):
    return pd.DataFrame({
        'Category': np.random.choice(['A', 'B', 'C'], n),
        'Value': np.random.rand(n)
    })

def main():
    st.title('Editable Data Table with ag-Grid')

    df = generate_data()

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_grid_options(editable=True)
    grid_options = gb.build()

    grid_response = AgGrid(
        df, 
        gridOptions=grid_options,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        fit_columns_on_grid_load=True,
    )

    updated_df = grid_response['data']
    st.write("### Updated Data")
    st.dataframe(updated_df)

if __name__ == "__main__":
    main()
