import random
from flask import *
import json, time
from flask import jsonify
from wordle_funcs import *

app = Flask(__name__)
secret_word = get_random_secret_word()

char_frequency(dataset)
@app.route('/', methods=['GET'])
def home_page():
        data_set = {'Page':'Home'}
        json_dump = json.dumps(data_set)

        return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
        user_guess = str(request.args.get('input'))
        isGuessed = user_guess == secret_word
        correctIndexes = correct_index_func(user_guess, secret_word)
        existingIndexes = existing_index_func(user_guess, secret_word)
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

