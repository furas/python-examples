# Quandl

Link: [www.quandl.com](https://www.quandl.com/)

## Python API

Link [Python API](https://www.quandl.com/tools/python)

Install

    ```bash
    $ pip install quandl

## Warsaw Stock Exchange (GPW)

Python instruction: https://www.quandl.com/data/WSE-Warsaw-Stock-Exchange-GPW/usage/quickstart/python


Link: [https://www.quandl.com/data/WSE-Warsaw-Stock-Exchange-GPW](https://www.quandl.com/data/WSE-Warsaw-Stock-Exchange-GPW)

ie. [PZU](https://www.quandl.com/data/WSE-Warsaw-Stock-Exchange-GPW?keyword=PZU), [WIG20](https://www.quandl.com/data/WSE-Warsaw-Stock-Exchange-GPW?keyword=WIG20)

    ```python
    import quandl
    
    data = quandl.get('WSE/PZU')
    #data = quandl.get('WSE/WIG20')
    
    print('    columns:', list(data.columns))
    print('start index:', data.index[0])
    print('  end index:', data.index[-1])

    #     columns: ['Open', 'High', 'Low', 'Close', '%Change', 'Volume', '# of Trades', 'Turnover (1000)']
    # start index: 2010-05-12 00:00:00
    #   end index: 2018-05-29 00:00:00

## Warsaw Stock Exchange (deprecated)

Link: [https://www.quandl.com/data/WARSAWSE-Warsaw-Stock-Exchange](https://www.quandl.com/data/WARSAWSE-Warsaw-Stock-Exchange)

ie. [WIG20](https://www.quandl.com/data/WARSAWSE/WIG20-Warsaw-Stock-Exchange-Indices-WIG20)

    ```python
    import quandl
    
    data = quandl.get('WARSAWSE/WIG20') # less data then on 'WSE'
    #data = quandl.get('WARSAWSE/PZU') # doesn't exist
    
    print('    columns:', list(data.columns))
    print('start index:', data.index[0])
    print('  end index:', data.index[-1])

    #     columns: ['Open', 'High', 'Low', 'Close', '% Change', 'Turnover (1000s)']
    # start index: 2016-10-03 00:00:00
    #   end index: 2017-11-02 00:00:00
  
