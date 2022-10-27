num=[]
media=0
impar=pares=0
pocentagem=0
for i in range(10):
    num.append(int(input("Digite um numero: ")))
media=sum(num)/len(num)
qtde15=cont=0
for i in range(10):
    if num[i] > 15:
        qtde15+=1
    if num[i] > media:
        cont+=1
    if num % 2 == 0:
        pares+=1
    if num % 2 == 1:
        impar+=1
print("qtde de numeros maiores que 15:",qtde15)
print("qtde de numeros maiores que a media:",cont)
print("qtde de numero pares:",pares)
print("qtde de numeros impares:",impar)
