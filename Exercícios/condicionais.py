#EXERCÍCIO

'''
Utilizando apenas if e else, faça um programa que peça a idade sua e de um colega e
seus respectivos nomes, e diga, colocando os nomes nas respostas:
1) se seus nomes possuem a mesma quantidade de letras
2) quantos porcento a idade do mais velho representa da idade do mais novo,
limitando a resposta a 1 casa decimal
a) se a pessoa mais velha é maior de idade
b) se a pessoa mais nova é uma criança (possui menos de 12 anos)
3) para cada pessoa, diga:
a) se ela for maior de idade, se ela já se aposentou OU quanto tempo falta para se aposentar
(assumindo que a idade de aposentadoria é 75 anos);
b) se ela for menor de idade, qual sua idade em meses

OBS: criem casos de teste para todas as possibilidades que vocês identificarem
'''

nome_usuario = input("Digite seu nome:")
idade_usuario = float(input("Diga sua idade:"))
nome_colega = input("Digite o nome do seu colega:")
idade_colega = float(input("Diga a idade do seu colega:"))

#1) se seus nomes possuem a mesma quantidade de letras

if len(nome_usuario) == len(nome_colega):
    print("Os nomes possuem o mesmo número de caracteres.")
else:
    print("Os nomes não possuem o mesmo número de letras.")

# 2) quantos porcento a idade do mais velho representa da idade do mais novo,
#limitando a resposta a 1 casa decimal

if idade_usuario > idade_colega:
    porcentagem = idade_usuario / idade_colega * 100
    print("A idade do usuário representa {:.1f} % da idade do {}." .format(porcentagem, nome_colega))
else:
    idade_colega > idade_usuario
    porcentagem = idade_colega / idade_usuario * 100
    print("A idade do colega representa {:.1f} % da idade do {}.".format(porcentagem, nome_usuario))

#a) se a pessoa mais velha é maior de idade

if idade_usuario > idade_colega:
    maioridade = idade_usuario > 18
    print(f"{nome_usuario} já atingiu a maioridade!")
else:
    idade_colega > idade_usuario
    maioridade = idade_colega > 18
    print(f"{nome_colega} já atingiu a maioridade!")












    






