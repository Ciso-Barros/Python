tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))

# Valores da range ( x, y, z) x é onde inicia, y é onde termina ou seja, não estará no resultado, z é o incremento, exemplo de 1 em 1, de 2 em 2... 