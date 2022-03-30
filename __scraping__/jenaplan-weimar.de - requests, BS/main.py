# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.29
# [python - Printing out the entire Table Row of one or more found elements - Stack Overflow](https://stackoverflow.com/questions/71638172/printing-out-the-entire-table-row-of-one-or-more-found-elements/71660773#71660773)
                                                                                            
import requests
from bs4 import BeautifulSoup
import re

#day = input("Für welchen tag willst du den vertretungsplan sehen? \n Heute = 1, Morgen = 2, Übermorgen = 3 \n")
day = "1"

if day not in ("1", "2", "3"):
    print("Bitte gebe eine zahl von 1-3 ein!")
else:
       
    url = f"https://jenaplan-weimar.de/vplan/Vertretungsplaene/SchuelerInnen/subst_00{day}.htm"
    
    response = requests.get(url)
    doc = BeautifulSoup(response.content, "html.parser")
    
    #wunschklasse = input("Für welche Klasse möchtest du den Vertretungsplan sehen? (Achtung, bitte beachte die Abkürzungen!) ")
    wunschklasse = "STG"

    found = False

    all_rows = doc.find_all('tr')
    for row in all_rows:
        klasse = row.find_all(text=re.compile(f"{wunschklasse}.*"))
        if klasse:
            row_text = row.get_text(strip=True, separator='|')
            print(f"Für {wunschklasse} wurde folgendes gefunden: {row_text}")
            found = True

    # ----
    
    if not found:
        print("Sry aber deine gewählte Klasse hat keine Vertertung bzw keinen Ausfall")

