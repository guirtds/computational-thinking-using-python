'''
Exercícios:

1)Solicite um número de usuário,
diga a menor nota de real que é maior que este número,
caso não exista, diga "Este número é muito grande para ser pago com apenas uma nota de real"
'''

numero = float(input("Favor digitar um número:"))

if 0>numero:
    print("Este número é negativo!")

elif 2>numero:
    print("A menor nota maior que {} é a de 2 reais." .format(numero))

elif 5>numero>=2:
    print("A menor nota maior que {} é a de 5 reais." .format(numero))

elif 10>numero>=5:
    print("A menor nota maior que {} é a de 10 reais." .format(numero))

elif 20>numero>=10:
    print("A menor nota maior que {} é a de 20 reais." .format(numero))

elif 50>numero>=20:
    print("A menor nota maior que {} é a de 50 reais." .format(numero))

elif 100>numero>=50:
    print("A menor nota maior que {} é a de 100 reais." .format(numero))

elif 200>numero>=100:
    print("A menor nota maior que {} é a de 200 reais." .format(numero))

elif 200<=numero:
    print("Não existe uma nota de real maior que {}." .format(numero))

else:
    print("Situação não prevista...")

'''
2)Socilite um número ao usuário,
diga se este número é igual a 0,
se não for, diga se ele é par ou ímpar
'''

numero = float(input("Favor digitar um número:"))

if numero == 0:
    print(f"O número digitado, {numero}, é zero.")

elif numero % 2 == 0:
    print(f"O número digitado, {numero}, é par e diferente de 0.")

else:
    print(f"O número digitado, {numero}, é ímpar e diferente de 0.")

'''
3)Solicite 3 números ao usuário,
diga o menor entre eles
'''

n1 = float(input("Digite um número:"))
n2 = float(input("Digite um segundo número:"))
n3 = float(input("Digite um terceiro número:"))

if n3 > n1 < n2:
    print(f"O número {n1} é o menor entre os três.")

elif n3 > n2 < n1:
    print(f"O número {n2} é o menor entre os três.")

elif n1 > n3 < n2:
    print(f"O número {n3} é o menor entre os três.")

elif n1 == n2 == n3:
    print("Todos os números são iguais.")

elif n3 == n2 > n1:
    print(f"O menor número é o {n1}.")

elif n3 == n2 < n1:
    print(f"Os números {n2} e {n3} são iguais, além de serem menores que o número {n1}.")

'''
4)Solicite ao usuário (separadamente) o mês do ano, e o dia atual,
diga também em qual estação estamos
Outono: de 22 de março a 21 de junho
Inverno: de 22 de junho a 23 de setembro
Primavera: de 24 de setembro a 21 de dezembro
Verão: de 22 de dezembro a 21 de março
'''

mes = input("Diga o mês do ano atualmente:").upper()
dia = input("Diga o dia atual:")

if mes == "JANEIRO" or mes == "FEVEREIRO":
    print("Verão!") 

elif mes == "MARÇO":
    if dia <= 21:
        print("Verão!")

    else:
        print("Outono!")


if mes == "ABRIL" or mes == "MAIO":
    print("Outono!") 

elif mes == "JUNHO":
    if dia <= 21:
        print("Outono!")

    else:
        print("Inverno!")


if mes == "JULHO" or mes == "AGOSTO":
    print("Inverno!") 

elif mes == "SETEMBRO":
    if dia <= 21:
        print("Inverno!")

    else:
        print("Primavera!")

if mes == "OUTUBRO" or mes == "NOVEMBRO":
    print("Primavera!") 

elif mes == "DEZEMBRO":
    if dia <= 21:
        print("Primavera!")

    else:
        print("Verão!")

