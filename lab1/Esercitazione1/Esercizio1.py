word = input('Inserisci una parola: ')

for i in range(1, len(word)):
    for j in range(len(word)):
        if j + i <= len(word):
            print(word[j:j + i])
