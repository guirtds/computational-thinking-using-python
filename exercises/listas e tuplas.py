#Crie uma função que encontre e retorne o menor e o maior valor da lista, e seus índices sem utilizar a função nativa do
#python (min e max)

lista=[1,5,7,5,5,9,6,87,4,5]

def encontra_extremos(lista):

    maior = float("-inf")
    menor = float("inf")

    for i in lista:
        if i > maior:
            maior = i

        if i < menor:
            menor = i

    indice_maior = lista.index(maior)
    indice_menor = lista.index(menor)

    return maior, menor, indice_maior, indice_menor

maior, menor, indice_maior, indice_menor = encontra_extremos(lista)

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
print(f"O maior índice da lista está na posição {indice_maior}")
print(f"O menor índice da lista está na posição {indice_menor}")


#Tuplas

#Tuplas são basicamente listas que não podem ser alteradas, as funções das listas que são válidas para as tuplas
#são todas aquelas que não permitem uma possível alteração, como por exemplo (remove, append, etc)

#Para criar uma tupla é necessário a utilização de vírgulas

tupla_1 = (1,2,3,4,5)
#ou
tupla_2 = 1,2,3,4,5
