'''
ORDENAÇÃO DE LISTAS

- Processo intuitivo:

* percorrer lista
* comparo o len(lista) -1 vezes -> descubro o maior ou o menor valor
* trago o menor par a primeira posição ou o maior para a útltima posição
* comparo len(lista) -2 vezes -> descubro o maior ou o segundo menor
* trago o 2° menor para a segunda menor posição ou o segundo maior para a penúltima posição

- este raciocínio intuitivo é chamado de SELECTION SORT

- uma segunda forma de pensar:

* percorrer a lista
* selecionar o item e comparar com o vizinho
* caso seja maior, trocar, caso não seja, andar para o lado
* ao chegar ao final, voltar ao começo da lista 

[1, 0, 5, 3, 9, 8] -> [0, 1 , 5, 3, 9, 8] -> [0, 1, 3, 5, 9, 8] -> [0, 1, 3, 5, 8, 9]

'''

lista1 = [1, 0, 5, 3, 9, 8]
lista2 = [1, 0, 5, 3, 9, 8]

# programando o selection sort

# programando o bubble sort
