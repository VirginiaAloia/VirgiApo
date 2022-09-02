def main():
    num = int(input("Inserisci la dimensione della tabella: "))

    tabella = [[0 for _ in range(num)] for _ in range(num)]
    print(tabella)

    tabella[0][0] = 1

    for i in range(num):
        for j in range(num):
            if i > 0:
                tabella[i][j] += tabella[i - 1][j]

            if j > 0:
                tabella[i][j] += tabella[i][j - 1]

            print("{:{fill}}".format(tabella[i][j], fill=num), end="")
        print(" ")


if __name__ == "__main__":
    main()
