matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input('Digite o valor de :')))
    matriz.append(linha)
pares=0
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            pares+=1
for i in range(3):
    print(matriz[i])
print('A matriz contém', pares, ' números pares')
