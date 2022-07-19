import requests
from requests.models import InvalidURL

def verifica(url):
    try:
        requests.get(url)
    except requests.ConnectionError:
        print('\033[31m[ERRO] Verifique sua conexão e o link inserido!\033[m')
    except InvalidURL:
        print('\033[31mLink inválido\033[m')
    except:
        print('\033[31mERRO DESCONHECIDO! Talvez a url esteja errada.\033[m')
    else:
        print('Acessado')

verifica('https://www.youtube.com/watch?v=ik0qg-O_2DM')
