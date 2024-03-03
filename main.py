import streamlit as st
import numpy as np
import pandas as pd
import csv

st.title('Pokemon Data Visualization Tool')
st.divider()

#Load data from csv
@st.cache_data
def load_data():
    data = pd.read_csv('pokemon.csv')
    return data

data = load_data()

# Create dataframe 
df = pd.DataFrame(data)

# Display data
st.dataframe(df)
