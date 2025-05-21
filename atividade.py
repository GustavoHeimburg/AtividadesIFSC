num = float(input("Digite um numero: "))
if num % 1 != 0:
    print("NUmero decimal")
else:
    if int(num) %2 == 0:
        print("Inteiro par")
    else:
        print("Inteiro impar")