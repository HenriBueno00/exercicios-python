def soma_pares(num1,num2):
    soma=0
    if num1 <= num2:
        for i in range(num2,num1+1):
            if i % 2 == 0:
                soma+=i
    else:
        for i in range(num2,num1+1):
            if i % 2 == 0:
                soma+=i
    return(soma)
print("Programa Python -função soma pares")
num1=int(input("Digite um número: "))
num2=int(input("Digite um número: "))
res=soma_pares(num1,num2)
print("A soma é ",res)
