#Exercícios

#01) Escreva uma função que execute e retorne a soma e multiplicação de todos os núemros digitados pelo usuário

def soma_multiplica(*args):
    soma = 0
    multiplica = 1
    for i in args:
        soma += i
        multiplica = multiplica * i
    return soma,multiplica

soma, produto = soma_multiplica(5, 7, 1, 9, -68, 49, 147, 2)
print(f"A soma dos números é {soma}, e o produto dos números é {produto}.")

    #Escreva uma função que receba três números como parâmetros: n, maiaor, menor
    #e retorne dizendo se n está entre maior e menor

def esta_entre(n, maior, menor):
        if menor < n < maior:
            return(f"O número {n} está entre os números {menor} e {maior}.")

        return(f"O número {n} não está entre os números {maior} e {menor}.")
    
resposta = esta_entre(5, 20, 10)
print(resposta)