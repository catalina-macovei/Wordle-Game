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
        
        results = correct_index_func(user_guess, secret_word)

        res = {'userGuess': user_guess, "isGuessed": isGuessed, "correctIndexes": results.get('correctIndexes'), "existingIndexes": results.get('existingIndexes'), 'secret': secret_word}

        isEntropy = str(request.args.get('isEntropy')) if str(request.args.get('isEntropy')) != "None" else 0
        if isEntropy == '1':
                res['entropy_set'] = H_cuv(results['dataset'])[:10]
                
        response = jsonify(res)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/data/', methods=['GET'])
def wordle_page():
        global secret_word
        secret_word = get_random_secret_word()
        isEntropy = str(request.args.get('isEntropy')) if str(request.args.get('isEntropy')) != "None" else 0
        res = {'data': dataset}
        if isEntropy == '1':
                res['entropy_set'] = H_cuv(dataset)[:10]
        response = jsonify(res)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == '__main__':
    app.run(port=8000)

