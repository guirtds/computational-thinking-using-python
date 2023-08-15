#solicite dois números ao usuário, sendo que o segundo deverá ser obrigatoriamente maior que o primeiro

numero1 = float(input("Digite um número:"))
numero2 = float(input("Digite outro número:"))

while numero2 <= numero1:
    print("O segundo número é menor que o primeiro.")
    numero2 = float(input(f"Digite um número maior que o {numero1}:"))

#solicite ao usuario 2 números
#para cada número do 1 ao primeiro número, faça a tabuada dele do 0 até  segundo número

print()

n1=int(input("Diga qual número será feito a tabuada:"))
n2=int(input("Diga até qual número será feito a tabuada:"))

for i in range(1,n1+1):
    for j in range(n2+1):
        print(f"{i}*{j}=" ,i*j)
    print()

#utilizando while

i=1
while i<=n1:
    j=0
    print("Tabuada do",i)
    while j<=n2:
        print(f"{i}*{j}=" ,i*j)
        j+=1
    i+=1
    print()