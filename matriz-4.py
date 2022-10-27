from random import randint
matriz=[]
for i in range(5):
    linha=[]
    for j in range(3):
        linha.append(randint(1,20))
    matriz.append(linha)
multi=soma=media=0
for i in range(5):
    print(matriz[i])
for i in range(5):
    for j in range(3):
        if matriz[i][j] % 3 == 0:
            multi+=1
        if matriz[i][j] % 2 == 0 and matriz[i][j] > 10:
           soma+=matriz[i][j]
        media = media + matriz[i][j]
media = media / len(matriz)
print('A matriz tem numeros multiplos de 3:',multi)
print('A soma de pares na matriz é:',soma)
print('A media da matriz é:',media)
