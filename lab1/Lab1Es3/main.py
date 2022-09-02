DATA_PATCH = "C:/Users/39347/PycharmProjects/Lab1Es3"

IN_FILE = "input"
OUT_fILE = "output"


def main():
    lines = []
    with open("{}/{}".format(DATA_PATCH, IN_FILE), "r") as file:
        for line in file:
            print(line.strip())
            lines.append(line)
    lines = lines[-1::-1]

    with open("{}/{}".format(DATA_PATCH, OUT_fILE), "w") as file:
        for line in lines:
            file.write(line)


if __name__ == '__main__':
    main()
