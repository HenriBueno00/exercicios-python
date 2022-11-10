def soma(n1,n2):
    total=0
    if n1 <= n2:
        for k in range(n1,n2+1):
            total+=k
    else:
        for k in range(n2,n1+1):
            total+=k
    return total

print("----Funçaõ Soma----")
num1=int(input("Digite um numero para n1: "))
num2=int(input("Digite um numero para n2: "))
resu=soma(num1, num2)
print("O resultado é: ",resu)
