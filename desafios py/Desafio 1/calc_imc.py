print("######################################")
print("###     D E S A F I O RPA - 01     ###")
print("######################################")
print("            CALCULADORA IMC")
print("       Para sair pressione Enter.")
print("######################################")


peso = input("Insira seu peso: ")
altura = input("Insira sua altura: ")

if peso or altura != "":
    try:
        imc = (float(peso) / (float(altura) * float(altura)))
        
        if imc < 18.5:
            print(f"Você está abaixo do peso. IMC >>> {imc:.2f}")
        elif imc < 24.9:
            print(f"Você está com sobrepeso. IMC >>> {imc:.2f}")
        else:
            print(f"Você está no peso ideal. IMC >>> {imc:.2f}")

    except ValueError as e:
        print(f"Você inseriu dados inválidos. >>> {e}")
                
    except ZeroDivisionError as e:
        print(f"Não é possível divisão por zero. >>> {e}")
            
    finally:
        print("Pressione \"Enter\" para sair!")
        input("")
        

else:
    print("Você escolheu sair. Volte sempre!")