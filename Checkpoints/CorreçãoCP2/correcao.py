#imprima dois números inteiros, e o segundo número deve ser obrigatoriamente maior que o primeiro

n1 = float(input("Digite um número inteiro:"))
while n1 != int(n1):
    print("Você não digitou um número inteiro!")
    n1 = float(input("Digite um número inteiro:"))

n2 = float(input("Diga um número inteiro, maior que o primeiro:"))
while n2 // 1 != n2 or n2 <=n1:
    print("Você não digitou um número inteiro ou digitou um número maior ou igual ao primeiro.")
    n2 = float(input(f"Diga um número inteiro, maior que o {n1}:"))

n1 = int(n1)
n2 = int(n2)

#solicite dois números ao usuário
#n1 deve ser ímpar e positivo, e n2 deverá ser par e negativo,
#enquanto o usuário digitar um número que não atenda a estas condições,
#o programa deverá dizer exatamente qual característica do número não estava de acordo com o que foi solicitado

n1 = float(input("Diga um número ímpar positivo:"))
while n1 % 2 == 0 or n1 < 0:
    if n1 % 2 == 0 and n1 < 0:
        print("Você digitou um número ímpar negativo!")
        n1 = float(input("Diga um número ímpar positivo:"))

    elif n1 % 2 == 0:
        print("Você digitou um número par!")
        n1 = float(input("Diga um número ímpar positivo:"))

    else:
        print("Você digitou um número negativo!")
        n1 = float(input("Diga um número ímpar positivo:"))

n2 = float(input("Diga um número par negativo:"))
while n2 % 2 != 0 or n2 >= 0:
    if n2 % 2 != 0 and n2 >= 0:
        print("Você digitou um número ímpar positivo!")
        n2 = float(input("Diga um número par negativo:"))

    elif n2 % 2 != 0:
        print("Você digitou um número ímpar!")
        n2 = float(input("Diga um número par negativo:"))

    else:
        print("Você digitou um número positivo!")
        n2 = float(input("Diga um número par negativo:"))
