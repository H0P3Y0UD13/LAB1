import json


def table_make(stat_param):
        if round(int(stats[stat_param])/10) > i:
            return "XXXX"
        else:
            return "    "


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

print("Статы какого покемона вы хотите увидеть?")
pokemon_src = input()
objects = json.loads(str_pokemon_f)
pokemon_name = ""
abilities = ""
max_description = 0
max_words = 0
for profile in objects:
    stats = profile["stats"]
    tags = ["hp", "attack", "defense", "sp.atk", "sp.def", "speed"]
    description = profile["description"]
    if profile["name"] == pokemon_src:
        for i in reversed(range(0,16)):
            for j in range(0,6):
                if tags[j] != "speed":
                    print("%-8s" % (table_make(tags[j])), end='')
                else:
                    print("%-8s" % (table_make(tags[j])))
            if i == 0:
                for j in range(0,6):
                    if tags[j] != "speed":
                        print("%-8s" % (tags[j]), end='')
                    else:
                        print("%-8s" % (tags[j]), "\n")
    for skills in profile["abilities"]:
        if max_words < len(skills.split()):
            max_words = len(skills.split())
            abilities = skills
    if max_description < len(description):
        max_description = len(description)
        pokemon_name = profile["name"]
print(f"Покемон {pokemon_name} имеет наиболее длинное описание")
print(f"Умение {abilities} содержит больше всего слов")