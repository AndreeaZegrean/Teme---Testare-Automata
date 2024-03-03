# 1. Definiti o lista care sa stocheze numele tuturor celor prezenti la studiul individual.
# Parcurgeti lista si printati toate elementele din aceasta folosind pe rand for, while si foreach
lista_participanti = ["Diana", "Dana", "Bogdan", "Augustin", "Diandra", "Emilian", "Gabriela", "Ioana", "Irina",
                      "George", "Robert", "Razvan"]

# Parcurgere cu for:
for i in range(len(lista_participanti)):
    print(f"Astazi {lista_participanti[i]} este prezent la curs")

# Parcurgere cu foreach:
for participant in lista_participanti:
    print(f"Astazi {participant} este prezent la curs")

# Parcurgere cu while
i = 0
while i < len(lista_participanti):
    print(f"Astazi {lista_participanti[i]} este prezent la curs")
    i += 1

# #Bonus 1: Sortati o lista folosind algoritmul de sortare prin metoda bulelor (bubble sort)
for i in range(len(lista_participanti) - 1):
    for j in range(i + 1, len(lista_participanti)):
        if lista_participanti[i] > lista_participanti[j]:
            aux = lista_participanti[i]
            lista_participanti[i] = lista_participanti[j]
            lista_participanti[j] = aux

print(f"Lista dupa sortare este {lista_participanti}")

# Bonus 2: Incercati sa printati pe ecran pe cei 101 dalmatieni salvati intr-o lista. La fiecare dalmatian veti printa
# pe ecran urmatorul text: “Dalmatianul curent se afla in pozitia “i””.
# Atentie, ghilimelele vor trebui tratate folosind caracterul escape
for i in range(1, 102):
    print(f"Dalmatianul curent se afla in pozitia \"{i}\"")

# Aveti urmatorul dictionar (dictionar imbricat / nested dictionary / embedded dictionary):
fotbalisti_pe_echipe = {
    'Barcelona': {
        'Dica':
            {
                'Nume complet': 'Nicolae Dica',
                'Varsta': 45,
                'Numar Tricou': 10
            },
        'Banel':
            {
                'Nume complet': 'Banel Nicolita',
                'Varsta': 47,
                'Numar Tricou': 3
            },
        'Dukadam':
            {
                'Nume complet': 'Helmut Dukadam',
                'Varsta': 65,
                'Numar Tricou': 7
            }
    }
}

# Printati pe ecran numarul de pe tricou al oricarui jucator doriti
print(fotbalisti_pe_echipe['Barcelona']['Banel']['Numar Tricou'])
print(fotbalisti_pe_echipe['Barcelona']['Dica']['Numar Tricou'])
print(fotbalisti_pe_echipe['Barcelona']['Dukadam']['Numar Tricou'])

# Folositi functia pop pentru a scoate orice jucator din dictionar
# fotbalisti_pe_echipe.pop['Banel']
# print(fotbalisti_pe_echipe)

# Printati pe ecran detaliile despre fiecare jucator astfel incat sa obtineti urmatorul rezultat:
for key, value in fotbalisti_pe_echipe.items():
    for key_inner, value_inner in value.items():
        print(f"La echipa {key} joaca jucatorul:")
        for key_jucator, value_jucator in value_inner.items():
            print("Detalii jucator", f"{key_jucator}:{value_jucator}", sep=" - ", end=",")
print("\n")

# Alte exercitii
# 1.Ascunde vocalele! Să se scrie un "translator" care să modifice vocalele în "*" utilizând ciclul while / if / for.
# 2.Tipăriţi toate numerele prime aflate între două numere naturale citite de la tastatura
# 3.Se citește un număr natural n. Să se scrie programul care determină și afișează câte cifre impare are numărul citit.
# 4.Se citește un număr natural n. Să se scrie programul care determină și afișează numărul de cifre ale lui n
# 5.Se citește un număr natural n. Să se scrie programul care verifică dacă numărul este palindrom
# 6.Se citește un număr natural n. Să se scrie programul care determină și afișează cea mai mare și cea mai mică cifră a numărului n
# 7.Se citește un număr natural n. Să se scrie programul care afișează pe ecran mesajul DA dacă toate cifrele lui n
# sunt în ordine crescătoare și mesajul NU în caz contrar
# 8.Se citesc n numere întregi. Se cere: suma numerelor citite, maximul, minimul, câte sunt negative, câte sunt
# pare/impare, cel mai mare număr negativ/pozitiv
