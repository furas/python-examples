import pandas as pd

url = "http://properties.kimcorealty.com/property/output/find/search4/view:list/"

all_tables = pd.read_html(url) ; df = all_tables[0]

print(data[0])
headers = ['Number', 'Tenant', 'Square Footage']
    
#df = DataFrame(table, columns=headers)
#print (df)
