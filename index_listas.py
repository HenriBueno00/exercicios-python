from random import randint
nomes=["Henrique","Bueno","Fonseca","Laysa","Aparecida","Dias","Livia","Janaina","Marco","Leandro"]
idade=[]
for i in range(10):
    idade.append(int(randint(10,50)))
media=sum(idade)/len(idade)
maior_idade=max(idade)
menor_idade=min(idade)
idx_maior=idade.index(maior_idade)
idx_menor=idade.index(menor_idade)


cont=qtde=0
for i in range(10):
    if idade[i] > 15:
        cont+=1
    if idade[i] < media:
        qtde+=1
print(nomes)
print(idade)
print("A maior idade é: ",maior_idade," - ",nomes[idx_maior])
print("A menor idade é: ",menor_idade," - ",nomes[idx_menor])
