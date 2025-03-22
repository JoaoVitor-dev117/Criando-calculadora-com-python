print("1:somar")
print("2:subtrair")
print("3:multiplicar")
print("4:dividir")

dado1=input()

numx=int(input("primeiro numero:"))
numx2=int(input("segundo numero:"))

if dado1== "1":
    r =numx+numx2
    print("soma", r)

if dado1=="2":
    r=numx-numx2
    print("subtração", r)

if dado1=="3":
    r=numx*numx2
    print("multiplicação", r)

if dado1=="4":
    if numx2 !=0:
        r=numx/numx2
        print("divisão", r)
    else:
        print("divisão por zero")
