from random import randint
A=[]
B=[]
for i in range(2):
    lin=[]
    lin2=[]
    for j in range(2):
        lin.append(randint(1,10))
        lin2.append(randint(5,20))
    A.append(lin)
    B.append(lin2)
print(" matriz A: ")
for i in range(2):
    print(A[i])
print()

print(" matriz B: ")
for i in range(2):
    print(B[i])
print()

C=[]
for i in range(2):
    lin=[]
    for j in range(2):
        C.append(A[i][j]+B[i][j])
    C.append(lin)
       
print() 
print("Matriz C: ")
for i in range(2):
    print(C[i])
