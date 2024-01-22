import requests

url = "https://api.content.tripadvisor.com/api/v1/location/8604500/details?key=7BAF1BAB80954D11BA836E0CEC3C3366&language=en&currency=USD"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)