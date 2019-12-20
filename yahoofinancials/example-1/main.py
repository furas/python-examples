from yahoofinancials import YahooFinancials  

yahoo_financials = YahooFinancials('AAPL')
data = yahoo_financials.get_financial_stmts('annual', 'income') 

#print( data['incomeStatementHistory']['AAPL'][0].keys()  )
#print( data['incomeStatementHistory']['AAPL'][1].keys()  )
#print( data['incomeStatementHistory']['AAPL'][2].keys()  )

for item in data['incomeStatementHistory']['AAPL']:
    for key, val in item.items():
        print(key, val['ebit'])
    
