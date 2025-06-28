
# messed_pokemon = 'BulbAsaur-ChaRMAndeR-pikaCHU-chariZard-SQuirtlE'

# messed_pokemon_list = messed_pokemon.split('-')

# pokedex = []

# for character in messed_pokemon_list:
#     character_cap = character.capitalize()
#     if character_cap != 'Charizard':
#         pokedex.append(character_cap)

# print(pokedex)
# def double(num):
#     global int_val
#     int_val = num * 2

# int_val = 2
# double(int_val)

# print(int_val)  # outputs: 2


# def last_element(input_list):
#     x = input_list[-1] 
#     return x

# my_list = [1, 5, 3, 7]

# print(last_element(my_list) == 7)  # True
# print(my_list == [1, 5, 3, 7])     # False
# list_1 = ['Hi', 'hello', 'YO']
# list_2 = [45, 9, 10, 22, 77, 8, 8]

# print(last_element(list_1) == 'YO')         # True
# print(list_1 == ['Hi', 'hello', 'YO'])      # True
# print(last_element(list_2) == 8)            # True
# print(list_2 == [45, 9, 10, 22, 77, 8, 8])  # True



#############

# num = "77"

# friends = {1: "Bill", 2: "Bob", 3: "Jake", 4: "Aaron"}

# def play_round(item):
#     num, name = item
#     print()
#     print(f"{name} wants the secret number")
#     if name == "Bob":
#         print("'Ok', says Joey. Here is the secret number:")
#         print(f"{num}")
#     else:
#         print("No way!")

# for item in friends.items():
#     print(item)
#     play_round(item)

#########
# original code

# VALID_COUNTRY_CATEGORIES = {
#     "former_ottoman_empire": ["Macedonia", "Hungary", "Greece"],
#     "most_populous": "China",
# }

# def country_category_validation(categorized_countries):
#     for key, value in categorized_countries.items():
#         if VALID_COUNTRY_CATEGORIES.get(key, None) != value:
#             return False

#     return True

# print(country_category_validation({
#     "most_populous": "China",
#     "former_ottoman_empire": ["Macedonia", "Hungary", "Greece"],
# }))

## trial & error

VALID_COUNTRY_CATEGORIES = {
    "former_ottoman_empire": ["Macedonia", "Hungary", "Greece"],
    "most_populous": "China",
}

def country_category_validation(categorized_countries):
#    for key, value in categorized_countries.items():
#        if VALID_COUNTRY_CATEGORIES.get(key, None) != value:
    for key, value in VALID_COUNTRY_CATEGORIES.items():
        if categorized_countries.get(key, None) != value:
            return False

    return True

print(country_category_validation({
    "most_populous": "China",
    "former_ottoman_empire": ["Macedonia", "Hungary", "Greece"],
    'one more': 'thing'
}))