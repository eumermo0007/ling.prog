n = int(input("Escreva um numero"))
a = 0
b = 1
c = 0
for i in range(n):
    print(a,b)
    c = a
    a = b
    b = c+b