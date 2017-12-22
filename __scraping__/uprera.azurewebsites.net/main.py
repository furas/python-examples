import requests
from bs4 import BeautifulSoup
import csv
import time

final_data = []

url = "http://uprera.azurewebsites.net/View_projects.aspx"

s = requests.session()

response = s.get(url)
soup = BeautifulSoup(response.text, "html.parser")

VIEWSTATE = soup.select_one("#__VIEWSTATE")['value']
EVENTVALIDATION = soup.select_one("#__EVENTVALIDATION")['value']

headers= {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

formfields = {
    '__VIEWSTATE': VIEWSTATE,
    '__VIEWSTATEGENERATOR': '4F1A7E70',
    '__EVENTVALIDATION': EVENTVALIDATION,
    #'ctl00$ContentPlaceHolder1$DdlprojectDistrict': search_item,
    'ctl00$ContentPlaceHolder1$txtProject': '',
    'ctl00$ContentPlaceHolder1$btnSearch': 'Search'
}

for title in soup.select("#ContentPlaceHolder1_DdlprojectDistrict [value]")[:-1]:
    search_item = title.text
    print('\n-----', search_item, '-----\n')
    
    formfields['ctl00$ContentPlaceHolder1$DdlprojectDistrict'] = search_item

    response = s.post(url, data=formfields, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    all_options  = soup.find_all('option')
    for element in all_options:
        cities = element["value"]

    all_rows = soup.find("table", attrs={"id":"ContentPlaceHolder1_GridView1"}).find_all("tr")[1:]

    count = 0

    for row in all_rows:
        sublist = [search_item]
        
        tds = row.find_all("td")
        
        rera = tds[1].find("span").text
        sublist.append(rera)
        print('rera:', rera)

        name = tds[2].find("span").text
        sublist.append(name)
        print('name:', name)
            
        promoter_name = tds[3].find("span").text
        sublist.append(promoter_name)
        print('promoter_name:', promoter_name)
            
        district = tds[4].find("span").text
        sublist.append(district)
        print('district:', district)
        
        project_type = tds[5].find("span").text
        sublist.append(project_type)
        print('project_type:', project_type)
        
        rare_id = rera[9:]
        print('rare_id:', rare_id)
        details_url = 'http://uprera.azurewebsites.net/View_Registration_Details.aspx?binid={}&hfFlag=edit&ddlPRJ={}&txtPRJ='.format(rare_id, district)
        
        sublist.append(details_url)
        print('url:', details_url)

        final_data.append(sublist)

        count += 1
        print('count:', count)
        
        # for test exit after 10 results
        if count > 3: break
            
        
filename = "./UP_RERA.csv"
with open(filename, "w") as csvfile:
    csvfile = csv.writer(csvfile, delimiter=",")
    csvfile.writerow(['search_item', 'rare', 'name', 'promoter_name', 'district', 'project_type', 'url'])
    for row in final_data:
        csvfile.writerow(row)
