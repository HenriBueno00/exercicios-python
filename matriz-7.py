m=[]
for i in range(10):
    linha = []
    linha.append(input('Digite o nome da pessoa ' +str(i+1) + ':'))
    linha.append(int(input('Digite a idade de ' + linha[0] + ':')))
    m.append(linha)
menor=m[0][1] #procura a pessoa mais nova
pos= 0
for i in range(10):
    if m[i][1] < menor:
        menor = m[i][1]
        pos= i
for i in range(10):
    print(m[i])
print('A pessoa mais nova é', m[pos][0])
