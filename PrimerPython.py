import json
import os
bills = { "data":[]}

def fil_billdata():
	info = {}
	info["name"]= input('Please tell me the name of the bill:')
	info["amount"]=float(input('Please tell me the amount:'))
	info["date"]=input('Please tell me the date:')
	info["autopay"]=input('Please tell me if it is on autopay:')
	add_info(info)

def add_info(info):
	bills["data"].append(info)
def build_data():
	x = 'No'
	while(x!='n'):
		fil_billdata()
		x = input('Would you like to add another?[y/n]')

# read file if it exists
if os.path.exists('testfile.json'):
	with open('testfile.json', 'r') as myfile:
		data=myfile.read()
		# parse file
	bills = json.loads(data)
	if bills is None:
		if 'y' == input('The file was empty, would you like to start a file?[y/n]'):
			build_data()
		else:
			quit()
else:
	build_data()

y = json.dumps(bills, indent=4)
print('This is what will be written to file')
print(y)
if input('Save to file? [y/n]') == 'y':
	f = open("testfile.json","w")
	f.write(y)
	f.close()