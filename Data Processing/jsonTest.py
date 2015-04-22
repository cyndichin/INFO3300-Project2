import re

#Get data from the stringified +copy/pasted genJSON result for some year
with open('stringified','r') as u:
	jsonData = u.read()

result = re.sub(r'{("name":"[^"]+"),"children":\[{"Studio":"[^"]+","Genre":"[^"]+","Film":"[^"]+",("Gross":[^}]+)}\]}', r'{\1,\2}',jsonData)

#Write for year
with open('2007.json','w') as f:
	f.write(result)

#Clean up with jsonlint.com and remove null values (caused by csv oddities)