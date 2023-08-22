import numpy as np

A =[[4,-1,0,0],
    [-1,4,-1,0],
    [0,-1,4,-1],
    [8,0,-1,4]]

X = [0,0,0,0]

X2=[0,0,0,0]


B =[1,1,1,1]

error = 1*10**-4
maxit = 100
it=0
for it in range(maxit):
    X3=X2.copy()
    print("Iteracion #",it+1)
    it=it+1
    for i in range(len(A)):
        sum =0
        for j in range(len(A)):
            div=A[i][i]
            if i!=j:
                sum = sum + A[i][j]*X[j]
        X2[i]=((B[i]-sum)/div) 
    X=X2
    
    print("[X1",X[0],"X2",X[1],"X3",X[2],"X4",X[3],"]") 

    pot =np.power(X3[i]-X2[i],2)
    raiz = np.sqrt(pot)
    print("Norma: ",raiz)

    if raiz<error:
        break
    elif it>maxit-1:
        print("El metodo diverge")
        break
    