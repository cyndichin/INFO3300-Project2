import re

with open('stringified','r') as u:
	jsonData = u.read()

result = re.sub(r'{("name":"[^"]+"),"children":\[{"Studio":"[^"]+","Genre":"[^"]+","Film":"[^"]+",("Gross":[^}]+)}\]}', r'{\1,\2}',jsonData)

with open('fixedJson2007.json','w') as f:
	f.write(result)

