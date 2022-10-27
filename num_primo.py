soma_pri=0
for i in range(5):
    n=int(input("Digite um numero: \n"))
    cont=0
    for j in range(1,n+1):
        if n % j == 0:
            cont+=1

    if cont == 2:
        soma_pri += n
        print(n," é primo")
    else:
        print(n," não é primo")

print("A soma dos primos é: ",soma_pri)
