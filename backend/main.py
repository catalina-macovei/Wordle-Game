import random
from flask import *
import json, time
from flask import jsonify
from wordle_funcs import *

app = Flask(__name__)
secret_word = get_random_secret_word()

char_frequency(dataset)

@app.route('/user/', methods=['GET'])
def request_page():
        user_guess = str(request.args.get('input'))
        isGuessed = user_guess == secret_word
        correctIndexes = []
        existingIndexes = []
        global user_guess_cpy 
        user_guess_cpy = user_guess
        global the_secret_word_cpy 
        the_secret_word_cpy = secret_word
        if not isGuessed:
                correctIndexes = correct_index_func(user_guess, secret_word)
                existingIndexes = existing_index_func(user_guess_cpy, the_secret_word_cpy)
        
        response = jsonify({'userGuess': user_guess, "isGuessed": isGuessed, "correctIndexes": correctIndexes, "existingIndexes": existingIndexes, 'secret': secret_word})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/data/', methods=['GET'])
def wordle_page():
        global secret_word
        secret_word = get_random_secret_word()
        response = jsonify({'data': dataset})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == '__main__':
    app.run(port=8000)

