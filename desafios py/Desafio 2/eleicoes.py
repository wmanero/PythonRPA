from datetime import date as dt

data = dt.today()

print("*" * 27)
print("*" * 6, f"ELEIÇÕES {data.year}", "*" * 6)
print("*" * 27)
print("")

print("Valide suas informações para \nvotar nestas eleições.")
print("")

try:
    nome = input("Digite seu nome completo: ")
    nome = nome.title().strip()
    idade = int(input("Digite sua idade: "))
    idade = idade

    if idade >= 16:
        print(f"Parabéns {nome}, você tem {idade} anos e está apito a votar nestas eleições.")
    else:
        print(f"Infelizmente, {nome}, você tem {idade} anos e ainda não está apito a votar nestas eleições.")
except:
    print("Dados inválidos! Reinicie o programa e tente novamente.")


print("")
print("Aperte \'Enter' para sair.")
input("")