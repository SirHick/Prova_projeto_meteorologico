import requests
from flask import Flask

flask = Flask(__name__)

url = f"https://api.open-meteo.com/v1/forecast"

payload = {'temperature_2m': dados[]}

resposta = requests.get(
    url,
    params = ,
    timeout=15
)

dados = resposta.json()

valor = dados['temperature_2m']

print(valor)

resposta.raise_for_status()

def obter_tempo():
    dados = resposta.json()
    condicoes_atuais = dados["current"]
    return {    
        "temperatura": condicoes_atuais["temperature_2m"],    
        "sensacao_termica": condicoes_atuais["apparent_temperature"],    
        "precipitacao": condicoes_atuais["precipitation"],}