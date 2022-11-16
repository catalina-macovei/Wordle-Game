def char_frequency(dataset):   #calculeaza frecventa literelor in cuvinte si le sorteaza intr-un alt dictionar
    list_of_char = [chr(x + 65) for x in range(0, 26)]
    d = {y:str(dataset).count(y) for y in set(list_of_char)}
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict.items())

def get_wordle_data_set():  # citeste datele din fisier
    f = open("data/cuvinte_wordle.txt", "r")
    return [line[:-1] for line in f]
    