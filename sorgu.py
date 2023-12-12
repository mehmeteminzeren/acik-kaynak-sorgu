import requests
URL="https://api.agify.io?name=michael"
result=requests.get(URL)
data=result.json()
print(data)