from random import randint
matriz=[]
for i in range(4):
    linha=[]
    for j in range(3):
        linha.append(randint(1,20))
    matriz.append(linha)
for i in range(4):
    print(matriz[i])
qtde=media=soma=0
vetor=[]
for i in range(4):
    for j in range(3):
        vetor.append(matriz[i][j])
        if i == 2:
            media = sum(matriz[i])/len(matriz[i])
        if j == 1:
            soma+=matriz[i][j]
        if matriz[i][j] > 5 and matriz[i][j] < 15:
            qtde+=1
print('A quantidade de numeros maiores que 5 e menores que 15 é:',qtde)
print('A media da 3° linha da matriz é:',media)
print('A soma da 2° coluna da matriz é:',soma)
print('Vetor com os valores da matriz:',vetor)
