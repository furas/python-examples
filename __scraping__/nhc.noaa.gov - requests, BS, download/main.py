
# author: https://blog.furas.pl
# date: 2020.08.02
# link: https://stackoverflow.com/questions/63214832/extract-table-and-especially-files-from-webpage-with-python/

import requests
from bs4 import BeautifulSoup as BS
import os
import urllib.parse


def get_data(ocean='atlantic'):

    all_oceans = ['atlantic', 'eastern pacific', 'central pacific']
    
    ocean = ocean.lower()
    
    # check if ocean's name is correct and convert to column number in table
    if ocean in all_oceans:
        column = all_oceans.index(ocean) + 1
    else:
        print('Wrong ocean:', ocean)
        return

    # create folder for all files
    folder = ocean
    os.makedirs(folder, exist_ok=True)

    # get HTML    
    url = 'https://www.nhc.noaa.gov/gis/'
    r = requests.get(url)
    soup = BS(r.content, 'lxml')  # `html.parser` gives wrong number of rows 

    # works with rows in table    
    table = soup.find('table')
    all_rows = table.find_all('tr')

    print('rows:', len(all_rows))

    for row in all_rows:
        
        # get all cells in current row
        all_cell = row.find_all('td')

        # display `header` from first column
        header = all_cell[0].find('b')
        if header:
            header = header.get_text(strip=True)
            
        if not header:
            header = '???'
            
        print('\n---', header, '---\n')
        
        # in some rows cells are joined so all oceans need the same `column=1`
        number_of_cells = len(all_cell)

        if number_of_cells == 3:
            column = 1

        # work with data in cell
        if number_of_cells == 3:
            cell = all_cell[1]       # one cell for all oceans
        else:
            cell = all_cell[column]  # every ocean has own cell in row
        
        print('text:', cell.get_text(strip=True), '\n')
        
        # works with all links in cell
        for link in cell.find_all('a'):
            
            href = link['href']
            print('    > link:', link.text, '==>', href)
            
            # create full path to linked file or page
            #if href.startswith(('http://', 'https://', 'ftp://')):
            #    full_url = href
            #elif href.startswith('/'):
            #    full_url = 'https://www.nhc.noaa.gov' + href
            #else:
            #    full_url = 'https://www.nhc.noaa.gov/gis/' + href
               
            full_url = urllib.parse.urljoin(url, href)
            
            # download only files with expected extensions
            if full_url.endswith( ('.zip', '.kmz', '.kml', '.xml') ):
                print('    > full url :', full_url)
                filename = full_url.rsplit('/', 1)[-1]
                full_path = os.path.join(folder, filename)
                print('    > full path:', full_path)
                r = requests.get(full_url)
                with open(full_path, 'wb') as fh:
                    fh.write(r.content)
            else:
                print('    > other:', full_url)
                
# --- main ---

if __name__ == '__main__':
    ocean = 'Atlantic' # 'Eastern Pacific' or 'Central Pacific'
    get_data(ocean)
