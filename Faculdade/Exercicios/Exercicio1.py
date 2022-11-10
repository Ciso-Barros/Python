# Exercício de fixação 1: Crie um programa que pergunte a idade do usuário. Caso seja maior de idade, deve mostrar uma mensagem informando que pode se inscrever para fazer o teste para tirar a carteira de motorista.

idade = int(input("Digite a idade: "))
if idade >= 18:
    print("Você tem " + str(idade) + " anos, pode fazer fazer carteira de motorista!")
else:
     print("Você tem " + str(idade) + " anos, NÂO pode fazer fazer carteira de motorista!")

