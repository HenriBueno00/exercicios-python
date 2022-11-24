from random import randint

def pares(mat):
    qtd=0
    for i in range(3):
        for j in range(3):
            if mat[i][j] % 2 == 0:
                qtd+=1
    return qtd

def diagonal(mat):
    soma=0
    for i in range(3):
        for j in range(3):
            if i == j:
                soma+=mat[i][j]
    return soma

def media_mat(mat):
    for i in range(3):
        for j in range(3):
            media+=mat[i][j]
    media=media/len(mat) * len(mat[0])
    return media


mat=[]
for i in range(3):
    lin=[]
    for j in range(3):
        lin.append(randint(10,20))
    mat.append(lin)

print("------------------matriz--------------------")      
for i in range(3):
    for j in range(3):
        print(mat[i][j])  
print("-----------funçoes----------")
print("Qtde pares:",pares(mat))
print("soma da diagonal:",diagonal(mat))
print("A media é:",media_mat(mat))
