#prog se62 
peso=float(input("Digite peso: "))
altura=float(input("Digite altura: "))
imc=peso/(altura**2)
if imc<20:
    print("\nabaixo do peso")
elif imc<=25:
    print("\nnormal")
elif imc<=30:
    print("\nexcesso de peso")
elif imc<=35:
    print("\nobesidade")
else:
    print("\nobesidade mórbida\n")


