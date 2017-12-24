
API: [https://poloniex.com/support/api/](https://poloniex.com/support/api/})

Example result

    url: https://poloniex.com/public?command=returnTradeHistory&currencyPair=BTC_NXT&start=1410158341&end=1410499372
    -----
    data lenght: 1112
    -----
    data[0].keys; dict_keys(['globalTradeID', 'tradeID', 'date', 'type', 'rate', 'amount', 'total'])
    -----
    globalTradeID: 2036467
          tradeID: 21387
             date: 2014-09-12 05:21:26
             type: buy
             rate: 0.00008943
           amount: 1.27241180
            total: 0.00011379
    -----
    globalTradeID: 2036466
          tradeID: 21386
             date: 2014-09-12 05:21:26
             type: buy
             rate: 0.00008943
           amount: 1.27241180
            total: 0.00011379
    -----
    globalTradeID: 2036465
          tradeID: 21385
             date: 2014-09-12 05:21:26
             type: buy
             rate: 0.00008943
           amount: 238.28433663
            total: 0.02130976
    -----

