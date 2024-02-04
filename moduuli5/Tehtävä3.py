numero = int(input("Syötä kokonaisluku: "))

if numero > 0:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f"{numero} ei ole alkuluku.")
            break
    else:
        print(f"{numero} on alkuluku.")
