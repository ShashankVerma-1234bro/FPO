import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"28.61,77.20"}

headers = {
	"X-RapidAPI-Key": "1a13c3820bmsh95a7966a03e8e9bp10f91ajsnd6136685c2bf",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

for i in response.json():
    print(i, (response.json())[i])
