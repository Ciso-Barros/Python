# Trabalho de entrega para da Semana 4 do aluno Tarcísio Henrique Sampaio Barros 
# Código de Aluno: 02763844235
# Nome de usuário: 1112022207198 


# Biblioteca para gerar números "Aleatórios"
import random
from time import sleep

# 
print ("\033[0;35m=====================================================================================\033[0m\n")
print ("\033[0;35m\033[1;36m ## TRABALHO DE LÓGICA DE PROGRAMAÇÃO - PYTHON (Protótipo completo da Semana 8 \033[0m)")
print ("\033[1;36m Aluno: Tarcísio Henrique Sampaio Barros\033[0m ")
print ("\033[1;36m Número de usuário: 1112022207198\033[0m\n")
print ("\033[0;35m=====================================================================================\033[0m\n")
print ("\033[0;32mBem-vindo ao jogo Zombie Dice!\033[0m\n")


num_de_Jogadores = 0


# O laço While  garante a condição de no mínimo dois jogadores...
while (num_de_Jogadores < 2):

    # Entrada de dados, para informar o número de jogadores
    num_de_Jogadores = int(input("Digite o número de jogadores: "))

    if (num_de_Jogadores < 2):
        print("\n\033[1;33mAVISO: Você precisa de pelo menos 2 jogadores!\033[0m\n")

# Lista de jogadores que será armezanado na variável
lista_de_jogadores = []


# Entrada de dados para armazenar o nome dos jogador na ordem da lista. 
for i in range(0, num_de_Jogadores):

    nomes = input (f'\nInforme o nome do {i + 1}° Jogador: ').upper()

    lista_de_jogadores.append(nomes)


# Lista de dados informados no enunciado da questão 
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



print ("\n\033[1;34mIniciando o jogo...!\033[0m\n")

# variáveis iniciais do jogo. 
jogador_atual = 0
dados_sorteados = []
tiros = 0
cerebros = 0
passos = 0
pontos = []

# Após o sorteio do número através da biblioteca um dado será selecionado e sua cor/tipo é informada ao jogador.
for i in range(0, num_de_Jogadores):
    pontos.append(0)

def sorteamento_dados (cor_dado = ()):
    for n in range (0, 3):
        num_sorteado = random.randrange(12)
        dado_sorteado = lista_dados[num_sorteado]
        if dado_sorteado == dado_verde():
            cor_dado = '\033[32mVERDE\033[m'
        elif dado_sorteado == dado_amarelo():
            cor_dado = '\033[33mAMARELO\033[m'
        elif dado_sorteado == dado_vermelho():
            cor_dado = '\033[31mVERMELHO\033[m'

        print("O dado sorteado foi o -->>", cor_dado)
        
        dados_sorteados.append(dado_sorteado)
        sleep(1)
    
# Com base no número gerado, um dado é selecionado, e sua cor (tipo) é informada ao jogador, bem como sua faces.

while True:

    print('\nTurno do jogador:  ',lista_de_jogadores[jogador_atual])

    sorteamento_dados()

    for dado_sorteado in dados_sorteados:
        num_faces = random.randint(0, 5)
        if dado_sorteado[num_faces] == "C":
            print(f'\n{lista_de_jogadores[jogador_atual]} comeu um CÉREBRO!')
            cerebros += 1

        elif dado_sorteado[num_faces] == "T":
            print(f'\n{lista_de_jogadores[jogador_atual]} levou um TIRO!')
            tiros += 1

        else:
            print(f'\n{lista_de_jogadores[jogador_atual]} tirou um PASSO! Sua vítima escapou!')
            passos += 1
    sleep(1)

# Mostra os dados

    print("\n\033[5;30m***PONTUAÇÃO ATUAL***\033[0m")
    print(f"CÉREBROS: {cerebros}" )
    print(f"TIROS: {tiros}\n")

# Verifica pontução e a rodado  do  jogador



    if tiros > 2:
        print(f'\n\033[41;1;37m{lista_de_jogadores[jogador_atual]} perdeu essa rodada! Levou, {tiros} tiros\033[0m')
        tiros = 0
        cerebros = 0
        passos = 0
        dados_sorteados = []
        jogador_atual += 1


        if jogador_atual == len(lista_de_jogadores):
            jogador_atual = 0
            print('\nPróxima rodada, agora é a vez do jogador: ', lista_de_jogadores[jogador_atual])

    else:
        continuar_turno = str(input(f'\033[0;35m{lista_de_jogadores[jogador_atual]} deseja continuar? [S/N]  \033[0m')).strip().upper()[0]

        if (continuar_turno == "N"):
            pontos[jogador_atual] += cerebros
            jogador_atual += 1
            dados_sorteados = []
            tiros = 0
            cerebros = 0
            passos = 0

            if (jogador_atual == len(lista_de_jogadores)):
                jogador_atual = 0

    if pontos [jogador_atual] >= 13:
        print('Parabéns', lista_de_jogadores[jogador_atual], 'você VENCEU!!!')
        print("\nFinalizando o protótipo do jogo")
        break

    dados_sorteados.clear()

    for i in range (0, num_de_Jogadores):
        print(lista_de_jogadores[i], pontos[i], 'pontos', end='')
    print()

print("Fim de jogo!")