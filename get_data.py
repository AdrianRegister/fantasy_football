import requests
import json

from dotenv import load_dotenv
import os

load_dotenv()

def store_data():
  headers = {"x-rapidapi-key": os.getenv("API_KEY")}
  url = f'https://v3.football.api-sports.io/players?league=39&season=2023&page=1'
  
  response = requests.get(url, headers=headers)
  data = response.json()

  print(data)

  # page = 46

  # while page <= 51:
  #   url = f'https://v3.football.api-sports.io/players?league=39&season=2023&page={page}'
  #   response = requests.get(url, headers=headers)
  #   data = response.json()
    
  #   file_path = f'player-data/page{page}.json'
  #   with open(file_path, 'w') as file:
  #       json.dump(data, file, indent=2)
    
  #   page += 1

store_data()    