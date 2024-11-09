# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:56:00 2024

@author: Riartts
"""

import csv

# Trabalhando com CSV

with open("pessoas.csv") as arqv:
    dados_pessoas = csv.reader(arqv, delimiter=',')
    for linha in dados_pessoas:
        print(linha)

print("############################################")

# CSV com dicionário e lendo por chave

with open('pessoas.csv') as arqv:
    dados_pessoas = csv.DictReader(arqv, delimiter=',')
    for linha in dados_pessoas:
        print(linha['nome'])
        
print("############################################")

# CSV com Lista

with open('pessoas.csv','a') as arqv:
    dados_pessoas = csv.DictReader(arqv, delimiter=',')
    escritor = csv.writer(arqv, delimiter=',')
    escritor.writerow(['nome', 'cidade', 'estado', 'idade', 'profissão'])
    escritor.writerow(['alana', 'penha', 'sc', '20', 'estudante'])
    

lista_pessoas = [
     ['nome','idade','cidade','estado','profissão'],
     ['Ana Silva','32','São Paulo','SP','Engenheira'],
     ['Carlos Oliveira','45','Rio de Janeiro','RJ','Professor'],
     ['Mariana Santos','28','Belo Horizonte','MG','Médica'],
     ['João Pereira','39','Salvador','BA','Advogado'],
     ['Fernanda Costa','53','Porto Alegre','RS','Empresária'],
     ['Rafael Almeida','26','Recife','PE','Programador'],
     ['Beatriz Lima','41','Fortaleza','CE','Jornalista'],
     ['Gabriel Martins','35','Curitiba','PR','Arquiteto'],
     ['Luciana Ferreira','29','Manaus','AM','Bióloga'],
     ['Rodrigo Souza','48','Brasília','DF','Economista']
     ]  

with open ('pessoas.csv','a') as arqv:
    escritor = csv.writer(arqv, delimiter=',')
    escritor.writerows(lista_pessoas)


# CSV com dicionário
    
lista_pessoas_dict = [
    {
        "nome": "Ana Silva",
        "idade": 32,
        "cidade": "São Paulo",
        "estado": "SP",
        "profissão": "Engenheira"
    },
    {
        "nome": "Carlos Oliveira",
        "idade": 45,
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "profissão": "Professor"
    },
    {
        "nome": "Mariana Santos",
        "idade": 28,
        "cidade": "Belo Horizonte",
        "estado": "MG",
        "profissão": "Médica"
    },
    {
        "nome": "João Pereira",
        "idade": 39,
        "cidade": "Salvador",
        "estado": "BA",
        "profissão": "Advogado"
    },
    {
        "nome": "Fernanda Costa",
        "idade": 53,
        "cidade": "Porto Alegre",
        "estado": "RS",
        "profissão": "Empresária"
    },
    {
        "nome": "Rafael Almeida",
        "idade": 26,
        "cidade": "Recife",
        "estado": "PE",
        "profissão": "Programador"
    },
    {
        "nome": "Beatriz Lima",
        "idade": 41,
        "cidade": "Fortaleza",
        "estado": "CE",
        "profissão": "Jornalista"
    },
    {
        "nome": "Gabriel Martins",
        "idade": 35,
        "cidade": "Curitiba",
        "estado": "PR",
        "profissão": "Arquiteto"
    },
    {
        "nome": "Luciana Ferreira",
        "idade": 29,
        "cidade": "Manaus",
        "estado": "AM",
        "profissão": "Bióloga"
    },
    {
        "nome": "Rodrigo Souza",
        "idade": 48,
        "cidade": "Brasília",
        "estado": "DF",
        "profissão": "Economista"
    }
]    
    
campos = ['nome', 'cidade','estado', 'idade', 'profissão']

with open('pessoas.csv', 'a') as arqv:
    escritor = csv.DictWriter(arqv, delimiter=',', fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(lista_pessoas_dict)
    
    
    