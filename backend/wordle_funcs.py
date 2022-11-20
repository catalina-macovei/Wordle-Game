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
    
def word_dict(): # returneaza un dictionar cuvant:H(cuv)=0 - de utilizat pentru a crea dictionarul initial cu items din fisierul de cuvinte, la fiecare start a new game
    return {x:0 for x in get_wordle_data_set()}

def char_counter(dataset):   # calculeaza numarul literelor
    nr_total_ap_lit = 0
    for cuvant in dataset:
        for x in cuvant:
            nr_total_ap_lit +=1
    return nr_total_ap_lit

def char_probability(dataset):   # calculeaza probabilitatea literelor
    list_of_char = [chr(x + 65) for x in range(0, 26)]
    d = {y:str(dataset).count(y)/char_counter(dataset) for y in set(list_of_char)}
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

import math
def H_cuv(dataset): # calculeaza entropia pentru fiecare cuvant din dataset; in suggestions list vor aparea primele patru cuvinte din dictionarul returnat
    for cuvant in dataset.keys():
        s=0
        for litera in cuvant:
            s = s-char_probability(dataset.keys())[litera]*math.log2(char_probability(dataset.keys())[litera])
        dataset[cuvant]=s
    sorted_dict = dict(sorted(dataset.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

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
