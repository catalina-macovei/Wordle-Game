from flask import *
from flask import jsonify
from wordle_funcs import *
from flask_cors import CORS,cross_origin
import math


app = Flask(__name__)
CORS(app, support_credentials=True)

global secret_word

@app.route('/average', methods=['GET'])
@cross_origin(supports_credentials=True)
def request_avg():
        #call function get_avg()
        return jsonify({'avg': 3.8})


@app.route('/user/', methods=['GET'])
@cross_origin(supports_credentials=True)
def request_page():
        user_guess = str(request.args.get('input'))
        isGuessed = user_guess == secret_word
        
        results = correct_index_func(user_guess, secret_word)

        res = {'userGuess': user_guess, "isGuessed": isGuessed, "correctIndexes": results.get('correctIndexes'), "existingIndexes": results.get('existingIndexes'), 'secret': secret_word}

        isEntropy = str(request.args.get('isEntropy')) if str(request.args.get('isEntropy')) != "None" else 0
        if isEntropy == '1':
                res['entropy_set'] = H_cuv(results['dataset'])[:10]
                
        response = jsonify(res)
        return response

@app.route('/data/', methods=['GET'])
@cross_origin(supports_credentials=True)
def wordle_page():
        global secret_word
        secret_word = get_random_secret_word()
        secret_word = "UEDUL"
        isEntropy = str(request.args.get('isEntropy')) if str(request.args.get('isEntropy')) != "None" else 0
        res = {'data': dataset}
        if isEntropy == '1':
                res['entropy_set'] = H_cuv(dataset)[:10]
        response = jsonify(res)
        return response


if __name__ == '__main__':
    app.run(port=8000)

