BINGONum = []
for item in range(1,76):
    BINGONum.append(item)
B_list = []
I_list = []
N_list = []
G_list = []
O_list = []
B = []
I = []
N = []
G = []
O = []

print()
print("\t\t\t\t\t\t\t BINGO")
print()

for BINGONum in range(1, 16):
    B_list.append(BINGONum)
print("B =>", *B_list, sep="    ")

for BINGONum in range(16, 31):
    I_list.append(BINGONum)
print("I =>", *I_list, sep="    ")

for BINGONum in range(31, 46):
    N_list.append(BINGONum)
print("N =>", *N_list, sep="    ")

for BINGONum in range(46, 61):
    G_list.append(BINGONum)
print("G =>", *G_list, sep="    ")

for BINGONum in range(61, 76):
    O_list.append(BINGONum)
print("O =>", *O_list, sep="    ")

print()

while True:
    draw = input("Deseja pegar um número aleatório(N/S)?")
    draw = draw.capitalize()
    if draw == "S":

        import random
        BINGONum = []
        for item in range(1, 76):
            BINGONum.append(item)

        PICKnum = random.choice(BINGONum)
        print()

        if PICKnum >= 1 and PICKnum <=15:
            B.append(PICKnum)
            if PICKnum in B_list:
                B_list.remove(PICKnum)
            print("B =>", * B_list, sep="   ")
            print("I =>", * I_list, sep="   ")
            print("N =>", * N_list, sep="   ")
            print("G =>", * G_list, sep="   ")
            print("O =>", * O_list, sep="   ")

            print("\nSelecione um número")
            print("B => " + str(B)[1:-1], sep="   ")
            print("I => " + str(I)[1:-1], sep="   ")
            print("N => " + str(N)[1:-1], sep="   ")
            print("G => " + str(G)[1:-1], sep="   ")
            print("O => " + str(O)[1:-1], sep="   ")

            print()

            print("Número aleatório selecionado : B-0" + str(PICKnum))
            print()

            input("Aperte qualquer tecla para continuar...")
            print()

        if PICKnum >= 16 and PICKnum <= 30:
            I.append(PICKnum)
            if PICKnum in I_list:
                I_list.remove(PICKnum)
            print("B =>", * B_list, sep="   ")
            print("I =>", * I_list, sep="   ")
            print("N =>", * N_list, sep="   ")
            print("G =>", * G_list, sep="   ")
            print("O =>", * O_list, sep="   ")

            print("\nSelecione um número")
            print("B => " + str(B)[1:-1], sep="   ")
            print("I => " + str(I)[1:-1], sep="   ")
            print("N => " + str(N)[1:-1], sep="   ")
            print("G => " + str(G)[1:-1], sep="   ")
            print("O => " + str(O)[1:-1], sep="   ")
            print()

            print("Número aleatório selecionado : I-" + str(PICKnum))
            print()
            input("Aperte qualquer tecla para continuar...")
            print()

        if PICKnum >= 31 and PICKnum <= 46:
            N.append(PICKnum)
            if PICKnum in N_list:
                N_list.remove(PICKnum)
            print("B =>", * B_list, sep="   ")
            print("I =>", * I_list, sep="   ")
            print("N =>", * N_list, sep="   ")
            print("G =>", * G_list, sep="   ")
            print("O =>", * O_list, sep="   ")

            print("\nSelecione um número")
            print("B => " + str(B)[1:-1], sep="   ")
            print("I => " + str(I)[1:-1], sep="   ")
            print("N => " + str(N)[1:-1], sep="   ")
            print("G => " + str(G)[1:-1], sep="   ")
            print("O => " + str(O)[1:-1], sep="   ")
            print()

            print("Número aleatório selecionado : N-" + str(PICKnum))
            print()
            input("Aperte qualquer tecla para continuar...")
            print()

        if PICKnum >= 46 and PICKnum <= 60:
            G.append(PICKnum)
            if PICKnum in G_list:
                G_list.remove(PICKnum)
            print("B =>", * B_list, sep="   ")
            print("I =>", * I_list, sep="   ")
            print("N =>", * N_list, sep="   ")
            print("G =>", * G_list, sep="   ")
            print("O =>", * O_list, sep="   ")

            print("\nSelecione um número")
            print("B => " + str(B)[1:-1], sep="   ")
            print("I => " + str(I)[1:-1], sep="   ")
            print("N => " + str(N)[1:-1], sep="   ")
            print("G => " + str(G)[1:-1], sep="   ")
            print("O => " + str(O)[1:-1], sep="   ")
            print()

            print("Número aleatório selecionado : G-" + str(PICKnum))
            print()
            input("Aperte qualquer tecla para continuar...")
            print()

        if PICKnum >= 61 and PICKnum <= 75:
            O.append(PICKnum)
            if PICKnum in O_list:
                O_list.remove(PICKnum)
            print("B =>", * B_list, sep="   ")
            print("I =>", * I_list, sep="   ")
            print("N =>", * N_list, sep="   ")
            print("G =>", * G_list, sep="   ")
            print("O =>", * O_list, sep="   ")

            print("\nSelecione um número")
            print("B => " + str(B)[1:-1], sep="   ")
            print("I => " + str(I)[1:-1], sep="   ")
            print("N => " + str(N)[1:-1], sep="   ")
            print("G => " + str(G)[1:-1], sep="   ")
            print("O => " + str(O)[1:-1], sep="   ")
            print()

            print("Número aleatório selecionado : O-" + str(PICKnum))
            print()
            input("Aperte qualquer tecla para continuar...")
            print()

    elif draw == "N":
        print()
        print("O jogo acabou")
        print()

        AnotherDraw = input("Deseja iniciar um novo jogo? (N/S)?")
        AnotherDraw = AnotherDraw.capitalize()
        print

        if AnotherDraw == "S":
            print("BINGO")
            print()

            B_list.clear()
            I_list.clear()
            N_list.clear()
            G_list.clear()
            O_list.clear()
            B.clear()
            I.clear()
            N.clear()
            G.clear()
            O.clear()

            print()

            for BINGONum in range(1, 16):
                B_list.append(BINGONum)
            print("B => ", * B_list, sep="   ")

            for BINGONum in range(16, 31):
                I_list.append(BINGONum)
            print("I => ", * I_list, sep="   ")

            for BINGONum in range(31, 46):
                N_list.append(BINGONum)
            print("N => ", * N_list, sep="   ")

            for BINGONum in range(46, 61):
                G_list.append(BINGONum)
            print("G => ", * G_list, sep="   ")

            for BINGONum in range(61, 76):
                O_list.append(BINGONum)
            print("O => ", * O_list, sep="   ")

        else:
            print()
            print()
            print("Obrigado")
            break




