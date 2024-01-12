import streamlit as st
import pandas as pd
import numpy as np

# Sample data generation
@st.cache
def generate_data(n=100):
    return pd.DataFrame({
        'Category': np.random.choice(['A', 'B', 'C'], n),
        'Value': np.random.rand(n)
    })

def main():
    st.title('Simple Aggregation Table with Streamlit')

    df = generate_data()

    st.write("### Original Data")
    st.dataframe(df)

    st.write("### Aggregated Data")
    agg_df = df.groupby('Category').agg(Total_Value=('Value', 'sum'),
                                        Average_Value=('Value', 'mean'),
                                        Count=('Value', 'count'))
    st.dataframe(agg_df)

if __name__ == "__main__":
    main()
