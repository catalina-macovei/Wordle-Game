import random
import math


def get_wordle_data_set():  # citeste datele din fisier
    f = open("data/cuvinte_wordle.txt", "r")
    wordsArray = [line[:-1] for line in f]
    wordsArray.pop(len(wordsArray) - 1)
    return wordsArray

global dataset 
dataset = get_wordle_data_set()

def get_random_secret_word():
    return dataset[random.randint(0, len(dataset))]


char_total_count = (len(get_wordle_data_set()) * 5)

def char_frequency(dataset):   #calculeaza frecventa literelor in cuvinte si le sorteaza intr-un alt dictionar
    list_of_char = [chr(x + 65) for x in range(0, 26)]
    char_dict = { i : 0 for i in list_of_char }
    for cuvant in dataset:
        for litera in set(cuvant):
            char_dict[litera] = char_dict.get(litera) + 1

    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


char_frequency_dict = char_frequency(dataset)

def char_probability(dataset):   # calculeaza probabilitatea literelor
    list_of_char = [chr(x + 65) for x in range(0, 26)] #sir de frecventa [A - Z]
    d = {y:str(dataset).count(y)/char_total_count for y in set(list_of_char)}
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


char_probability_dict = char_probability(dataset)

def H_cuv(cuvinte): # calculeaza entropia pentru fiecare cuvant din dataset
    new_dic = {}
    for cuvant in cuvinte:
        s = 0
        for litera in cuvant:
            s = s - char_probability_dict.get(litera) * math.log2(char_probability_dict.get(litera))
        new_dic[cuvant] = round(s, 4)
    sorted_dict = list(sorted(new_dic.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

# pentru fiecare cuvant secret gaseste 1.lista index la pozitia fixa a literei si 2.lista index la pozitia literei care exista in cuvant

def filterDataSet(correctIndexes, existingIndexes, user_guess):
    newDataset = []
    global dataset
    if len(correctIndexes):
        for index in correctIndexes:
            for word in dataset:
                if word[index] == user_guess[index]:
                    newDataset.append(word)
        dataset = newDataset
    if len(newDataset):
        dataset = newDataset
    newDataset = []
    print("first run\n\n\n\n\n")
    print(dataset)
    if len(existingIndexes):
        for index in existingIndexes:
            for word in dataset:
                if word.find(user_guess[index]):
                    newDataset.append(word)
        dataset = newDataset
    if len(newDataset):
        dataset = newDataset
    print("second run\n\n\n\n\n")    
    print(dataset)


def correct_index_func(user_guess, secret_word):   # pentru fiecare cuvant secret gaseste si returneaza 1.lista index la pozitia fixa a literei
    user_guess_cpy = user_guess
    secret_word_cpy = secret_word

    correct_index = []
    for i in range(len(user_guess)):
        if user_guess_cpy[i] == secret_word_cpy[i]:
            user_guess_cpy = user_guess_cpy[0:i] + "0" + user_guess_cpy[i + 1:]
            secret_word_cpy = secret_word_cpy[0:i] + "1" + secret_word_cpy[i + 1:]
            correct_index.append(i)

    existing_index = []
    for i in range(len(user_guess_cpy)): 
        if user_guess_cpy[i] in secret_word_cpy:
            index = secret_word_cpy.find(user_guess_cpy[i])
            existing_index.append(i)
            secret_word_cpy = secret_word_cpy[0:index] + "-" + secret_word_cpy[index + 1:]
            print(user_guess_cpy, secret_word_cpy)
    filterDataSet(correct_index, existing_index, user_guess)
    return {'correctIndexes': correct_index, 'existingIndexes': existing_index}
# optimization functions using entropy:
    
def word_dict(): # returneaza un dictionar cuvant:H(cuv)=0 - de utilizat pentru a crea dictionarul initial cu items din fisierul de cuvinte, la fiecare start a new game
    return {x:0 for x in get_wordle_data_set()}


# update_datset primeste ca parametri dictionarul de cuvinte, cuvantul incercat, lista correct_index si lista existing_index si returneaza un nou dictionar de cuvinte ale carui 
# cuvinte se potrivesc pattern ului dat de un cuvant de 5 litere cu literele corecte pe pozitiile corecte, iar pe pozitiile ramase litere care se pot afla in cuvantul 
# secret, dar care nu au primit raspuns negativ la incercare de guess

import re
def update_dataset(dataset,word,correct_index,existing_index): 
    pattern=[0,0,0,0,0]                                         
    for i in correct_index:                                     
        pattern[i]=word[i]                                       
    list_of_char = [chr(x + 65) for x in range(0, 26)]          
    rest_index = [i for i in range(5) if i not in correct_index]
    existing_index_str = "".join([word[i] for i in existing_index])
    ls = [cuv for cuv in dataset if [True for c in existing_index_str if c in cuv]]
    not_existing_letters = [word[i] for i in rest_index if i not in existing_index]
    possible_letters ="".join([c for c in list_of_char if c not in not_existing_letters])
    for i in rest_index:
        pattern[i]=f"[{possible_letters}]"
    pattern = "".join(pattern)
    pattern = re.compile(pattern)
    existing_index_str = re.compile(existing_index_str)
    ls = pattern.findall(" ".join([cuv for cuv in ls ]))
    dict = H_cuv({cuv:0 for cuv in ls})
    return dict
