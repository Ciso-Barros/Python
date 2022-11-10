# Trabalho de entrega para da Semana 4 do aluno Tarcísio Henrique Sampaio Barros 
# Código de Aluno: 02763844235
# Nome de usuário: 1112022207198 


# Biblioteca para gerar números "Aleatórios"
import random
from time import sleep

# Tela  Inicial
print ("##### ###################################################")
print ("--- ZOMBIE DICE (Protótipo da Semana 4) ---")
print ("Aluno: Tarcísio Henrique Sampaio Barros ")
print ("Número de usuário: 1112022207198")
print ("##### ###################################################\n")
print ("Bem-vindo ao jogo Zombie Dice!\n")


num_de_Jogadores = 0


# O laço While  garante a condição de no mínimo dois jogadores...
while (num_de_Jogadores < 2):

    # Entrada de dados, para informar o número de jogadores
    num_de_Jogadores = int(input("Digite o número de jogadores: "))

    if (num_de_Jogadores < 2):
        print("AVISO: Você precisa de pelo menos 2 jogadores!\n")

# Lista de jogadores que será armezanado na variável
lista_de_jogadores = []


# Entrada de dados para armazenar o nome dos jogador na ordem da lista. 
for i in range(0, num_de_Jogadores):

    nomes = input (f'Informe o nome do {i + 1}° Jogador: ').upper()

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



print ("\nIniciando o jogo...!\n")

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
    for n in range (0, 2):
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
    
sorteamento_dados()