
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.19
#
# title: How to Extract All Crypto Symbols from Coinmarketcap
# url: https://stackoverflow.com/questions/70027278/how-to-extract-all-crypto-symbols-from-coinmarketcap/
# [How to Extract All Crypto Symbols from Coinmarketcap](https://stackoverflow.com/questions/70027278/how-to-extract-all-crypto-symbols-from-coinmarketcap/)

# title: can't retrieve data after 10 row in a 100 row table
# url: https://stackoverflow.com/questions/71286789/cant-retrieve-data-after-10-row-in-a-100-row-table/
# [can't retrieve data after 10 row in a 100 row table](https://stackoverflow.com/questions/71286789/cant-retrieve-data-after-10-row-in-a-100-row-table/)

# https://coinmarketcap.com/all/views/all/

# [Listings Latest](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest)

import requests

url = 'https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


for start in range(1, 20000, 5000):

    params = {
        'start': start,
        'limit': 5000,
    }

    r = requests.get(url, params=params)
    data = r.json()
    
    for number, item in enumerate(data['data']):
         # first question
         #print(f"{start+number:4} | {item['symbol']:5} | {item['date_added'][:10]}")
         
         # second question
         usd = item['quote']['USD']
         print(f"{start+number:4} | {item['name']:20} | {item['symbol']:20} | {usd['price']:25} | {usd['market_cap']:20} | {usd['volume_24h']:12}")

''' --- first question ---
   1 | BTC   | 2013-04-28
   2 | ETH   | 2015-08-07
   3 | BNB   | 2017-07-25
   4 | USDT  | 2015-02-25
   5 | SOL   | 2020-04-10
   6 | ADA   | 2017-10-01
   7 | XRP   | 2013-08-04
   8 | DOT   | 2020-08-19
   9 | USDC  | 2018-10-08
  10 | DOGE  | 2013-12-15
'''

''' --- second question ---
   1 | Bitcoin              | BTC                  |         37583.10571031953 |    712944938281.2621 | 20506963757.761803
   2 | Ethereum             | ETH                  |        2605.4265612647923 |    312019186748.4554 | 14735857986.984612
   3 | Tether               | USDT                 |        1.0004365827321502 |    79582785654.62805 | 52322182961.31001
   4 | BNB                  | BNB                  |         360.8294815571075 |   59578995228.327576 | 1506217337.3376758
   5 | USD Coin             | USDC                 |        0.9998571962594189 |    53366037535.38875 | 3906120808.287997
   6 | XRP                  | XRP                  |        0.7155041339106955 |   34307908872.285137 | 2474248121.70985
   7 | Cardano              | ADA                  |         0.845557365804996 |   28451406129.877007 | 1117625241.1235523
   8 | Terra                | LUNA                 |         73.41161643060934 |     27727822937.5355 | 3098404637.7947397
   9 | Solana               | SOL                  |         84.86524818533208 |   27162230598.676266 | 1917755991.5167074
  10 | Avalanche            | AVAX                 |         73.99209094139086 |    18207101060.97057 | 1587619301.2131295
'''
