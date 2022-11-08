def fatorial(num):
    if num > 0:
        fat=1
        for i in range(1,num+1):
            fat=fat*1
    else:
        fat=0
    return(fat)
print("Programa")
num1=int(input("Digite um valor:"))
res=fatorial(num1)
print("O fatotial de,",num1,",é ",res)
