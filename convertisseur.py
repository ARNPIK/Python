def reset():
    print("B = Bronzes A = Argents O = Ors P = Platines")
    global cur1
    cur1 = input("convertir:")
    global cur2
    cur2 = input("en: ")
    loop()


def loop():
    while True:
        print(cur1 + " en " + cur2)
        nb1 = int(input("nombre de " + cur1 + " : "))
        nb2 = 0
        r = 0
        if nb1 == -1:
            reset()

        if cur1 == "A" and cur2 == "B":
            nb2 = nb1 * 100
        elif cur1 == "O" and cur2 == "B":
            nb2 = nb1 * 100000
        elif cur1 == "P" and cur2 == "B":
            nb2 = nb1 * 1000000000

        elif cur1 == "B" and cur2 == "A":
            nb2 = nb1 // 100
            r = nb1 % 100
        elif cur1 == "O" and cur2 == "A":
            nb2 = nb1 * 1000
        elif cur1 == "P" and cur2 == "A":
            nb2 = nb1 * 10000000

        elif cur1 == "B" and cur2 == "O":
            nb2 = nb1 // 100000
            r = nb1 % 100000
        elif cur1 == "A" and cur2 == "O":
            nb2 = nb1 // 1000
            r = nb1 % 1000
        elif cur1 == "P" and cur2 == "O":
            nb2 = nb1 * 10000

        elif cur1 == "B" and cur2 == "P":
            nb2 = nb1 // 1000000000
            r = nb1 % 1000000000
        elif cur1 == "A" and cur2 == "P":
            nb2 = nb1 // 10000000
            r = nb1 % 10000000
        elif cur1 == "O" and cur2 == "P":
            nb2 = nb1 // 10000
            r = nb1 % 10000

        if r == 0:
            print(str(nb2) + cur2)
        else:
            print(str(nb2) + cur2 + " et " + str(r) + cur1)



reset()