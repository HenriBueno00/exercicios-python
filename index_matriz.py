from random import randint
mat=[]
soma=[]
for i in range(3):
    lin=[]
    for j in range(3):
        lin.append(randint(1,10))
    soma.append(sum(lin))
    mat.append(lin)
maior=max(soma)
idx=soma.index(maior)
print(' matriz ')
for i in range(3):
    print(mat[i])
print('Linha com maior soma')
print(mat[idx])
print("A soma é: ",maior)
