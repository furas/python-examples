import pandas as pd

df = pd.DataFrame({'url':[
    'https://stackoverflow.com',
    'https://httpbin.org',
    'https://toscrape.com',
]})

pd.set_option('display.max_colwidth', -1)
result = df.to_html(formatters={'url':lambda x:f'<a href="{x}">{x}</a>'}, escape=False)

print(result)

df = pd.DataFrame({
    'url':[
        'https://stackoverflow.com',
        'https://httpbin.org',
        'https://toscrape.com',
    ],
    'name':[
        'Ask question',
        'Test requests',
        'Learn scraping'
    ]
})

render_template_string('''
<table>
{% for row in dt.iterrows() %}
    <tr><td><a href="{{ row['url'] }}">{{ row['name'] }}</a></td></tr>
{% endfor %}
</table>
''', df=df)

