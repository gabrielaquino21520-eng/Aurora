import random
# agora sim porra !


#A função coleta o dado e manda para o return=======

def Jogador_name():
    Name_sans = input("Olá jogador digite um nome para seu perssonagem: \n")
    print("seu nome é", Name_sans)
    return Name_sans


#MELHORAR, colocar uma opeção de confirmação de código.

#escolha da classe=======

def script_choice():
    print("========escolha sua classe========")
    while True:
        print("1)-Caçador 2)-Feiteceiro 3)-Monge")
        classe = (int(input()))
        if classe > 3 or classe < 1:
            print("escolha uma classe para continuar !!!")
        else:
            break

    #MELHORAR, caso o jogador digite uma letra aqui ferrou

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

        elif classe == 2:
            self.type = "Feiteceiro"
            self.descri = "Os Feiteceiros herdam conhecimentos de gerações antigas de familiares e podem usar o puro poder"
            self.xp = 0
            self.acc = 7
            self.life = 100
            self.magic = (random.randint(1, 12))

        elif classe == 3:
            self.type = "Monge"
            self.descri = "Monge esta além do plano atual, seu sentido fora desse mundo é oque o torna uma presença poderosa"
            self.xp = 0
            self.acc = 10
            self.Life = 100
            self.magic = (random.randint(1, 5))


class monster():
    def __init__(self, num):
     self.num = int

     if num == 1:
         self.ship = 'Animal'
         self.name = "lobo solitario"
         self.life = 64
         self.xp = 12
         self.dano_normal = random.randint(3, 7)
         self.dano_critico = 10
         self.condicao = "sangrando"

     elif num == 2:
         self.ship = 'Mistico'
         self.name = 'CONDE DRACULA'
         self.life = 210
         self.xp = 75
         self.dano_normal = random.randint(8, 17)
         self.dano_critico = random.randint(18, 28)

     elif num == 3:
         self.ship = 'Cósmico'
         self.name = 'A sombra na água'
         self.life = 350
         self.xp = 85
         self.dano_normal = 23, 30
         self.dano_critico = random.randint(18, 28)








def D10():
    D10 = random.randint(1, 10)
    if D10 <= 9 and D10 >= 3:
        print("Você foi atingido", "Normal", D10)
    elif D10 <= 2:
        print("Você consegue desviar", "Errou", D10)
    else:
        print("Você é dilacerado", "Critico", D10)

    return D10


def D6():
    D6 = random.randint(1, 6)
    if D6 == 3 or D6 == 2:
        int(D6)

    elif D6 == 1:
        int(D6)
    else:
        int(D6)

    return D6


def batalha_person():
    ec = ["Ataque", "Abilidade", "Checar", "Poções"]
    print('1 -', ec[0], '2 -', ec[1], "\n" '3 -', ec[2], '4 -', ec[3], "\n")
    escc = input(int())
    if escc == 1:
        dano = D6()

        # Ataques do caçador
        if Jogador_1.type == "Caçador":
            if dano == 3 or dano == 2:
                print("Bem sucedido \n")
                dano_real = dano + Jogador_1.acc
                dano_real -= Monster.life
                print("você da", dano_real, "de dano em", Monster.name)

            elif dano > 3:
                print("Crítico de muita sorte \n")
                dano_real = dano + Jogador_1.forca
                print("você da", dano_real, "de dano")

            elif dano > 1 and Monster.ship == 'Animal' and Jogador_1.type == "Caçador":
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


            elif dano > 1 and Monster.ship == 'Mistico' and Jogador_1.type == "Feiticeiro":
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
                rint("Crítico de muita sorte \n")
                dano_real = dano + Jogador_1.acc or Jogador_1.magic
                Monster.life -= dano_real
                print("você da", dano_real, "de dano em", Monster.name)


            elif dano > 1 and Monster.ship == 'Cósmico' and Jogador_1.type == "Monge":
                dano_real = dano + Jogador_1.acc + Jogador_1.magic
                Monster.life -= dano_real
                print("você da", dano_real, "de dano em", Monster.name)
                # restaurar vida
                Jogador_1.Life += dano_real
                print("sua vida é restaurada", Jogador_1.life)

                print("Você trancende e sua luz desfere uma luz restaura todo seu ser")

                print(dano_real, "com efeito")

            else:
                print("Mal sucedido \n")
                print("Você erra o ataque...")

    elif escc == 2:
        print("tenho que fazer ainda")

    elif escc == 3:
        print("Tenho que fazer ainda")

    elif escc == 4:
        print("tenho que fazer ainda")

    else:
        print("tenho que fazer ainda")


def ataque_monster():
    dano = D10()







# valor sendo recebido pelo return, atraz do "Name_sans"======



#codigo sendo execultado aqui.


print("=====jogador 1=====")
Name_sans = Jogador_name()
classe = script_choice()
Jogador_1 = (classe_player(classe, Name_sans))
Monster = monster(num=2)
print(f"seu nome é {Jogador_1.name}: e sua classe é {Jogador_1.type} \n descrição: {Jogador_1.descri} \n Vida: {Jogador_1.life} \n Ação: {Jogador_1.acc} ")
print(Monster.ship)