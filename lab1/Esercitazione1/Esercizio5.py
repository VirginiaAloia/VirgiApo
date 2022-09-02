

def main():
    ismax = False
    listnum = []
    num = input("Inserisci un numero: ")

    while num != "":
        listnum.append(int(num))
        num = input("Inserisci un altro numero o termina: ")

    for i in range(len(listnum)):
        if (i == 0 or listnum[i] > listnum[i-1]) and \
                (i == len(listnum) - 1 or listnum[i] > listnum[i+1]):
            print("Il massimo locale si trova in posizione: {}".format(i+1))
            ismax = True

    if not ismax:
        print("Non ci sono massimi locali")


if __name__ == "__main__":
    main()
