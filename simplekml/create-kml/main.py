text = '''./production.log.109.gz:I, [2022-02-10T10:00:59.703529 #25190]  INFO -- : #<Event::TeltonikaServer:3ffcbe931d90>:357544377733734 TS: 2022-02-10 10:00:35 +0000, GPS: 52.1773033,20.8162, SAT: 17, KM/H: 0, V: 26343
./production.log.109.gz:I, [2022-02-10T10:01:13.939349 #25190]  INFO -- : #<Event::TeltonikaServer:3ffcbe931d90>:357544377733734 TS: 2022-02-10 10:00:40 +0000, GPS: 52.1773033,20.8162, SAT: 17, KM/H: 0, V: 26352
./production.log.109.gz:I, [2022-02-10T10:10:44.757308 #25190]  INFO -- : #<Event::TeltonikaServer:3ffcbe931d90>:357544377733734 TS: 2022-02-10 10:10:40 +0000, GPS: 52.1773033,20.8162, SAT: 18, KM/H: 0, V: 25924
'''

import io
import re
import simplekml

#f = open("filename.log")
f = io.StringIO(text)

# -----------------------

groups = {}

for line in f:
    ts  = re.findall('TS: ([^ ]*) ', line)[0]
    gps = re.findall('GPS: ([^ ]*), ', line)[0]
    
    print('TS:', ts, '| GPS:', gps)
    
    if ts not in groups:
        groups[ts] = []
        
    groups[ts].append(gps)
    
#----------------------------------------
    
for name, values in groups.items():
    print('name:', name)
    
    kml = simplekml.Kml()
    
    for gps in values:
        kml.newpoint(coords=[gps.split(',')])
        
    # --- after loop ---
    kml.save(f"{name}.kml")
