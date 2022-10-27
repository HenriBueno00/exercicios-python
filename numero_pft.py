i = 0
while i > 0:
    n=int(input("Digite um numero"))
    soma = 0
    for i in range(1, n):
        if (n % i == 0):
            soma = soma + 1

    if soma == 0:
        print(n,"  é perfeito")
    else:
        print(n," não é perfeito")
    n=int(input("Digite um numero"))
