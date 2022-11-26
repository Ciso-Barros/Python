# Aluno: Matheus Vicente Martins Castro (RA: 1112022202021) Curso: Raciocínio Computacional (11100010563_20222_01)
# Professor: Galbas Milleo Filho

import random
from time import sleep
# Biblioteca para gerar números randômicos

print("ZOMBIE DICE (Protótipo Semana 8) ")
print("Seja bem-vindo ao jogo Zombie Dice!")
# Tela de boas-vindas

num_jogadores = 0

while (num_jogadores < 2):
# Para este jogo, são necessários, ao menos, 2 jogadores. O laço While garante que essa condição seja satisfeita

    num_jogadores = int(input("Informe a quantidade de jogadores: "))
    print("O total de jogadores é {}".format (num_jogadores))

    if (num_jogadores < 2):
        print("AVISO: Você precisa de pelo menos 2 jogadores!")

lista_jogadores = []

for c in range (0, num_jogadores):
# Entrada de dados, para informe do nome do jogador

    nome = input(f'Digite o nome do {c + 1}º jogador: ').upper()
    lista_jogadores.append(nome)
    # Adiciona um jogador a lista de jogadores

def dado_verde():
    dadoVerde = ("C", "P", "C", "T", "P", "C")
    return dadoVerde

def dado_amarelo():
    dadoAmarelo = ("T", "P", "C", "T", "P", "C")
    return dadoAmarelo

def dado_vermelho():
    dadoVermelho = ("T", "P", "T", "C", "P", "T")
    return dadoVermelho

lista_dados = [
    dado_verde(), dado_verde(), dado_verde(), dado_verde(), dado_verde(), dado_verde(),
    dado_amarelo(), dado_amarelo(), dado_amarelo(), dado_amarelo(),
    dado_vermelho(), dado_vermelho(), dado_vermelho()
]
    # Lista de dados previamente estipulada pelo enunciado da questão


print("Iniciando o jogo!")

jogador_atual = 0
dados_sorteados = []
tiros = 0
cerebros = 0
passos = 0
pontos = []

# Variáveis iniciais (condição orignal do jogo)

for i in range(0, num_jogadores):
    pontos.append(0)

def sorteamento_dados (cor_dado = ()):
    for n in range (0, 2):
        num_sorteado = random.randrange(12)
        dado_sorteado = lista_dados[num_sorteado]
        if dado_sorteado == dado_verde():
            cor_dado = "VERDE"
        elif dado_sorteado == dado_amarelo():
            cor_dado = "AMARELO"
        elif dado_sorteado == dado_vermelho():
            cor_dado = "VERMELHO"

        print("O dado sorteado foi", cor_dado)
        dados_sorteados.append(dado_sorteado)
        sleep(1)

# Com base no número gerado, um dado é selecionado, e sua cor (tipo) é informada ao jogador, bem como sua faces

while True:

    print('Turno do jogador: ', lista_jogadores[jogador_atual])

    sorteamento_dados()

    for dado_sorteado in dados_sorteados:
        num_faces = random.randint(0, 5)
        if dado_sorteado[num_faces] == "C":
            print('Você comeu um CÉREBRO!')
            cerebros += 1

        elif dado_sorteado[num_faces] == "T":
            print('Você levou um TIRO!')
            tiros += 1
        else:
            print('Você tirou um PASSO! Sua vítima escapou!')
            passos += 1
    sleep(1)

# Escolhe uma face do dado, de acordo com a categoria (Ex. Se a face foi T, então o jogador levou um tiro).

    print("===SCORE ATUAL===")
    print("CÉREBROS: ", cerebros)
    print("TIROS: ", tiros)

# Soma a quantidade de passos, tiros e score do jogador

    if tiros > 2:
        print('Você perdeu essa rodada! Levou, ', tiros, ' tiros')
        tiros = 0
        cerebros = 0
        passos = 0
        dados_sorteados = []
        jogador_atual += 1

        if jogador_atual == len(lista_jogadores):
            jogador_atual = 0
            print('Indo para a próxima rodada, jogador: ', lista_jogadores[jogador_atual])

    else:
        continuar_turno = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]

        if (continuar_turno == "N"):
            pontos[jogador_atual] += cerebros
            jogador_atual += 1
            dados_sorteados = []
            tiros = 0
            cerebros = 0
            passos = 0

            if (jogador_atual == len(lista_jogadores)):
                jogador_atual = 0

    if pontos [jogador_atual] >= 13:
        print('Parabéns', lista_jogadores[jogador_atual], 'você VENCEU!!!')
        print("Finalizando o protótipo do jogo")
        break

    dados_sorteados.clear()

    for i in range (0, num_jogadores):
        print(lista_jogadores[i], pontos[i], 'pontos', end='')
    print()

print("Fim de jogo!")
