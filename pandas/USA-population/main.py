import pandas as pd

def test(narodowosc):
    procenty = df[narodowosc]/1000
    suma_narodowosc = (df['Populacja']*procenty).sum()
    procent = (suma_narodowosc/suma_populacja)
    print(f'{suma_narodowosc:11_.0f} | {procent:6.1%} | {narodowosc}')

tables = pd.read_html('https://pl.wikipedia.org/wiki/Demografia_Stan%C3%B3w_Zjednoczonych')
#len(tables)
df = tables[0]
df['Populacja'] = df['Populacja'].map(lambda x:int(x.replace('\xa0', '')))
df['Hawajczycy i wyspiarze Pacyfiku%'] = df['Hawajczycy i wyspiarze Pacyfiku%'].map(lambda x: 0 if x =='-' else int(x))

suma_populacja = df['Populacja'].sum()

print(f'{s1:11_.0f} | 100.0% | Populacja')
for x in df.columns:
    if x.endswith('%'):
        test(x)

