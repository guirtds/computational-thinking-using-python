lista = [9, 4, 7, 1, 5, 8]

lista.append(5)
print(lista)

lista.extend([6,0,4])
print(lista)

# podemos também concatenar listas utilizando o símbolo +

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1+lista2)

# para salvar a concatenação, eu tenho que colocar em uma variável de memória 

lista1 += lista2
#ou
nova_lista = lista1 + lista2

### INSERT
# adiciona um item à lista, ANTES do índice especificado

lista3 = [1, 2, 3, 4, 5]
lista.append(6)
print(lista3)
lista3.insert(2, 6) # o número 6 vai passar a ser o índice 2
print(lista3)
lista3.insert(40, 9) # como a lista não tem 40 elementos , ele vai colocar automaticamente ao final da lista
print(lista3)

### INDEX
# localiza o índice da PRIMEIRA ocorrência de um determinado valor

print("O índice em que o valor aparece pela primeira vez é: " ,lista3.index(6))

# verificando se um valor existe na lista 

print(10 in lista3)
print(6 in lista3)

if 10 in lista3:
    print("O índice em que o valor ocorre pela primeira vez é:" ,lista3.index(10))

else:
    print("Não há o número 10 na lista!")

### COUNT
# conta quantas vezes determinado valor aparece na lista

print("O número 6 aparece" , lista3.count(6), "vezes na lista.")

### EXERCÍCIOS

# remover todos os números "5" da lista usando "while"

lista4 = [1, 5, 7, 5, 5, 9, 6, 87, 4, 5] # len(lista) = 10. Último índice = 9 
i = 0
while i <= len(lista4):
    item_atual = lista4[i]
    if item_atual == 5:
        lista4.remove(5)
        i -= 1
    i += 1
print(lista4)

