from random import randint
salarios=[]
n_filhos=[]
for i in range(10):
    salarios.append(randint(500,5500))
    n_filhos.append(randint(0,4))
media_salarios=sum(salarios)/len(salarios)
media_filhos=sum(n_filhos)/len(n_filhos)
maior=max(salarios)

cont=cont_filhos=inferior=0
for i in range(10):
    if salarios[i] > media_salarios:
        cont+=1
    elif n_filhos[i] > media_filhos:
        cont_filhos+=1
    elif salarios[i] > maior:
        maior = salarios[i]
    elif salarios[i] < 1000:
        inferior+=1
        
percentual=(inferior/len(salarios)) * 100
print("Media de salarios: ", media_salarios)
print("Media de n° de filhos: ",media_filhos)
print("Maior salario: ", maior)
print("Salarios menor que R$1000: ",inferior)
