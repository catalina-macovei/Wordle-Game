import random

def char_frequency(dataset):   #calculeaza frecventa literelor in cuvinte si le sorteaza intr-un alt dictionar
    list_of_char = [chr(x + 65) for x in range(0, 26)]
    d = {y:str(dataset).count(y) for y in set(list_of_char)}
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

def get_wordle_data_set():  # citeste datele din fisier
    f = open("data/cuvinte_wordle.txt", "r")
    wordsArray = [line[:-1] for line in f]
    wordsArray.pop(len(wordsArray) - 1)
    return wordsArray


dataset = get_wordle_data_set()  # stocheaza o lista cu cuvintele din fisier


def get_random_secret_word():
    return dataset[random.randint(0, len(dataset))]


# pentru fiecare cuvant secret gaseste 1.lista index la pozitia fixa a literei si 2.lista index la pozitia literei care exista in cuvant


def correct_index_func(user_guess, the_secret_word):   # pentru fiecare cuvant secret gaseste si returneaza 1.lista index la pozitia fixa a literei
    global user_guess_cpy
    global the_secret_word_cpy
    user_guess_cpy = user_guess
    the_secret_word_cpy = the_secret_word
    list_index = []
    for i in range(len(user_guess)):
        if user_guess[i] == the_secret_word[i]:
            user_guess_cpy = user_guess_cpy[0:i] + "0" + user_guess_cpy[i + 1:]
            the_secret_word_cpy = the_secret_word_cpy[0:i] + "1" + the_secret_word_cpy[i + 1:]
            list_index.append(i)
    return list_index

  
def existing_index_func(user_guess_cpy, the_secret_word_cpy):   # 2.returneaza lista index la pozitia literei care exista in cuvant
    list_index = []
    for i in range(len(user_guess_cpy)):
        if user_guess_cpy[i] in the_secret_word_cpy:
            index = the_secret_word_cpy.index(user_guess_cpy[i])
            list_index.append(i)
            the_secret_word_cpy = the_secret_word_cpy[0:index] + "1" + the_secret_word_cpy[index + 1:]
    return list_index

# optimization functions using entropy:
    

