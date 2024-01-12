import streamlit as st
import pandas as pd
import numpy as np

@st.cache(allow_output_mutation=True)
def generate_data(n=100):
    return pd.DataFrame({
        'ID': np.arange(n),
        'Category': np.random.choice(['A', 'B', 'C'], n),
        'Value': np.random.rand(n)
    })

def update_data(df, row_id, new_value):
    df.loc[df['ID'] == row_id, 'Value'] = new_value
    return df

def main():
    st.title('Editable Data Table with Streamlit')

    df = generate_data()

    st.write("### Original Data")
    st.dataframe(df)

    st.write("### Edit Data")
    row_id = st.number_input("Enter Row ID to Edit", min_value=0, max_value=df['ID'].max(), step=1)
    new_value = st.number_input("Enter New Value", min_value=0.0, max_value=1.0)
    
    if st.button("Update Data"):
        df = update_data(df, row_id, new_value)
        st.success("Data Updated")

    st.write("### Updated Data")
    st.dataframe(df)

if __name__ == "__main__":
    main()
