nomes=[]
idades=[]
for i in range(10):
    nomes.append(input("Digite seu nome: "))
    idades.append(input("Digite sua idade: "))
media=sum(idade)/len(idade)
qtde15=cont=0
for i in range(10):
    if idade[i] > 15:
        qtde15+=1
    if idade[i] < media:
        cont+=1
print("media: ", media)
