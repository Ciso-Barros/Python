# Exemplo de aplicação 1: Elabore um programa que solicite ao usuário o cadastro de endereços para entrega de produtos de uma loja.

enderecos = []
print("\nCadastro de Endereços de Entrega\n")
while True:
    logradouro = input("Digite o logradouro: ")
    numero = int(input("Digite o número: "))
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    novo_endereco = (logradouro, numero, bairro, cidade, estado)
    enderecos.append(novo_endereco)
    if input("Deseja cadastrar um novo endereço (s/n): ") == "n":
        break
print("Os endereços cadastrados são:")
for i in range(0, len(enderecos)):
    endereco = enderecos[i]
    print(f"{i}. {endereco[0]}, {endereco[1]}, {endereco[2]} - {endereco[3]}/{endereco[4]}")
