
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.19
#
# title: How to Extract All Crypto Symbols from Coinmarketcap
# url: https://stackoverflow.com/questions/70027278/how-to-extract-all-crypto-symbols-from-coinmarketcap/70028568#70028568

# [How to Extract All Crypto Symbols from Coinmarketcap](https://stackoverflow.com/questions/70027278/how-to-extract-all-crypto-symbols-from-coinmarketcap/70028568#70028568)

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
        print(f"{start+number:4} | {item['symbol']:5} | {item['date_added'][:10]}")

'''
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
  11 | SHIB  | 2020-08-01
  12 | AVAX  | 2020-07-13
  13 | LUNA  | 2019-07-26
  14 | LTC   | 2013-04-28
  15 | WBTC  | 2019-01-30
  16 | BUSD  | 2019-09-20
  17 | CRO   | 2018-12-14
  18 | UNI   | 2020-09-17
  19 | LINK  | 2017-09-20
  20 | ALGO  | 2019-06-20
  21 | BCH   | 2017-07-23
  22 | MATIC | 2019-04-28
  23 | VET   | 2017-08-22
  24 | XLM   | 2014-08-05
  25 | AXS   | 2020-08-31
  26 | MANA  | 2017-09-17
  27 | ICP   | 2021-03-23
  28 | TRX   | 2017-09-13
  29 | FTT   | 2019-07-31
  30 | UST   | 2020-09-21
  31 | FIL   | 2017-12-13
  32 | DAI   | 2019-11-22
  33 | ETC   | 2016-07-24
  34 | EGLD  | 2020-09-04
  35 | ATOM  | 2019-03-14
  36 | THETA | 2018-01-17
  37 | BTCB  | 2019-06-18
  38 | HBAR  | 2019-09-17
  39 | NEAR  | 2020-08-11
  40 | FTM   | 2018-10-29
  41 | XTZ   | 2017-10-06
  42 | GRT   | 2020-12-17
  43 | XMR   | 2014-05-21
  44 | HNT   | 2020-06-05
  45 | EOS   | 2017-07-01
  46 | SAND  | 2020-08-05
  47 | KLAY  | 2020-03-30
  48 | FLOW  | 2021-01-27
  49 | CAKE  | 2020-09-25
  50 | AAVE  | 2020-10-02
  51 | MIOTA | 2017-06-13
  52 | XEC   | 2021-07-08
  53 | KDA   | 2020-05-31
  54 | LRC   | 2017-08-30
  55 | LEO   | 2019-05-21
  56 | KSM   | 2019-12-12
  57 | NEO   | 2016-09-08
  58 | BSV   | 2018-11-09
  59 | MKR   | 2017-01-29
  60 | QNT   | 2018-08-10
  61 | ENJ   | 2017-11-01
  62 | CHZ   | 2019-07-01
  63 | RUNE  | 2019-07-23
  64 | ONE   | 2019-06-01
  65 | STX   | 2019-10-28
  66 | WAVES | 2016-06-02
  67 | BTT   | 2019-01-31
  68 | HOT   | 2018-04-29
  69 | AMP   | 2020-09-08
  70 | ZEC   | 2016-10-29
  71 | AR    | 2020-05-27
  72 | DASH  | 2014-02-14
  73 | COMP  | 2020-06-16
  74 | KCS   | 2017-10-24
  75 | CELO  | 2020-05-22
  76 | CRV   | 2020-08-14
  77 | NEXO  | 2018-05-01
  78 | IOTX  | 2018-05-25
  79 | TFUEL | 2019-03-28
  80 | WAXP  | 2017-12-21
  81 | HT    | 2018-02-03
  82 | XEM   | 2015-04-01
  83 | BAT   | 2017-06-01
  84 | OKB   | 2019-04-30
  85 | DCR   | 2016-02-10
  86 | ICX   | 2017-10-27
  87 | QTUM  | 2017-05-24
  88 | OMG   | 2017-07-14
  89 | TUSD  | 2018-03-06
  90 | MINA  | 2021-03-02
  91 | YFI   | 2020-07-18
  92 | RVN   | 2018-03-10
  93 | VGX   | 2017-07-18
  94 | SUSHI | 2020-08-28
  95 | UMA   | 2020-05-25
  96 | AUDIO | 2020-10-20
  97 | REV   | 2017-11-01
  98 | SCRT  | 2020-05-19
  99 | ZIL   | 2018-01-25
 100 | VLX   | 2019-10-03
'''
