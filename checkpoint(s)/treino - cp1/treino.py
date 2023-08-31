'''
1) Crie uma função que receba como parâmetros o nome e o número do mês de aniversário de uma pessoa.
Esta função deverá criar um dicionário com esta pessoa da seguinte forma:
{"Nome": nome , "Aniversario": mes}, onde o mês deverá ser escrito em forma de palavra de 3 letras 
(jan,fev,mar,...,dez etc). Além disso, adicione esta pessoa (dicionário) a um arquivo txt, cada um em uma linha.
Este arquivo deve conter, ao final, todos os dicionários criados (ou seja, sem perder informação).

Antes de salvar o dicionário em um arquivo txt, 
a função deverá salvar cada dicionário individualmente em um arquivo JSON, cujo nome deverá ser "nome_mes.json"
Ex: "paulo_jun.json"
'''

import os
import json

def exercicio1(nome, num_mes):
    
    dicio_mes = {1:"jan", 2:"fev", 3:"mar", 4:"abr", 5:"mai", 6:"jun", 7:"jul", 8:"ago", 9:"set", 10:"out", 11:"nov", 12:"dez"}
    
    mes_palavra = dicio_mes[num_mes] # entregando a chave para receber o valor daquela chave

    # criando o dicionário
    dicio_pessoa = {"Nome": nome, "Aniversario": mes_palavra}

    # salvando em um arquivo json

    with open(f"{nome}_{mes_palavra}.json", "w") as arquivo_json:
        # a função "dump" necessita de 2 argumentos:
        # o item a ser salvo (dicionário)
        # e o arquivo que vai receber o item (neste exemplo, o "arquivo_json")
        json.dump(dicio_pessoa, arquivo_json)

    # para escrever, basta abrir o arquivo
    # neste caso, tem que utilizar o "a", para somente adicionar itens no dicionário que já foi criado, pois o "w" apagaria o dicionário já existente e depois disso incrementaria um novo

    with open("exercicio1.txt", "a") as arquivo_txt:
        arquivo_txt.write(str(dicio_pessoa))
        arquivo_txt.write("\n")

exercicio1("João", 9)
exercicio1("Maria", 7)
exercicio1("Guilherme", 5)

'''
2) Utilizando o "os.listdir()" no caminho onde foram salvos os arquivos json, faça um loop que carregue todos os arquivos json (um por um) e os coloque em uma nova lista de nomes
'''

caminho = os.getcwd() # função que retorna o CWD (Current Work Directory), (Diretório Atual de Trabalho)

print(caminho)
lista_arquivos = os.listdir(caminho) 

# o "listdir" retorna uma lista com os nomes dos arquivos neste diretório

lista_nova = []

for i in lista_arquivos:
    nome_dividido = i.split(".")
    ext = nome_dividido[-1]
    if ext == "json": # deve-se abrir o arquivo para poder ler

        with open(i, "r") as arquivo:
            conteudo = json.load(arquivo) # salvando na memória o conteúdo

            lista_nova.append(conteudo) # adicionando à lista o dicionário
print(lista_nova)
        