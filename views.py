from .views import get_data
import requests


def get_data():

#Pega e devolve os dados da API pro JSON.
  response = requests.get('')
  data = response.json()
  return data
