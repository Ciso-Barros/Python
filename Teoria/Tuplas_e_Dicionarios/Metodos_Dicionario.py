
# Exemplos de aplicação de métodos sobre dicionários:

agenda = {"Maria": "(41) 98765-4321", "João": "(11) 12345-6789", "Rosana": "(21) 91827-3645"}
print(agenda)
# adiciona um novo elemento no vetor
agenda["José"] = "(19) 98877-1122"
print(agenda)
# cria um dicionário com chaves e valores específicos
chaves = ["chave1", "chave2", "chave3"]
valores = "valor"
novo_dicionario = dict.fromkeys(chaves, valores)
print(novo_dicionario)
# mostra a lista de itens do dicionário
print(agenda.items())
# mostra a lista de chaves do dicionário
print(agenda.keys())
# mostra a lista de valores do dicionário
print(agenda.values())
# remove um item de chave específica
agenda.pop("Maria")
print(agenda)
# remove o último item inserido
agenda.popitem()
print(agenda)
# retorna ou insere o valor de uma chave em específico
print(agenda.setdefault("Rosana", "(21) 91827-3645"))
print(agenda.setdefault("Maria", "(41) 98765-4321"))
print(agenda)
# adiciona o conteúdo de um dicionário a outro
agenda.update(novo_dicionario)
print(agenda)
# limpa o conteúdo de um dicionário
agenda.clear()
print(agenda)
