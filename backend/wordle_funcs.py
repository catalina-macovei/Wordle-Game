import random

def char_frequency(dataset):   #calculeaza frecventa literelor in cuvinte si le sorteaza intr-un alt dictionar
    list_of_char = [chr(x + 65) for x in range(0, 26)]
    d = {y:str(dataset).count(y) for y in set(list_of_char)}
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

def get_wordle_data_set():  # citeste datele din fisier
    f = open("data/cuvinte_wordle.txt", "r")
    return [line[:-1] for line in f]

dataset = get_wordle_data_set()  # stocheaza o lista cu cuvintele din fisier


def get_random_secret_word():
    return dataset[random.randint(0, len(dataset))]


# pentru fiecare cuvant secret gaseste 1.lista index la pozitia fixa a literei si 2.lista index la pozitia literei care exista in cuvant


def correct_index_func(user_guess, the_secret_word):   # pentru fiecare cuvant secret gaseste si returneaza 1.lista index la pozitia fixa a literei
    return [i for i in range(len(user_guess)) if user_guess[i] == the_secret_word[i]]
    
def existing_index_func(user_guess, the_secret_word):  # 2.returneaza lista index la pozitia literei care exista in cuvant
    correct_index = correct_index_func(user_guess, the_secret_word)
    return [user_guess.index(i) for i in user_guess if i in the_secret_word and user_guess.index(i) not in correct_index]

# optimization functions using entropy:
    

