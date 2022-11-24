import random
import math


def get_wordle_data_set():  # citeste datele din fisier
    f = open("data/cuvinte_wordle.txt", "r")
    wordsArray = [line[:-1] for line in f]
    wordsArray.pop(len(wordsArray) - 1)
    f.close()
    return wordsArray

dataset = get_wordle_data_set()

def get_random_secret_word():
    global dataset
    dataset = get_wordle_data_set()
    return dataset[random.randint(0, len(dataset) - 1)]

def char_probability(dataset):   # calculeaza probabilitatea literelor
    char_total_count = len(dataset) * 5
    list_of_char = [chr(x + 65) for x in range(0, 26)] #sir de frecventa [A - Z]
    d = {y:str(dataset).count(y)/char_total_count for y in set(list_of_char)}
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


def H_cuv(cuvinte): # calculeaza entropia pentru fiecare cuvant din dataset
    char_probability_dict = char_probability(dataset)

    new_dic = {}
    for cuvant in cuvinte:
        s = 0
        for litera in set(cuvant):
            s = s - char_probability_dict.get(litera) * math.log2(char_probability_dict.get(litera))
        new_dic[cuvant] = round(s, 4)
    sorted_dict = list(sorted(new_dic.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

# pentru fiecare cuvant secret gaseste 1.lista index la pozitia fixa a literei si 2.lista index la pozitia literei care exista in cuvant

def filterDataSet(correctIndexes, existingIndexes, user_guess):
    newDataset = []
    global dataset
    wrongIndexes = {0,1,2,3,4}-set(correctIndexes+existingIndexes)
    if len(correctIndexes):
        for index in correctIndexes:
            for word in dataset:
                if word[index] == user_guess[index]:
                    newDataset.append(word)
            dataset = newDataset               # stocam lista auxiliara in dataset. Astfel primim o lista mai scurta.
            newDataset = [] 
    
    if len(existingIndexes):
        for index in existingIndexes:
            for word in dataset:
                if word.find(user_guess[index]) != -1 and word[index] != user_guess[index]:
                    newDataset.append(word)
            dataset = newDataset
            newDataset = []

    corr_ex_chars = set([user_guess[i] for i in correctIndexes+existingIndexes])
    if len(wrongIndexes) != 0:
        for index in wrongIndexes:
            if user_guess[index] not in corr_ex_chars:
                i=0
                while i in range(len(dataset)):
                    if user_guess[index] in dataset[i]:
                        del dataset[i]
                    else:
                        i+=1
    def myFunc(word):
        return len(set(word))
    dataset.sort(key=myFunc, reverse=True)     

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
    filterDataSet(correct_index, existing_index, user_guess)
    return {'correctIndexes': correct_index, 'existingIndexes': existing_index, 'dataset': dataset}
# optimization functions using entropy:

