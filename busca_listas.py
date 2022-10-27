from random import randint
nomes=["Joao","paulo","laysa","maycon","ze",]
tel=[]
FIM = str
for i in range(5):
    tel.append(int(randint(21545612032,2198546515646513298)))
busca=str(input("digite um  nome: "))
while busca != "fim":
    achou=0
    for i in range(len(nomes)):
        if busca == nomes[i]:
            idx=i
            achou=i
            break
    if achou == 1:
        print("Nome: ",nomes[idx]," - ",tel[idx])
    else:
        print(busca," nao foi encontrado")
    busca=str(input("digite um  nome: "))
