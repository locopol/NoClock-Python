import requests, re, schedule
from bs4 import BeautifulSoup
from __main__ import notification

#Bencina en linea
bel_region = '7'
bel_comuna = '327'
bel_gas = '1'

def get_bencina_enlinea():
    url = 'http://www.bencinaenlinea.cl/web2/buscador.php?region=' + bel_region
    res = 'http://www.bencinaenlinea.cl/web2/imprimir_tabla_resumen.php'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    token = re.search(r"buscar_en_mapa\('(.*)'\)", soup.find('script', text=lambda t: t and 'imprimir_tabla' in t).string).group(1)
    data = {
        'region': bel_region,
        'comuna': 'comuna=' + bel_comuna,
        'combustible': bel_gas,
        'token': token,
        'bandera': ''
    }
    headers = {
        'Cookie': response.cookies.items()[0][0] + "=" + response.cookies.items()[0][1]
    }
  
    response2 = requests.post(res, data=data, headers=headers)
    soup = BeautifulSoup(response2.text, 'html.parser')

    text = "Bencina   en linea: Min: " + re.search(r"\d+", soup.find_all('b')[0].text).group(0) + "Max: " + re.search(r"\d+", soup.find_all('b')[1].text).group(0)

    obj = {"icon": { "x": 1, "y": 10, "value": "gas" }, "message": { "x": 10, "y": 3, "value": text}, "remaining_time": 10 }
    
    print("Bencina en linea ... " + notification(myObj=obj))

def main():
#    schedule.every(2).hours.do(get_bencina_enlinea)
    schedule.every(10).seconds.do(get_bencina_enlinea)
