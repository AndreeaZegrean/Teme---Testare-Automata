# 1. Definiți o adresă de memorie care să salveze data curentă. Va fi o variabilă sau o constantă?
# raspuns -> o variabila
# am definit variabila data curenta
dataCurenta = '03.02.2024'
print(dataCurenta)

# 2. Identificați tipul de dată pe care îl are variabila pe care ați definit-o folosind una din funcțiile învățate la curs
# raspuns -> string. am printat cu functia type pt a afla ce fel de tip de data are variabila dataCurenta
print(type(dataCurenta))

# 3. Definiți alte câteva variabile care să stocheze cursul la care sunteți,
# ce zi este și la ce sesiune de curs sunteți.
# raspuns -> am definit 4 variabile diferite
nume = 'Deea'
curs = 'ITFactory'
sesiune_curs = '2'
zi = 'sambata'
# am printat cu formatare
print(f'{nume} face curs la {curs} si este la sesiunea de curs nr {sesiune_curs} iar ziua de recuperare curs este {zi}')

# 4. Salvați fiecare cuvânt din propoziția: “Ana s-a nascut in anul 1990” în câte o adresă de memorie.
cuv1 = 'Ana'
cuv2 = 's-a'
cuv3 = 'nascut'
cuv4 = 'in'
cuv5 = 'anul'
cuv6 = 1990 # sau in acest caz poate sa ramana anul de tip text, adica cu ghilimele si putem printa print(cuv1 + cuv2 + cuv3 + cuv4 + cuv5 + cuv6)
propozitie = 'Ana s-a nascut in anul 1990'
print(propozitie)

# 5. Printați propoziția de mai sus folosind trei tipuri diferite de printuri.
print(cuv1, cuv2, cuv3, cuv4, cuv5, cuv6)
print(f'{propozitie}') # prin formatare
print(f'{cuv1} {cuv2} {cuv3} {cuv4} {cuv5} {cuv6}') # prin formatare
# am declarat tipul de data pt cuv6 fiind un strig, altfel nu se putea printa mesajul, ne dadea eroare
print(cuv1 + ' ' + cuv2 + ' ' + cuv3 + ' ' + cuv4 + ' ' + cuv5 + ' ' + str(cuv6))

# 6. Declarați câteva alte adrese de memorie la alegere și inițializați-le folosind funcția input.
nume = input('Numele meu este: ')
prenume = input('Prenumele meu este: ')
varsta = input('Am varsta de: ' )
job = input('lucrez la: ')
CNP = input('CNP-ul meu este: ')
print(nume + ' ' + prenume)
print(f'{nume} este numele meu, {prenume} este prenumele meu, am {varsta} ani si lucrez la {job}, iar CNP-ul meu este {CNP} ')
