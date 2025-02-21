n = int(input("Digite um numero"))
n2 = int(input("Digite um numero"))
n3 = int(input("Digite um numero"))

media = (n+n2+n3)/3

if media>=7:
    print("Aprovado")
elif media<5:
    print("Reprovado")
else:
    print("Recuperação")