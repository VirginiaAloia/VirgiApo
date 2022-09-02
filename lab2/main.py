def trova_direzione(schieramento, riga, colonna):
    direzione = None

    if riga > 0 and schieramento[riga - 1][colonna] > 1:
        direzione = "Sud"
    elif riga < len(schieramento) - 1 and schieramento[riga + 1][colonna] > 1:
        direzione = "Nord"
    elif riga > 0 and schieramento[riga][colonna - 1] > 1:
        direzione = "Est"
    elif riga > len(schieramento[riga]) - 1 and schieramento[riga][colonna + 1] > 1:
        direzione = "Ovest"
    return direzione


def main():
    schieramento = []
    with open("schieramento", 'r') as file:
        for line in file:
            line = line.strip()
            row = []
            for num in line:
                row.append(int(num))
            schieramento.append(row)

        for i in schieramento:
            print(i)

    larghezza = 0
    ind_file = 0
    num_file = 0
    direzione = None

    num_in_fila = {}

    for riga in schieramento:
        ind_colonna = 0
        for posizione in riga:
            if posizione == 1:
                larghezza += 1
            if posizione > num_file:
                num_file = posizione
            if posizione != 0:
                if posizione not in num_in_fila:
                    num_in_fila[posizione] = 1
                else:
                    num_in_fila[posizione] += 1

            if posizione == 1 and direzione is None:
                direzione = trova_direzione(schieramento, ind_file, ind_colonna)
            ind_colonna += 1
        ind_file += 1

    min_in_fila = larghezza
    for x, j in num_in_fila.items():
        if j < min_in_fila:
            min_in_fila = j
            max_buchi_fila = x

    print("larghezza: {}".format(larghezza))
    print("Numero di file: {}".format(num_file))
    print("Direzione: {}".format(direzione))
    print("Fila con più buchi: {}".format(max_buchi_fila))


if __name__ == '__main__':
    main()
