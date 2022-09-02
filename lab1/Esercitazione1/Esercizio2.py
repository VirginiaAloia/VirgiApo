word1 = input('Inserisci la prima parola: ')
word2 = input('Inserisci la seconda parola: ')

word1 = word1.lower()
word2 = word2.lower()


list1 = list(word1)
list2 = list(word2)
list3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
         't', 'u', 'v', 'w', 'x', 'y', 'z']

stamplist1 =[]
stamplist2 =[]
stamplist3 = []
stamplist4 = []

# Caratteri che compaiono in entrambe le scritte
print("I caratteri contenuti in entrambe sono: ")
for i in range(len(list1)):
    if list1[i] in list2:
        if list1[i] not in stamplist1:
            stamplist1.append(list1[i])
            print(list1[i])


# Caratteri che compaiono in una stringa non nell'altra
print("I caratteri contenuti solo nella prima sono: ")
for j in range(len(list1)):
    if list1[j] not in list2:
        if list1[j] not in stamplist2:
            stamplist2.append(list1[j])
            print(list1[j])


print("I caratteri contenuti solo nella seconda sono: ")
for z in range(len(list2)):
    if list2[z] not in list1:
        if list2[z] not in stamplist3:
            stamplist3.append(list2[z])
            print(list2[z])


print("Caratteri non contenuti in nessuna delle due sono: ")
for k in range(len(list3)):
    if list3[k] not in list1:
        if list3[k] not in stamplist4:
            stamplist4.append(list3[k])
            print(list3[k])
