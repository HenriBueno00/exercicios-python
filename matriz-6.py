from random import randint
matriz=[]
for i in range(3):
    linha=[]
    for j in range(5):
        linha.append(randint(1,20))
    matriz.append(linha)
primo=[]
soma=qtd=0
maior=matriz[0][0]
pos_i=pos_j=0
impar=total=media=0
num=0
for i in range(3):
    for j in range(5):
        if matriz[i][j] > maior:
            maior=matriz[i][j]
            pos_i=i
            pos_j=j
        cont_div=0
        num=matriz[i][j]
        for k in range(1,num+1):
            if num % k == 0:
                cont_div+=1
        if cont_div == 2:
            primo.append(num)
                
        if matriz[i][j] % 2 == 1:
            soma+=matriz[i][j]
            qtd+=1
if qtd > 0:
    media=soma/qtd
for i in range(3):
    print(matriz[i])
print("O maior numeoro:",maior," indices ",pos_i," - ",pos_j)
print("Os numeros primos:",num)
print("A media dos numeros impares é:",media)
