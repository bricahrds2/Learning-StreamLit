import streamlit as st
import numpy as np
import pandas as pd
import requests
import json

st.title('Pokemon Data Visualization Tool')
st.divider()

def get_pokemon_data() -> dict:
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/ditto'
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data

pokemon_data = get_pokemon_data()

if pokemon_data:
    st.write('Pokemon Data Rectrieved Successfully')
    st.subheader(pokemon_data.get('name'))
    st.write(pokemon_data.get('weight'))
    st.image(pokemon_data.get('sprites').get('front_default'))
    