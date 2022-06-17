# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.11
# [python - Accessing Data from Javascript API call - Stack Overflow](https://stackoverflow.com/questions/72570830/accessing-data-from-javascript-api-call/72575730)

# `requests` converts `+` to `%28` but server needs `+`

import requests
import urllib.parse

data = {
    "xmlquery": "<post>\n<param+name=\"Exchange\"+value=\"NMF\"/>\n<param+name=\"SubSystem\"+value=\"Prices\"/>\n<param+name=\"Action\"+value=\"GetMarket\"/>\n<param+name=\"inst__a\"+value=\"0,1,2,5,21,23\"/>\n<param+name=\"ext_xslt\"+value=\"/nordicV3/paging_inst_table.xsl\"/>\n<param+name=\"Market\"+value=\"GITS:CO:CPHCB,GITS:CO:CPHBB,M:GITS:CO:CPHTA,GITS:CO:CPHAU,GITS:CO:CPHSA\"/>\n<param+name=\"RecursiveMarketElement\"+value=\"True\"/>\n<param+name=\"XPath\"+value=\"//inst[@itid='2'+or+@itid='3']\"/>\n<param+name=\"ext_xslt_lang\"+value=\"en\"/>\n<param+name=\"ext_xslt_tableId\"+value=\"bondsSearchDKTable\"/>\n<param+name=\"ext_xslt_options\"+value=\",noflag,\"/>\n<param+name=\"ext_xslt_hiddenattrs\"+value=\",fnm,isrid,dlt,tp,bb,ib,cpt,rps,os,lt,st,itid,lists,it,mkt,\"/>\n<param+name=\"ext_xslt_notlabel\"+value=\",fnm\"/>\n<param+name=\"ext_xslt_jspcbk\"+value=\"doPaging\"/>\n<param+name=\"ext_xslt_jsscbk\"+value=\"doSortPager\"/>\n<param+name=\"ext_xslt_sorder\"+value=\"descending\"/>\n<param+name=\"ext_xslt_sattr\"+value=\"chp\"/>\n<param+name=\"ext_xslt_start\"+value=\"0\"/>\n<param+name=\"ext_xslt_size\"+value=\"100\"/>\n<param+name=\"inst__an\"+value=\"id,nm,fnm,isin,cpnrt,bp,ap,lsp,chp,atap,ed,dlt,cr,isrid,tp,bb,ib,cpt,rps,os,lt,st,itid,lists,it,mkt\"/>\n<param+name=\"app\"+value=\"/obligationer/danmark\"/>\n</post>"
}

# server needs all these headers
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

url = 'http://www.nasdaqomxnordic.com/webproxy/DataFeedProxy.aspx'

data_str = urllib.parse.urlencode(data, safe="+")  # <-- don't convert `+`

response = requests.post(url, data=data_str, headers=headers)

#print(response.text)

# ---------------------------------

import pandas as pd

all_tables = pd.read_html(response.text)
df = all_tables[1]

print(df)
