# labo week 5
# Tuples


# t1 = ("1NMCT", "2NMCT", "3NMCT")
# t2 = ("1Devine", "2Devine", "3Devine")
# t3 = ("tuple", False, 3.2, 1)
#
#
# def print_list(naam_verzameling, elementen):
#     print("Verzameling %s:" % naam_verzameling)
#     for element in elementen:
#         print("{0} zit op positie {1}".format(element, elementen.index(element)))
#

# t1[0] = "howest"
# identiek als labo week 4
# print_list("NMCT", t1)
# print_list("Devine", t2)
# print_list("test tuple", t3)
# # t1  = t1 + t2
# t1 *= 2
# print(t1)


# Dictionary
modules = {"Basic Programming": 12, "User 1": 17, "Computer Networks": 8}
# print(modules)
# print(modules.get("User 1"))  # opvragen
# print(modules.get("User 2"))
# print(modules.get("User 3", "Niet aanwezig"))
modules.update({"Data Science": 20})  # toevoegen
modules.update({"Data Science": 19})  # toevoegen met dezelfde key
# del modules["Data Science"]
print(modules)


# test aanwezigheid key
# if "User 1" in modules:
#     print("Key aanwezig")
# else:
#     print("Key niet aanwezig")


def print_dictionary(naam_verzameling, elementen):
    print("Dictionary %s:" % naam_verzameling)
    for key, val in elementen.items():
        print("key: %s -> value: %s" % (key, val))


# def voeg_niew_element_toe(key, value, elementen):
#     if (key in elementen):
#         print("Toevoegen mislukt. Key '%s' reeds aanwezig" % key)
#     else:
#         elementen.update({key: value})


# NMCT = {"1NMCT": 101, "2NMCT": 88, "3NMCT": 77}
# Devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}
# print_dictionary("NMCT", NMCT)
# print_dictionary("Devine", Devine)
#
# Howest = {}
# for d in (NMCT, Devine): Howest.update(d)
# print_dictionary("Howest", Howest)

# test toevoegen van nieuw element met zelfde key
# voeg_niew_element_toe("1IPO", 51, Howest)
# print_dictionary("Howest", Howest)
# voeg_niew_element_toe("1IPO", 10, Howest)

# genererenn van een dictionary waarbij value het kwadraat van de key is
def geef_dict():
    d = {}
    for i in range(1, 21):
        d[i] = i ** 2
    return d


nieuwe_dict = geef_dict()
print_dictionary("kwadraten", nieuwe_dict)


# demo test




def tel_voorkomen_woorden(zin):
    dic = {}
    for woord in zin.split(" "):
        dic[woord.lower()] = dic.get(woord.lower(), 0) + 1
    return dic


zin = "dit is nmct is het niet waar ? Uiteraard NMCT"
print("Onderzochte zin:\n%s\n" % zin)
dic_woorden = tel_voorkomen_woorden(zin)
print_dictionary("Woorden_dic", dic_woorden)
print("Ten einde")
print("Jef Daels")
print("Walcarius Stijn")
print("DEmo")
print("Demo 9")
print("Demo 9B")
print("Demo 9c")
print("Demo 10")
print("Demo 11")
print("Demo 12")





# set:
# ongeordende datastructuur met unieke elementen. Duplicaten worden niet toegelaten.

# list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# mijn_set = set(list)
# print(mijn_set)
#
# postnummers = {8500, 8531, 8010, 8850, 8370}
# postnummers.add(9000)
# postnummers.add(8500)  # dubbel
# postnummers.discard(8010)  # verwijderen
#
# for postcode in postnummers:
#     print(postcode)
#     postcode += 1000
#
# print(postnummers)


# def verhoog_waarde_van_key(mijn_dict, key):
#     if (key in mijn_dict):
#         waarde = mijn_dict.get(key)
#         waarde = waarde + 1
#         mijn_dict.update({key: waarde})  # overriden met zelfde key
#
#
# evaluaties = {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0, "0": 0}
# print("Geef de verschilleden evaluatiecijfers door (sluit af met lege waarde)")
# print("Uitmuntend: 5, Zeer goed: 4, Goed: 3, Voldoende: 2, Onvoldoende: 1, Zwak: 0")
# stop = False
# while (stop == False):
#     feedback_score = input("Geef de nieuwe feedbackscore op: ")
#     if (feedback_score != ""):
#         verhoog_waarde_van_key(evaluaties, feedback_score)
#     else:
#         stop = True
# print("De gegeven zijn verwerkt. Dit is het resultaat:")
# for key, val in evaluaties.items():
#     print("score: %s -> aantal: %s" % (key, val))
#
#

# extra
# In Python we can also include functions or lambdas in our dictionary mapping
# def zero():
#     return "zero result"
#
#
# def one():
#     return "one result"
#
# def two():
#     return "two result"
#
# def numbers_to_functions_to_strings(argument):
#     switcher = {
#         0: zero,
#         1: one,
#         2: two,
#     }
#     # Get the function from switcher dictionary
#     func = switcher.get(argument)
#     # Execute the function
#     return func()
#
# #test
# print(numbers_to_functions_to_strings(1))
