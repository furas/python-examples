
Data is in `<script>` between `data:` and `queue:` in JSON format.

You can use standard string functions (ie. `find()`, `slicing`) to cut off this part.
And then you can use module `json` to convert to python dictionary.
And then you have to only find `moneyLine` in this dictionary.

    scrapy shell 'http://www.espn.com/nfl/schedule/_/week/1'

get `<script>` as text

    items = response.xpath("//script[contains(., 'moneyLine')]/text()")
    txt = items.extract_first()

find start and end of data 
(I found this manually checking txt)

    start = txt.find('data:') + 6 # manually found how many add to get correct JSON string
    end = txt.find('queue:') - 6  # manually found how many substract to get correct JSON string

    json_string = txt[start:end]

convert to python dictionary

    import json
    data = json.loads(json_string)

example data 
(I found this manually using `data.keys(), data['sports'][0].keys(), etc.)

    data['sports'][0]['leagues'][0]['events'][0]['odds']['home']['moneyLine']

