import re

data = ['2d1h39m53s', '1h39m53s', '39m53s', '53s']

for item in data:
    rs = re.search('(?:(\d+)d)?(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?', item)
    print(rs.groups())
    
