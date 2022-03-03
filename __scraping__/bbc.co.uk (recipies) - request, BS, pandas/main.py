# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.28
# [Python function returning None when trying to display dataframe - Stack Overflow](https://stackoverflow.com/questions/71266235/python-function-returning-none-when-trying-to-display-dataframe/71289394#71289394)

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

# --- functions ---

def collect_page_data(url, columns_name):

    # --- scraping ---
    
    page = requests.get(url)
    page_soup = BeautifulSoup(page.text, 'html.parser')
    
    res = page_soup.find("script", {"type": "application/ld+json"})

    #data = json.loads(res.text)
    data = json.loads(res.string)  # 
    
    prep_time = data['prepTime']
    cook_time = data['cookTime']
    
    for char in ['P', 'T', 'M']:
        prep_time = prep_time.replace(char, "")
        cook_time = cook_time.replace(char, "")
        
    total_time = int(prep_time) + int(cook_time)

    # --- dataframe ---
    
    df = pd.DataFrame(columns=columns_name)
    
    df = df.append({
        'name': data['author']['name'],
        'total_time': total_time,
        'image': data['image'],
        'rating_count': data['aggregateRating']['ratingCount'],
        'rating_value': data['aggregateRating']['ratingValue'],
        'category': data['recipeCategory'],
        'ingredients': data['recipeIngredient'],
        'diet': data['suitableForDiet'][1],
        'vegan': data['suitableForDiet'][2],
        'vegetarian': data['suitableForDiet'][3],
        'url': url
    }, ignore_index=True)
        
    return df

# --- main ---

columns_name = [
    'title', 'name', 'total_time', 'image',
    'ingredients', 'rating_value', 'rating_count',
    'category', 'cuisine', 'diet', 'vegan', 'vegetarian', 'url'
]

url = 'https://www.bbc.co.uk/food/recipes/avocado_pasta_with_peas_31700'

df = collect_page_data(url, columns_name)

print(df.iloc[0])

