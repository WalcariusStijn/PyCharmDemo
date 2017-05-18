test_woord = "Basic Programming"
print(test_woord[0])
print(test_woord[6:])
print(test_woord[6:9])

list1 = ['1NMCT1', '1NMCT2', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [True, False, False, True]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

list4[2] = True  # update
del list4[3]  # delete
print(list4)

print(list1 + list2)
print(list2 * 2)
if (7 in list2): print("element 7 is aanwezig")
for x in list3:
    print(str.upper(x))
print(list3)

# set: unieke values
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("Set: " + str(basket))
print(max(basket))
for x in basket:
    print(x)

geboortejaren = {1998, 1997, 1995, 1996, 1999, 2000, 1997, 1996, 2001}
print("De %d unieke geboortejaren zijn: " % len(geboortejaren))
print(geboortejaren)

unieke_letters = set("stijn walcarius")
print(unieke_letters)
#print(unieke_letters[0])


mijn_dict = {"a": "alpha", "o": "omega", "g": "gamma"}
print(mijn_dict)
print("Opvragen van een waarde uit de dictionary ahv zijn key:")
print(mijn_dict.get("a","niets gevonden voor deze key"))
print(mijn_dict.get("z","niets gevonden voor deze key"))


mijn_dict["t"] = "theta"        #toevoegen van key & value
del mijn_dict["o"]              #verwijderen van value mbv key
print(mijn_dict)

#list(d.keys()) on a dictionary returns a list of all the keys used in the dictionary
if ("t" in list(mijn_dict.keys())):      #controle op aanwezigheid van key
    print("key is aanwezig")
else:
    print("key is niet aanwezig")

# Herhaling?
# Lists (=an collection of objects) --> arrays
# verschillen tov andere programmeertalen
# elementen hoeven niet van het zelfde type te zijn
# •They are ordered
# •The contain arbitrary objects
# •Elements of a list can be accessed by an index
# •They are arbitrarily nestable, i.e. they can contain other lists as sublists
# •Variable size
# •They are mutable, i.e. the elements of a list can be changed
# kunnen groeien at runtime
list1 = [42, "What's the question?", 3.1415]
# kunnen sublists bevatten
person = [["Marc", "Mayer"], ["17, Oxford Str", "12345", "London"], "07876-7876"]

# Tuples: tuple is an immutable list, i.e. a tuple cannot be changed in any way once it has been created



# t[1] = "a" #--> fout!


# slicing --> "subarray"
cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
first_three = cities[0:3]  # [begin,einde[
for city in first_three:
    print(city)
print(first_three)
print(cities[2:])  # afprinten vanaf een bepaalde positie
print(cities[0:5:2])  # stapgrootte meegeven

print("Lengte orginele array: %d " % len(cities))

# controle of element in list aanwezig is
# if ("red" in colors1):
#     print("red aanwezig")


# Of beter met een klein deelprobleem
def checkColorInList(checkColor, *arg_colors):
    if checkColor in arg_colors:
        return "red aanwezig"
    else:
        return "niet aanwezig"


# print("Controleer rood in list colors1: %s " % checkColorInList("red", *colors1))
# print("Controleer rood in list colors2: %s " % checkColorInList("red", *colors2))
# print("Controleer rood in list colors: %s " % checkColorInList("red", *colors))

# Herhalingen van lists via de * operator
# y1 = colors1 * 4  #result : 1 list
# print(y1)
# y2 = [colors1] *4  #result : nested list
# print(y2)
# y2[0][0] = "z"      #opgelet met referenties
# print(y2)

# Dictionaries:
# no ordering in dictionaries
# dictionaries are unordered sets. But the main difference is that items in dictionaries are accessed via keys and not via their position.

# http://www.python-course.eu/python3_dictionaries.php
print("Dictionaries")
NMCT = {"1NMCT": 123, "2NMCT": 458, "3NMCT": 485}
for key, val in NMCT.items():
    print("%s -> %s" % (key, val))

# print(NMCT["1NMCT"])
# print(NMCT["4NMCT"])  #KeyError

# no ordering in dictionaries
print(NMCT)
# add another entry to an existing dictionary
NMCT["4NMCT"] = 8541
print(NMCT)

# keuze keys
# We can use arbitrary types as values in a dictionary, but there is a restriction for the keys. Only immutable data types can be used as keys, i.e. no lists or dictionaries can be used:
# If you use a mutable data type as a key, you get an error message:

# Toepassing: maak switch-case in Python via Dictionary
choices = {'a': 1, 'b': 2}
key = 'a'
result = choices.get(key, 'default')
print(result)


def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")


print(numbers_to_strings(2))
print(numbers_to_strings(12))


# In Python we can also include functions or lambdas in our dictionary mapping
def zero():
    return "zero result"


def one():
    return "one result"


def numbers_to_functions_to_strings(argument):
    switcher = {
        0: zero,
        1: one,
        2: lambda: "two",
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "nothing")
    # Execute the function
    return func()


print(numbers_to_functions_to_strings(2))


# schrijf een functie dat over een dictionary itereert
# A double asterisk in front of the dict parameter below means any other named parameters
def printVals(prefix='', **dict):
    # Print out the extra named parameters and their values
    for key, val in dict.items():
        print('%s [%s] => [%s]' % (prefix, str(key), str(val)))


printVals(prefix='..', NMCT1=123, NMCT2=458, NMCT3=485)


def printVals(**dict):
    # Print out the extra named parameters and their values
    for key, val in dict.items():
        print('[%s] => [%s]' % (str(key), str(val)))


printVals(**NMCT)

