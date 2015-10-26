# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:04:19 2015

@author: david
"""

print("Olá! Bem vindo(a) a minha Batalha Naval! A seguir, voce encontrará um tabuleiro de 10 por 10, no qual estão escondidos 3 barcos de tamanhos diferentes! O menor possui tamanho 3, o intermediario, 4 e o maior, tamanho 5. Tente acertá-los com seus tiros e divirta-se! \n")

from random import randint

# Criando a matriz 10 por 10
matriz = []
for m in range(10):
    matriz.append(["O"] * 10)
        
# Fazendo com que os componentes da matriz fiquem separados por espaços        
def tabuleiro(matriz):
    for linha in matriz:
        print (" ".join(linha))
tabuleiro(matriz)
print(" ")
        
# Barco 1
def linha(matriz):
    return randint(0, len(matriz) - 1)
def coluna(matriz):
    return randint(0, len(matriz[0]) - 1)
linha1 = linha(matriz)
coluna1 = coluna(matriz)

# Barco 2
linha2 = linha(matriz)
coluna2 = coluna(matriz)

# Barco 3
linha3 = linha(matriz)
coluna3 = coluna(matriz)

# Sorteia de novo se a linha 1 eh igual a 2
while linha1 == linha2 or linha1 == linha3 or linha2 == linha3:
    linha2 = linha(matriz)
    linha3 = linha(matriz)
        
# Direçao do corpo do barco
def direcao():
    dir = randint(1,4)
    if dir == 1:
        return "direita"
    elif dir == 2:
        return "cima"
    elif dir == 3:
        return "esquerda"
    elif dir == 4:
        return "baixo"
        
# Barco 1 (tamanho 3)   
while True:
    d = direcao() # determina a direcao
    if d == "cima":
        if coluna1 >= 2:
            linha1_2 = linha1 - 1
            coluna1_2 = coluna1
            linha1_3 = linha1 - 2
            coluna1_3 = coluna1
            break
    if d == "direita":
        if coluna1 <= 7:
            linha1_2 = linha1
            coluna1_2 = coluna1 + 1
            linha1_3 = linha1
            coluna1_3 = coluna1 + 2
            break
    if d == "baixo":
        if linha1 <= 7:
            linha1_2 = linha1 + 1
            coluna1_2 = coluna1
            linha1_3 = linha1 + 2
            coluna1_3 = coluna1
            break
    if d == "esquerda":
        if coluna1 >= 2:
            linha1_2 = linha1
            coluna1_2 = coluna1 - 1
            linha1_3 = linha1
            coluna1_3 = coluna1 - 2
            break
barco1 = [(linha1,coluna1), (linha1_2,coluna1_2), (linha1_3,coluna1_3)]

# Barco 2 (tamanho 4)
while True:
    d = direcao() # determina a direcao
    if d == "cima":
        if coluna2 >= 3:
            if (linha2 - 1,coluna2) not in barco1 and (linha2 - 2,coluna2) not in barco1 and (linha2 - 3,coluna2) not in barco1:
                linha2_2 = linha2 - 1
                coluna2_2 = coluna2
                linha2_3 = linha2 - 2
                coluna2_3 = coluna2
                linha2_4 = linha2 - 3
                coluna2_4 = coluna2
                break
    if d == "direita":
        if coluna2 <= 6:
            if (linha2 ,coluna2 + 1) not in barco1 and (linha2,coluna2 + 2) not in barco1 and (linha2,coluna2 + 3) not in barco1:
                linha2_2 = linha2
                coluna2_2 = coluna2 + 1
                linha2_3 = linha2
                coluna2_3 = coluna2 + 2
                linha2_4 = linha2
                coluna2_4 = coluna2 + 3
                break
    if d == "baixo":
        if linha2 <= 6:
            if (linha2 + 1 ,coluna2) not in barco1 and (linha2 + 2,coluna2) not in barco1 and (linha2 + 3,coluna2) not in barco1:
                linha2_2 = linha2 + 1
                coluna2_2 = coluna2
                linha2_3 = linha2 + 2
                coluna2_3 = coluna2
                linha2_4 = linha2 + 3
                coluna2_4 = coluna2
                break
    if d == "esquerda":
        if coluna2 >= 3:
            if (linha2 ,coluna2 - 1) not in barco1 and (linha2,coluna2 - 2) not in barco1 and (linha2,coluna2 + 3) not in barco1:
                linha2_2 = linha2
                coluna2_2 = coluna2 - 1
                linha2_3 = linha2
                coluna2_3 = coluna2 - 2
                linha2_4 = linha2
                coluna2_4 = coluna2 - 3
                break
barco2 = [(linha2,coluna2), (linha2_2,coluna2_2), (linha2_3,coluna2_3), (linha2_4,coluna2_4)]

# Barco 3 (tamanho 5)
while True:
    d = direcao() # determina a direcao
    if d == "cima":
        if coluna3 >= 4:
            if (linha3 - 1,coluna3) not in barco1 and (linha3 - 1,coluna3) not in barco2 and (linha3 - 2,coluna3) not in barco1 and (linha3 - 2,coluna3) not in barco2 and (linha3 - 3,coluna3) not in barco1 and (linha3 - 3,coluna3) not in barco2 and (linha3 - 4,coluna3) not in barco1 and (linha3 - 4,coluna3) not in barco2: 
                linha3_2 = linha3 - 1
                coluna3_2 = coluna3
                linha3_3 = linha3 - 2
                coluna3_3 = coluna3
                linha3_4 = linha3 - 3
                coluna3_4 = coluna3
                linha3_5 = linha3 - 4
                coluna3_5 = coluna3
                break
    if d == "direita":
        if coluna3 <= 5:
            if (linha3,coluna3 + 1) not in barco1 and (linha3,coluna3 + 1) not in barco2 and (linha3,coluna3 + 2) not in barco1 and (linha3,coluna3 + 2) not in barco2 and (linha3,coluna3 + 3) not in barco1 and (linha3,coluna3 + 3) not in barco2 and (linha3,coluna3 + 4) not in barco1 and (linha3,coluna3 + 4) not in barco2: 
                linha3_2 = linha3
                coluna3_2 = coluna3 + 1
                linha3_3 = linha3
                coluna3_3 = coluna3 + 2
                linha3_4 = linha3
                coluna3_4 = coluna3 + 3
                linha3_5 = linha3
                coluna3_5 = coluna3 + 4
                break
    if d == "baixo":
        if linha3 <= 5:
            if (linha3 + 1,coluna3) not in barco1 and (linha3 + 1,coluna3) not in barco2 and (linha3 + 2,coluna3) not in barco1 and (linha3 + 2,coluna3) not in barco2 and (linha3 + 3,coluna3) not in barco1 and (linha3 + 3,coluna3) not in barco2 and (linha3 + 4,coluna3) not in barco1 and (linha3 + 4,coluna3) not in barco2: 
                linha3_2 = linha3 + 1
                coluna3_2 = coluna3
                linha3_3 = linha3 + 2
                coluna3_3 = coluna3
                linha3_4 = linha3 + 3
                coluna3_4 = coluna3
                linha3_5 = linha3 + 4
                coluna3_5 = coluna3
                break
    if d == "esquerda":
        if coluna3 >= 4:
            if (linha3,coluna3 - 1) not in barco1 and (linha3,coluna3 - 1) not in barco2 and (linha3,coluna3 - 2) not in barco1 and (linha3,coluna3 - 2) not in barco2 and (linha3,coluna3 - 3) not in barco1 and (linha3,coluna3 - 3) not in barco2 and (linha3,coluna3 - 4) not in barco1 and (linha3,coluna3 - 4) not in barco2: 
                linha3_2 = linha3
                coluna3_2 = coluna3 - 1
                linha3_3 = linha3
                coluna3_3 = coluna3 - 2
                linha3_4 = linha3
                coluna3_4 = coluna3 - 3
                linha3_5 = linha3
                coluna3_5 = coluna3 - 4
                break
barco3 = [(linha3,coluna3), (linha3_2,coluna3_2), (linha3_3,coluna3_3), (linha3_4,coluna3_4), (linha3_5,coluna3_5)]

# Testando
matriz[linha1][coluna1] = "1"
matriz[linha1_2][coluna1_2] = "1"
matriz[linha1_3][coluna1_3] = "1"
matriz[linha2][coluna2] = "2"
matriz[linha2_2][coluna2_2] = "2"
matriz[linha2_3][coluna2_3] = "2"
matriz[linha2_4][coluna2_4] = "2"
matriz[linha3][coluna3] = "3"
matriz[linha3_2][coluna3_2] = "3"
matriz[linha3_3][coluna3_3] = "3"
matriz[linha3_4][coluna3_4] = "3"
matriz[linha3_5][coluna3_5] = "3"
#tabuleiro(matriz)
print(" ")

contadorparte=[0]*3
contadorbarco=0

matrizcopia=[]
for m in range(10):
    matrizcopia.append(["O"] * 10)
    
# Partindo para os tiros
while(contadorbarco<3):
    contadorverdade=0
    tirolinha = str(input("Escolha a linha (de 0 a 9) para o tiro: \n"))
    tirocoluna = str(input("Escolha a coluna (de 0 a 9) para o tiro: \n")) 
    if matriz[int(tirolinha)][int(tirocoluna)] == "1" or matriz[int(tirolinha)][int(tirocoluna)] == "2" or matriz[int(tirolinha)][int(tirocoluna)] == "3":
        if matriz[int(tirolinha)][int(tirocoluna)] == "1":
            contadorparte[0]+=1
            if contadorparte[0]==3:
                contadorbarco+=1
                print("Voce afundou um barco")
                contadorverdade=1
        elif matriz[int(tirolinha)][int(tirocoluna)] == "2":
            contadorparte[1]+=1
            if contadorparte[1]==4:
                contadorbarco+=1
                print("Voce afundou um barco")
                contadorverdade=1
        elif matriz[int(tirolinha)][int(tirocoluna)] == "3":
            contadorparte[2]+=1
            if contadorparte[2]==5:
                contadorbarco+=1
                print("Voce afundou um barco")
                contadorverdade=1
        print("Voce acertou\n")
    elif matriz[int(tirolinha)][int(tirocoluna)] == "X":
        print("Voce ja tentou essa posição!\n")
    else: 
        print ("Continue tentando\n")
        
    matriz[int(tirolinha)][int(tirocoluna)] = "X"
    matrizcopia[int(tirolinha)][int(tirocoluna)] = "X"
    matriz
    
    if contadorverdade==1:
        tabuleiro(matrizcopia)
        print('')
    
print("Voce terminou o jogo! Parabéns")