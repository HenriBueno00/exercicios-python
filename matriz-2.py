from random import randint
lin=3
col=5
matriz = []
for i in range(lin):
    linha = []
    for j in range(col):
        linha.append(randint(1,20))
    matriz.append(linha)
    
soma_par=total=media=0
for i in range(lin):
    for j in range(col):
        if matriz[i][j] % 2 == 0 and matriz[i][j] > 10:
            soma_par+=matriz[i][j]
        total+=matriz[i][j]
media=total/(lin* col)
for i in range(lin):
    print(matriz[i])
print('Soma pares da matriz ',soma_par)
print('Média da matriz: ',media)
