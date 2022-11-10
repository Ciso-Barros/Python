nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
if idade>=65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")
print("FIM")

# O último print não está sujeito a condição pois não está identado.