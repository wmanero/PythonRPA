# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:18:14 2024

@author: WManero
"""

import requests
"""
resposta = requests.get("https://reqres.in/api/users?page=2")
resp_formatado = resposta.json()
print(resp_formatado.keys())
print()
print("ID: ",resp_formatado["data"][0]["id"])
print("E-mail: ",resp_formatado["data"][0]["email"])
print("Nome: ",resp_formatado["data"][0]["first_name"])
print("Sobrenome: ",resp_formatado["data"][0]["last_name"])
"""
resposta = requests.get("http://universities.hipolabs.com/search?country=brazil")
resp_formatado = resposta.json()
print(resp_formatado[3].keys())
print(resp_formatado[3]["web_pages"])