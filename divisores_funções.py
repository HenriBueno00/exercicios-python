def soma_divisores(num):
    total=0
    for i in range(1,num+1):
        if num % i == 0:
            total+=i
    return total
print("Soma dos divisores")
num1=int(input("Digite um numero: "))
resu=soma_divisores(num1)
print("resultado:",resu)
