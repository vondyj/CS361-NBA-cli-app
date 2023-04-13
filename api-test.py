import requests

BASE_URL = "https://free-nba.p.rapidapi.com"

headers = {
	"X-RapidAPI-Key": "819d583bd4mshb1f58b42eb6bd5fp143f39jsn6aed4cda8d08",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com",
}

querystring = {
    "page": "0",
    "per_page": "25" 
    }

response = requests.request("GET", f"{BASE_URL}/players", headers=headers, params=querystring)

print(response.json())
print(response.status_code)