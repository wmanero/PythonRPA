# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:10:47 2024

@author: WManero
"""

import requests
import json

url = "https://reqres.in/api/users"
payload = json.dumps({
    "name": "WManero",
    "job": "DEV"                     
})
header = {"Content-Type": "application/json"}

resposta = requests.post(url, headers=header, data=payload)
print(resposta.status_code)
resp_formatado = resposta.json()
print(resp_formatado.keys())
print(resp_formatado)

