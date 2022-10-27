for i in range(5):
    n=int(input("Digite um numero: "))
    soma_imp=0
    for x in range(1, n + 1):
          if x % 2 == 1:
              soma_imp+=x
    print("A soma dos impares ",n,"é",soma_imp)
