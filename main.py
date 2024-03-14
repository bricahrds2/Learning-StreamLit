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


randomnumber = str(np.random.randint(1, 1000))
randomnumber2 = str(np.random.randint(1, 1000))

#Fetch random pokemon name
def get_random_pokemon(number:int) -> str:
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/'+number
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data.get('name')

pokemon_name = get_random_pokemon(randomnumber)
pokemon_name_2 = get_random_pokemon(randomnumber2)

def get_pokemon_data(pokemonname) -> dict:
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/'+pokemonname
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        st.write(f'Error: {e}')
        data = None
    return data

pokemon_data = get_pokemon_data(pokemon_name)
pokemon_data_2 = get_pokemon_data(pokemon_name_2)

if pokemon_data and pokemon_data_2:
    col1, col2 = st.columns(2)

with col1:
    st.write('Pokemon Data Retrieved Successfully')
    st.header(pokemon_data.get('name').capitalize())
    st.image(pokemon_data.get('sprites').get('front_default'))
    st.write('Pokemon Weight',pokemon_data.get('weight'))
    pokemon_type = pokemon_data.get("types")[0].get("type").get("name")
    annotated_text(
        (pokemon_type,'', colours[pokemon_type])
    )
with col2:
    st.write('Pokemon Data Retrieved Successfully')
    st.header(pokemon_data_2.get('name').capitalize())
    st.image(pokemon_data_2.get('sprites').get('front_default'))
    st.write('Pokemon Weight',pokemon_data_2.get('weight'))
    pokemon_type = pokemon_data_2.get("types")[0].get("type").get("name")
    annotated_text(
        (pokemon_type,'', colours[pokemon_type])
    )

comparison = {
    pokemon_data.get('name').capitalize(): {
        'hp': pokemon_data.get('stats')[0].get('base_stat'),
        'attack': pokemon_data.get('stats')[1].get('base_stat'),
        'defense': pokemon_data.get('stats')[2].get('base_stat'),
        'special_attack': pokemon_data.get('stats')[3].get('base_stat'),
        'special_defense': pokemon_data.get('stats')[4].get('base_stat'),
        'speed': pokemon_data.get('stats')[5].get('base_stat')
    },
    pokemon_data_2.get('name').capitalize(): {
        'hp': pokemon_data_2.get('stats')[0].get('base_stat'),
        'attack': pokemon_data_2.get('stats')[1].get('base_stat'),
        'defense': pokemon_data_2.get('stats')[2].get('base_stat'),
        'special_attack': pokemon_data_2.get('stats')[3].get('base_stat'),
        'special_defense': pokemon_data_2.get('stats')[4].get('base_stat'),
        'speed': pokemon_data_2.get('stats')[5].get('base_stat')
    }
}

st.bar_chart(comparison)
    
    
