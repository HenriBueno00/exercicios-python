#Crie uma função que receba um número inteiro como parâmetro e verifique se ele é primo ou não,e exibindo uma mensagem dentro da função.
def primo(num):
    cont_div=0
    for i in range(1,num+1):
        if num % i == 0:
            cont_div+=1
    if cont_div == 2:
        print("O numero "+str(num)+ " é primo")
    else:
        print("O numero "+str(num)+ " não é primo")
print("----Programa principal----")
n1=int(input("Digite um numero:"))
primo(n1)
