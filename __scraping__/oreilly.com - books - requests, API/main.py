# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.28
# 

import requests

url = 'https://www.oreilly.com/api/v2/search/?query=*&extended_publisher_data=true&highlight=true&include_assessments=false&include_case_studies=true&include_courses=true&include_playlists=true&include_collections=true&include_notebooks=true&include_sandboxes=true&include_scenarios=true&is_academic_institution_account=false&source=user&formats=book&formats=article&formats=journal&sort=date_added&facet_json=true&json_facets=true&page=0&include_facets=true&include_practice_exams=true&orm-service=search-frontend'

response = requests.get(url) 

data = response.json()

for number, item in enumerate(data['results'], 1):
    print(number, '|', item['title'])
