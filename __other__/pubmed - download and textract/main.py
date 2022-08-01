# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.07.19
# [python - getting weird results from metapub and pubmed - Stack Overflow](https://stackoverflow.com/questions/73043246/getting-weird-results-from-metapub-and-pubmed/)

import os
from urllib.request import urlretrieve
import metapub
import textract

#another_path = '/content/Articles/'
another_path = './'

pmid_list = ['35566889','33538053', '30848212']

for query in pmid_list:

    print('query:', query)

    url = metapub.FindIt(query).url
    print('url:', url)

    if url:

        try:
            out_file = os.path.join(another_path, query)
            print('out_file:', out_file)

            print('... downloading')

            urlretrieve(url, out_file + '.pdf')

            print('... processing')

            data = textract.process(out_file + '.pdf', extension='pdf', method='pdftotext', encoding="utf_8")

            print('... saving')

            with open(out_file + '.txt', "wb") as textfile:  # save bytes
                textfile.write(data)

            print('... OK')

        except Exception as ex:
            print('Exception:', ex)

