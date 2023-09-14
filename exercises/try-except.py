def coleta_rm():
    while True:
        message = ""
        try:
            rm = int(input("Digite seu RM:"))
        except ValueError:
            print("Valor digitado não está de acordo, só são permitidos caracteres numéricos.")
            print()
            message = "Houve um erro! Um novo ciclo será iniciado.\n"
        else:
            message = "RM coletado com sucesso."
            return rm
        finally:    # finally tem precedência em relação ao "return", pois ela precisa ser executada
            print(message)
print(coleta_rm())
print()


# Exercícios

# 1- Peça ao usuário para inserir dois números e realizar uma divisão.
# Use try e except para lidar com a exceção de divisão por zero e imprima uma mensagem apropriada

print("Exercício 1\n")

while True:
    try:
        num_1 = int(input("Digite o primeiro numero:"))
        num_2 = int(input("Digite o segundo numero:"))
        div = num_1 / num_2
    except ValueError:
        print("Digite apenas caracteres numericos.")
    except ZeroDivisionError:
        print("Impossível dividir por zero.")
    else:
        print(f"O valor da divisao de {num_1} por {num_2} é {div}.")
        break
    finally:
        print()


# 2- Calculadora de idade com tratamento de data de nascimento:
# Peça ao usuário para inserir sua data de nascimento no formato "dd/mm/aaaa"
# Utilize try e except para capturar erros de entrada e calcular a idade da pessoa
# Em seguida, use um bloco else para exibir a idade calculada e um bloco finally
# para agradecer o usuário por usar a calculadora

print("Exercício 2\n")

from datetime import datetime

while True:
    try:
        nasc = datetime.fromisoformat(input("Digite uma data de nascimento no formato aaaa-mm-dd:"))
    except:
        print("Digite uma data valida de acordo com o padrao aaaa-mm-dd.")
    else:
        today = datetime.today()
        idade_anos = int((today - nasc).days / 365)
        print(f"Voce possui {idade_anos} anos.")
        break
    finally:
        print()