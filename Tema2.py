# Ex_1 - În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
''' O variabila este o adresa de memorie reprezentata de un nume, adresa de memorie
care contine o valoare ce se poate modifica pe parcursul executiei programului'''

#Ex_2 - Declară și inițializează câte o variabilă din fiecare din următoarele tipuri:int, string, float, boolean
# int
varsta = 35
# string
nume = 'Andreea'
# float
procent = 19.75
# boolean
curs_finalizat = True

#Ex_3 - Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.
'''print(type(varsta))
print(type(nume))
print(type(procent))
print(type(curs_finalizat))'''

#Ex_4 - Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere), apoi verifică din nou tipul de date al acesteia.
'''print(f'Tipul de date curent este {type(procent)}')
procent = round(procent)
print(f'Noul tip de date este: {type(procent)}')'''

#Ex_5 - Incearca sa convertesti variabila string la int folosind type casting si observa rezultatele
# curs = int(curs)
# raspuns -> nu se poate transforma un string in int

#Ex_6 - Incearca sa convertesti variabila boolean la int folosind type casting si observa rezultatele
'''curs_finalizat = int(curs_finalizat)
print(f'Noua valoare a variabilei curs_finalizat este {curs_finalizat}')'''

#Ex_7 - Schimba valoarea variabilei boolean (din true in false sau din false in true) si repeta exercitiul anterior
'''curs_finalizat = True
curs_finalizat = int(curs_finalizat)
print(f'Noua valoare a variabilei curs_finalizat este {curs_finalizat}')'''

#Ex_1 -  Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile. Rezolvă nepotrivirile de tip pe rand prin toate modalitatile cunoscute
# print(varsta, nume, procent, curs_finalizat)
# print(f'{varsta} {nume} {procent} {curs_finalizat}')

# Varianta asta va returna eroare pentru ca nu poate face concatenare intre string si int si respectiv string si bool
# print('La varsta de ' + varsta + ' ani particip la cursul de' + curs + '. Am parcurs ' + procent + '% din curs. Cursul e finalizat? '
# + curs_finalizat)

# Varianta mai buna dar care necesita mult cod scris
# print('La varsta de ' + str(varsta) + ' ani particip la cursul de' + curs + '. Am parcurs ' + str(procent) + '% din curs.
# Cursul e finalizat? ' + str(curs_finalizat))


#Ex_2 - Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila.
# Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'.
'''nume = input('Numele meu este: ')
prenume = input('Prenumele meu este: ')
print(len(nume + prenume))
print(f'Numele complet are {len(nume + prenume)} caractere')'''

#Ex_3 - Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila.
# Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.
# a = input('lungimea dreptungiului este: ')
# b = input('latimea dreptunghiului este: ')
# print(int(a) * int(b))

# lungime = float(input('Introduceti lungimea'))
# latime = float(input('Introduceti latimea'))
# aria = lungime * latime
# print(f'Aria dreptunghiului este {aria}')


#Ex_4 - Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare cuvântul
# 'the' în acest string
# fraza = 'Coral is either the stupidest animal or the smartest rock'
# print(fraza.count('the'))

'''prop = 'Coral is either the stupidest animal or the smartest rock'
nr_aparitii = prop.count('the')
print(f'Cuvantul 'the' apare de {nr_aparitii} ori')'''


#EX_5 Folosindu-te de string-ul de la exercițiul 8, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”) si afișează pe ecran rezultatul
# print(fraza.replace('the', 'THE'))

# prop = prop.replace('the','THE')
# print(f'Noua propozitie este: {prop}')

#Ex_6 Folosindu-te de string-ul de la exercițiul 8 foloseste un assert ca să verifici dacă acest string conține doar numere.
# print(fraza.isdecimal())

# assert prop.isnumeric() == True, f'The string is not numeric'

# Ex cu dificultate medie
#Ex_1 Citiți de la tastatură un string de dimensiune impară și afișați caracterul din mijloc.
'''cuv = 'Andreea'
print(len(cuv))
print(cuv[3])'''

# string_impar = input('va rugam sa introduceti un string de lungime impara ')
# print(f'Caracterul din mijloc este: {string_impar[len(string_impar)//2]}')

# # rezolvare de dificultate medie:
# string_impar = input('va rugam sa introduceti un string de lungime impara ')
# if len(string_impar)%2==0:
#   string_impar = input('Dimensiunea stringului nu este impara. Va rugam sa introduceti stringul de dimensiune corecta')
# print(f'Caracterul din mijloc este: {string_impar[len(string_impar)//2]}')

#Ex_2 Folosind assert, verificați dacă un string este palindrom. Stringul se va citi de la tastatură
# string_palindrom = 'mamam'
# assert string_palindrom == string_palindrom[::-1]
# print('Stringul este palindrom')


#Ex_3 - Citiți un string de la tastatură (ex: 'alabala portocala') asupra căruia să efectuați următoarele:
# salvați fiecare cuvânt într-o variabilă;
# printați ambele variabile pentru verificare.

# string_citit = input('Va rugam sa introduceti un numar')
# cuv1, cuv2 = string_citit[:1],string_citit[1:2]
# print(f'Cuvintele salvate sunt: {cuv1}, {cuv2}')


#Ex_4 - Citiți un string de la tastatură (ex: alabala portocala) asupra căruia sa efectuați următoarele:
# salvați primul caracter într-o variabilă
# capitalizați acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

# string_citit = input('Va rugam sa introduceti un numar')
# primul_caracter = string_citit[0]
# string_capitalizat = string_citit[0] + string_citit[1:len(string_citit)-1].replace(primul_caracter,primul_caracter.upper())+string_citit[len(string_citit)-1]


# Ex_5 - citeste un user de la tastatura, citeste o parola. Afiseaza: 'Parola pt user x este ***** si are x caractere
'''user = input('Nume user: ')
parola = input('parola este: ')
#print(len(parola))
print(f'parola pentru {user} este {parola} si are {len(parola)} caractere')'''

# Exerciții Structură Alternativă If

# #Ex_1 Explicați cu cuvintele voastre în cadrul unui comentariu cum funcționează un if else
"""
Se evalueaza mai intai conditia din interiorul if-ului. Daca este adevarata, se va executa blocul de instructiuni imediat
  urmator
Daca aceasta este falsa, se va evalua, daca exista, conditia din elif. Daca aceasta este adevarata se va executa
  blocul de instructiuni imediat urmator. Daca este falsa, se poate trece la urmatorul elif (daca exista) si
  se va repeta evaluarea, in caz contrar se va muta pe ramura de else, daca exista
Ramura de else nu mai evalueaza nicio conditie, ci executa direct blocul de cod de care e legata"""


# Ex_2 Verificați și afișați dacă x este număr natural sau nu (un număr se consideră natural dacă este număr întreg mai mare ca 0)
'''x = 13
if(x > 0 and type(x)==int):
    print('Numarul este natural')
else:
    print('Numarul nu este natural')'''

# Ex_3 Verificați și afișați dacă x este număr pozitiv, negativ sau neutru
'''if (x>0):
    print('Numarul este pozitiv')
elif(x < 0):
    print('Numarul este negativ')
else:
    print('Numarul este neutru')'''


# Ex_4 Verificați și afișați dacă x este între -2 și 13 (incluzând capetele de interval).
'''numar = int(input('introduceti numarul:'))
if numar >= -2 and numar <= 13:
    print('nr este in interval')
else:
    print('nr nu este in interval'''

# Solutia 1:
'''if x >=-2 and x<=13:
    print('Numarul se afla in interval')'''

# solutia 2:
'''if x in range(-2, 14):
    print('Numarul se afla in interval')'''

#Ex_5 Verificați dacă x NU este între 5 și 27, excluzând capetele de interval. (a se folosi ‘not’)
'''x = 10
print(not x < 5 and x != 27 )'''

# Solutia 1:
'''if  not(x >= 5 and x <= 27):
    print('Numarul se afla in interval')'''

# solutia 2:
'''if not(x in range(5, 27)):
    print('Numarul se afla in interval')'''

#Ex_6 Declarați o nouă variabilă y de tip int și apoi verificați și afișați dacă x și y sunt egale, în caz contrar
# afișați care din ele este mai mare
'''y = 35
if x > y:
    print('x este mai mare decat y')
elif x == y:
    print('x este egal cu y')
elif x < y:
    print('y este mai mare decat x')'''

'''y = 3
if x == y:
    print('Numerele sunt egale')
elif x>y:
    print('x este mai mare ca y')
else:
    print('y este mai mare ca x')'''

#Ex_7 Presupunând ca x, y, z (toate de tip int) reprezintă laturile unui triunghi, afișați dacă triunghiul este isoscel
# (două laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latură nu e egală).
'''a = 2
b = 2
c = 2
if a == b:
    print('tringhiul este isoscel')
elif a == b and b == c:
    print('tringhiul este echilateral')
elif a != b != c:
    print('tringhiul este oarecare')'''
    
# Solutia 1
'''z = 4
if x == y == z:
    print('Triunghiul este echilateral')
elif x==y and y!=z or y==z and z!=x or x==z and z!=y:
    print('Triunghiul este isoscel')
else:
    print('Triunghiul este oarecare')'''

# Solutia 2
'''z = 4
if x == y == z:
    print('Triunghiul este echilateral')
elif x!=y!=z:
    print('Triunghiul este oarecare')
else:
    print('Triunghiul este isoscel')'''


#Ex_8 Citiți o literă de la tastatură apoi verificați și afișați dacă este vocală sau nu.
# Atenție! Trebuie să evaluați și cazurile uppercase și cazurile lowercase.
'''litera = input('introduceti litera ').lower()
vocale = 'aeiou'
if litera in vocale:
    print('Litera este o vocala')
else:
    print('Litera nu este vocala')'''

# -- Exerciții Structură Alternativă If - Dificultate Medie
# EX_1 - Calculare preț discount
'''Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil, va avea o reducere de 10%.
Atât pentru seniori cât și pentru non-seniori se va aplica o reducere suplimentară de 10% dacă vor călători în timpul iernii.
De asemenea, atât pentru seniori, cât și pentru non-seniori se va aplica o taxă de lux de 3% dacă vor călători la clasa I 
(în orice sezon) sau 1% taxă de gestiune în caz contrar.'''

'''Pentru exercițiul de mai sus trebuie să scrieți structura alternativă if-elif-else astfel încât să implementați scenariul aferent.
Pretul biletului se va citi de la tastatura si se va actualiza conform discountului si taxelor aferente'''

'''varsta = int(input('Va rugam sa introduceti varsta'))
sezon = input('Va rugam sa introduceti sezonul')
clasa = int(input('Va rugam sa introduceti clasa la care calatoriti'))
pret_bilet = float(input('Va rugam sa introduceti pretul biletului'))
discount = 0
tax = 0
if varsta >=65:
    discount = 0.1
else:
    nr_copii = int(input('Va rugam sa introduceti numarul de copii cu care calatoriti'))
    if nr_copii>=1:
        discount = 0.1
if sezon == 'iarna':
    discount = discount+0.1
if clasa == 1:
    tax = 0.03
else:
    tax = 0.01
pret_bilet = pret_bilet - pret_bilet*discount + pret_bilet*tax)'''

'''Ex_2 - Calculare discount seller
Compania X vinde mărfuri la punctele de vânzare pentru cumpărători wholesale și retail.
Clienții wholesale primesc o reducere de două procente la toate comenzile.
De asemenea, compania încurajează atât clienții wholesale, cât și clienții cu amănuntul să
plătească ramburs la livrare, oferind o reducere de două procente pentru această metodă de plată.
Încă o reducere de două procente este acordată pentru comenzile de 50 sau mai multe unități.'''

'''tip_cumparator = input('Va rugam introduceti tipul de cumparator')
tip_plata = input('Va rugam introduceti tipul de plata')
nr_unitati = int(input('Va rugam introduceti numarul de unitati'))
pret_unitate = float(input('Va rugam introduceti pretul per unitate'))
discount_total = 0
if tip_cumparator == 'wholesale':
    discount_total = 0.02
if tip_plata == 'cash':
    discount_total = discount_total+0.02
if nr_unitati>=50:
    discount_total = discount_total+0.02
pret_total = pret_unitate * nr_unitati
pret_discount = pret_total - pret_total*discount_total'''

'''Ex_3 - Introduceți un nume de film de la tastatură și evaluați dacă numele acelui film este numele filmului
vostru preferat. Dacă da, atunci printați pe ecran: “Acesta este filmul meu preferat”.
În caz contrar printați pe ecran: “Din pacate nu este filmul meu preferat”. '''

'''nume_film = input('Introduceti numele filmului')
if nume_film == "Breakfast at Tiffany's":
    print("Acesta este filmul meu preferat")
else:
    print('Din pacate nu este filmul meu preferat')'''

'''Ex_4 - Aveți la dispoziție următorul database 
url: jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC
Extrageți din acest text numele bazei de date: mysql.db.server
Folosiți un if statement pentru a evalua dacă numele bazei de date este cel corect (presupunând că extrageți url-ul 
dintr-un sistem extern și nu știți care este acesta)'''

'''database_url = 'jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC'
nume_baza_de_date = database_url[34:database_url.index('?')]
print(nume_baza_de_date)'''

















