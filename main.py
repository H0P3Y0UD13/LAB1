import json


file = open("pokemon_full.json")
str_pokemon_f = file.read()
len_str = len(str_pokemon_f)
print("Общее количество символов в файле - ", len_str)
file.close()

count = 0
for symbol in str_pokemon_f:
    if symbol.isalnum():
        count += 1
print("Общее количесто символов без пробелов и знаков препинания - ", count)

objects = json.loads(str_pokemon_f)
pokemon_name = ""
abilities = ""
max_description = 0
max_words = 0
for profile in objects:
    description = profile["description"]
    for skills in profile["abilities"]:
        if max_words < len(skills.split()):
            max_words = len(skills.split())
            abilities = skills
    if max_description < len(description):
        max_description = len(description)
        pokemon_name = profile["name"]
print(f"Покемон {pokemon_name} имеет наиболее длинное описание")
print(f"Умение {abilities} содержит больше всего слов")