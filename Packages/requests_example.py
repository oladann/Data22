import requests

request_bbc = requests.get("https://www.bbc.co.uk/")

print(request_bbc.content)






#python_package (Root folder)
#-- app (folder)
#----__init__.py
#----Requests.py
#program.py
#setup.py