# https://raw.githubusercontent.com/cervoise/pentest-scripts/master/password-cracking/wordlists/pokemon-list-en.txt


def read_file(filename):
    with open(filename) as file:
        pokemon = file.readlines()
    pokemon = [item.strip() for item in pokemon]
    return pokemon


print(read_file("pokemon.txt"))
