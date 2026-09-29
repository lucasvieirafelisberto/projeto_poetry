import os
from datetime import datetime
import requests
import sys

def buscar_fato_aleatorio() -> dict:
    resposta = requests.get("https://uselessfacts.jsph.pl/random.json?language=pt")
    return {"fato": resposta.json()["text"],"sistema": sys.platform,"diretorio":os.getcwd(),"data": datetime.now().isoformat()}

def main():
    resultado = buscar_fato_aleatorio()
    print(resultado)

if __name__ == "__main__": main()