import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
from annotated_text import annotated_text

st.title('Pokemon Data Visualization Tool')
st.divider()

colours = {
    'normal': "#A8A77A",
	'fire': "#EE8130",
	'water': "#6390F0",
    'electric': '#F7D02C',
	'grass': '#7AC74C',
	'ice': '#96D9D6',
	'fighting': '#C22E28',
	'poison': '#A33EA1',
	'ground': '#E2BF65',
	'flying': '#A98FF3',
	'psychic': '#F95587',
	'bug': '#A6B91A',
	'rock': '#B6A136',
	'ghost': '#735797',
	'dragon': '#6F35FC',
	'dark': '#705746',
	'steel': '#B7B7CE',
	'fairy': '#D685AD'
}


def get_pokemon_data() -> dict:
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/ditto'
        response = requests.get(url)
        data = response.json()
        st.write('Pokemon Data Rectrieved Successfully')
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data

pokemon_data = get_pokemon_data()

if pokemon_data:
    st.header(pokemon_data.get('name').capitalize())
    st.image(pokemon_data.get('sprites').get('front_default'))
    st.write('Pokemon Weight',pokemon_data.get('weight'))
    pokemon_type = pokemon_data.get("types")[0].get("type").get("name")
    annotated_text(
        (pokemon_type,'', colours[pokemon_type])
    )
    