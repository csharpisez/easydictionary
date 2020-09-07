from PyDictionary import PyDictionary
dictionary = PyDictionary()

word = input("Enter Word : ")
dtype = input("Enter Need (meaning,synonym,antonym,translate) : ")

if dtype == "meaning":
    print (dictionary.meaning(f"{word}"))

if dtype == "synonym":
    print (dictionary.synonym(f"{word}"))

if dtype == "antonym":
    print (dictionary.antonym(f"{word}"))

if dtype == "translate":
    language = input("Enter language to translate to (es = espanol/spanish, hi = hindi etc.)")
    print (dictionary.translate(f"{word}",f'{language}'))
