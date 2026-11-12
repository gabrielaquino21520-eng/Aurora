import random
import climage
import dados
dados.D10()
dados.D6()
import os

#A função coleta o dado e manda para o return=======

def Jogador_name():
    Name_sans = input("Olá jogador digite um nome para seu personagem: \n")
    print("seu nome é", Name_sans)
    return Name_sans

def script_choice():
    print("========escolha sua classe========")
    while True:
        print("1)-Caçador 2)-Feiteceiro 3)-Monge")
        try:
            classe = (int(input()))
            if classe > 3 or classe < 1:
                print("escolha uma classe para continuar !!!")
            else:
                break
        except ValueError:
            print("escolha uma opção valida !!!")

    return classe


#Criação de um objeto/classe=======

class classe_player():
    #tudo que estiver dentro de () é um pre requisito para minha classe ou seja precisa ter uma informação em "sans" para que a classe seja execulatada.
    def __init__(self, classe, Name_sans):
        self.classe = classe
        self.name = Name_sans

        if classe == 1:
            self.type = "Caçador"
            self.descri = "Um caçador tem que ser forte, ágil e estar sempre um passo a frente da caça"
            self.xp = 0
            self.acc = 15
            self.life = 100
            self.forca = (random.randint(1, 11))
            self.magic = 0

        elif classe == 2:
            self.type = "Feiteceiro"
            self.descri = "Os Feiteceiros herdam conhecimentos de gerações antigas de familiares e podem usar o puro poder"
            self.xp = 0
            self.acc = 7
            self.life = 100
            self.forca = 0
            self.magic = (random.randint(1, 12))

        elif classe == 3:
            self.type = "Monge"
            self.descri = "Monge esta além do plano atual, seu sentido fora desse mundo é oque o torna uma presença poderosa"
            self.xp = 0
            self.acc = 10
            self.life = 100
            self.forca = 0
            self.magic = (random.randint(1, 5))

class Monster():

    def __init__(self, num):
     self.num = int(num)

     if num == 1:
         self.ship = 'Animal'
         self.name = "lobo solitario"
         self.life = 64
         self.xp = 12
         self.acc = random.randint(3, 7)
         self.dano_critico = 10
         self.condicao = "sangrando"

     elif num == 2:
         self.ship = 'Mistico'
         self.name = 'CONDE DRACULA'
         self.life = 210
         self.xp = 75
         self.acc = random.randint(8, 17)
         self.dano_critico = random.randint(18, 28)
         self.condicao = "sangrando"

     elif num == 3:
         self.ship = 'Cósmico'
         self.name = 'Mãe Hydra'
         self.life = 350
         self.xp = 85
         self.acc = 23, 30
         self.dano_critico = random.randint(18, 28)
         self.condicao = "medo"


class choices_b:

    def __init__(self, Jogador_1, Monster):
        self.Jogador_1 = Jogador_1
        self.Monster = Monster
        print("1 -Ataque", "2 -Abilidade ", "\n" "3 -Checar", "4 -Poções", "\n")
        action = int(input())
        if action == 1:
            dano = dados.D6()
            # Ataques do caçador
            if Jogador_1.type == "Caçador":
                if dano == 3 or dano == 2:
                    print("Bem sucedido \n")
                    dano_real = dano + Jogador_1.acc
                    Monster.life -= dano_real
                    print("você da", dano_real, "de dano em", Monster.name)

                elif dano > 3:
                    print("Crítico de muita sorte \n")
                    dano_real = dano + Jogador_1.forca
                    print("você da", dano_real, "de dano")

                elif dano > 1 and Monster.ship == 'Animal':
                    dano_real = dano + Jogador_1.acc + Jogador_1.forca
                    print("Com uma força quase mostruosa você desfere um ataque sanguenario")

                    print(dano_real, "com efeito")

                else:
                    print("Mal sucedido \n")
                    print("Você erra o ataque...")

            # Ataques do feiticeiro
            elif Jogador_1.type == "Feiticeiro":
                if dano == 3 or dano == 2:

                    print("Bem sucedido \n")
                    dano_real = dano + Jogador_1.magic
                    print("você da", dano_real, "de dano")

                elif dano > 3:
                    print("Crítico de muita sorte \n")
                    dano_real = dano + Jogador_1.magic
                    Monster.life -= dano_real
                    print("você da", dano_real, "de dano em", Monster.name)


                elif dano > 1 and Monster.ship == 'Mistico':
                    dano_real = dano + Jogador_1.acc + Jogador_1.magic + Jogador_1.magic
                    print("Seu conhecimento materializa em uma onda de PODER BRUTO")
                    Monster.life -= dano_real
                    print(Monster.name, "tem partes do corpo desentegrado e toma", dano, "de dano")

                    print(dano_real, "com efeito")

                else:
                    print("Mal sucedido \n")
                    print("Você erra o ataque...")


            # Ataques do monge
            elif Jogador_1.type == "Monge":
                if dano == 3 or dano == 2:
                    print("Bem sucedido \n")
                    dano_real = dano + Jogador_1.acc or Jogador_1.magic
                    Monster.life -= dano_real
                    print("você da", dano_real, "de dano em", Monster.name)

                elif dano > 3:
                    print("Crítico de muita sorte \n")
                    dano_real = dano + Jogador_1.acc or Jogador_1.magic
                    Monster.life -= dano_real
                    print("você da", dano_real, "de dano em", Monster.name)


                elif dano > 1 and Monster.ship == 'Cósmico':
                    dano_real = dano + Jogador_1.acc + Jogador_1.magic
                    self.Monster.life -= dano_real
                    print("você da", dano_real, "de dano em", Monster.name)
                    # restaurar vida
                    Jogador_1.Life += dano_real
                    print("sua vida é restaurada", Jogador_1.life)
                    print("Você trancende e sua luz desfere uma luz restaura todo seu ser")

                    print(dano_real, "com efeito")

                else:
                    print("Mal sucedido \n")
                    print("Você erra o ataque...")

        elif action == 2:
            print("tenho que fazer ainda")

        elif action == 3:
            print("Tenho que fazer ainda")

        elif action == 4:
            print("tenho que fazer ainda")

        else:
            print("tenho que fazer ainda")

def ataque_monster():

    dano = dados.D10()
    print(Monster.name," te atacou \n")

    if dano == 3 or dano == 2:
        print("Você foi atingido \n")
        dano_real = dano + Monster.acc
        dano_real -= Jogador_1.life
        print("você recebeu", dano_real, "de dano")

    elif dano > 3:
        print("Você é dilacerado \n")
        dano_real = dano + Jogador_1.forca
        print("você recebeu", dano_real, "de dano")

    elif dano > 1 and Monster.ship == 'Animal':
        dano_real = dano + Jogador_1.acc + Jogador_1.forca
        print("Com uma força quase mostruosa você desfere um ataque sanguenario")

        print(dano_real, "com efeito")

    else:
        print("Você consegue desviar \n")

def meeting():
    print(Monster.name, 'apareceu \n')

    while Jogador_1.life > 0 and Monster.life > 0:

        print(Monster.life)
        Lobo_imagem = climage.convert('C:/Users/docpo/Downloads/lo/imagem/lobo.jpg', 'lobo_ansi', width=30)
        print(Lobo_imagem)
        choices_b(Jogador_1, Monster)

        if Monster.life == 0:

            print("parabéns, recebeu", 0, "de xp")
            break

        elif Jogador_1 == 0:
            print("você fracassou melhore")
            break









# valor sendo recebido pelo return, atraz do "Name_sans"======

#codigo sendo execultado aqui.
print("=====jogador 1=====")
Name_sans = Jogador_name()
classe = script_choice()
Monster = Monster(1)
Jogador_1 = (classe_player(classe, Name_sans))
print(f"seu nome é {Jogador_1.name}: e sua classe é {Jogador_1.type} \n descrição: {Jogador_1.descri} \n Vida: {Jogador_1.life} \n Ação: {Jogador_1.acc} ", '\n')
meeting()









