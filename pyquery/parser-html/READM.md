
`PyQuery` has problem to work with page 
 
    http://www.floridaleagueofcities.com/widgets/cityofficials?CityID=101
    
Using `PyQuery(..., parser="html")` resolved this problem

https://stackoverflow.com/questions/57454154/pyquery-wont-return-elements-on-a-page

https://github.com/gawel/pyquery/issues/199
