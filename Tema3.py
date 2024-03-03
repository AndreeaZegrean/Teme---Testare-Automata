# LISTE
#1. Declarați o listă cu elemente multitype
# lista_1 = [1, 'Ana', 3.2, True, 1, 5, 6]

#2. Declarați o listă goală
#lista = []

#3. Accesați orice element din listă pe baza de index
#print(lista_1[2])

#4. Accesați poziția unui element din listă pe baza funcției index()
# print(lista_1.index(3.2))

#5. Adăugați elemente în listă atât cu funcția append() cât și cu funcția insert(). Observați rezultatele
# cu append il adauga la final
'''lista_1.append(35)
print(lista_1)'''

# cu insert il adauga in interiorul listei, dar trebuie specificat indexul pe care il va avea
'''lista_1.insert(1, 80)
print(lista_1)'''

#6. Ștergeți elemente din listă atat cu funcția pop() cât și cu funcția remove(). Observați rezultatele
# stergere elemente din lista, doar primul de acel fel
'''lista_1.remove(1)
print(lista_1)'''

# sterge element dupa index
'''lista_1.pop(5)
print(lista_1)'''

#7. Numărați elementele dintr-o listă folosind funcția len()
# print(len(lista_1))

#8. Numărați de câte ori apare un anumit element în listă folosind funcția count()
# print(lista_1.count(1))

#9. Uniți două liste folosind functia extend()
'''lista_2 = [77, 'Razvan', 40, False, 26]
lista_1.extend(lista_2)
print(lista_1)'''

#10. Sortați lista folosind functia sort() - ascendet
'''lista_3 = [201, 77, 24, 33, 40, 5, 26]
lista_3.sort()
print(lista_3)'''

#11. Inversați conținutul listei folosind functia reverse() - descendet
'''lista_3.reverse()
print(lista_3)'''

#12. Ștergeți toate elementele din listă folosind funcția clear()
'''lista_3.clear()
print(lista_3)'''

# TUPLURI
#1. Declarați un tuplu
tuplu_1 = (77, 9, 35, 23.4, 'Deea', False, 77, 2, 5, 77)
print(tuplu_1)

#2. Declarați un tuplu gol
# tuplu = ()

#3. Accesați orice element din tuplu pe bază de index
#print(tuplu_1[3])

#4. Accesați poziția unui element din listă pe baza funcției index()
#print(tuplu_1[1:4:2])

#5. Folosiți funcția count() pentru a număra de câte ori apare un element în tuplu
#print(tuplu_1.count(77))

#6. Folosiți funcția index() pentru a verifica poziția la care se află un anumit element în tuplu
'''tuplu_1.index[77]
print(tuplu_1[])'''

#7. Încercați să modificați un element din tuplu și observați rezultatele

# SETURI
#1. Declarați un set
set_1 = {1, 2, 3, 4, 2, 77}
print(set_1)

#2. Declarați un set gol
#set.elem = set()

#3. Adăugați un element nou în set folosind funcția add()
set_1.add(9)
#print(set_1)

#4. Ștergeți un element din set folosind funcția pop() și respectiv funcția remove(). Observați rezultatele
# sterge elementele dorite
#set_1.remove(2)
#print(set_1)

# scoate aleatoriu un element din lista, in cazul nostru primul
#set_1.pop()
#print(set_1)

#5. Verificați dacă un set este o subdiviziune a unui alt set (subset)

#5. Verificați dacă un set este o subdiviziune a unui alt set (subset)
#6. Verificați dacă un set conține toate elementele dintr-un alt set + alte elemente (superset)
#7. Verificați care sunt elementele comune între două seturi (intersection)
#8. Verificați diferența între două seturi cu funcția difference()

#9. Ștergeți toate elementele dintr-un set folosind funcția clear()
'''set_1.clear()
print(set_1)'''

# DICTIONARE
#1. Declarați un dicționar
dict_1 = {'Nume': 'Monica', 'Prenume': 'Asha',
          'varsta': 35,
          'telefon': '0754673489',
          'media_bac': 9.55}
print(dict_1['Nume'])
print(dict_1['varsta'])

#2. Declarați un dicționar gol
# dict = {}

#3. Adăugați un element nou în dicționar folosind funcția update() și respectiv pe baza de cheie
'''dict_2 = {10: 2, 'user_1': 'admin',
          'user_2': {'nume': 'Ale', 'email': 'ale@yahoo.com'}}
print(dict_2['user_2']['nume'])
print(dict_2['user_2']['email'])

dict_2.update({'user_2': 'Bogdan'})
print(dict_2['user_2'])'''

#4. Extrageți un element din dicționar folosind metoda get() și respectiv pe baza de cheie
'''dict_2.get('nume')
print(dict_2)'''

#5. Ștergeți un element din dicționar folosind funcția pop() și respectiv funcția popitem(). Observați rezultatele
#dict_1.pop(2)
'''dict_1.pop('Nume': 'Monica')
print(dict_1)'''

'''dict_1.popitem('Nume': 'Monica')
print(dict_1)'''

#6. Extrageți pe rând toate cheile, apoi toate valorile, și apoi toate item-urile din dicționar

#7. Ștergeți toate valorile din dicționar folosind metoda clear()
#dict_2.clear()
#print(dict_2)




