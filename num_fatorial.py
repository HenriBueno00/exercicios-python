for i in range(3):
    n=int(input("Digite um numero: \n"))
    fat = 1
    for x in range(2, n+1):
        fat = fat * x
    print("O fatorial de ", n, "é: ",fat)
