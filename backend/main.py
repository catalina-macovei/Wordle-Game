from flask import *
import json, time
from flask import jsonify
from wordle_funcs import *

app = Flask(__name__) 

dataset = get_wordle_data_set()  # stocheaza o lista cu cuvintele din fisier
char_frequency(dataset)
@app.route('/', methods=['GET'])
def home_page():
        data_set = {'Page':'Home'}
        json_dump = json.dumps(data_set)

        return json_dump

@app.route('/user/', methods=['GET'])
def request_page():
        user_query = str(request.args.get('user'))

        data_set = {'Page':'Request', 'user':user_query}
        json_dump = json.dumps(data_set)

        return json_dump


@app.route('/data/', methods=['GET'])
def wordle_page():
        response = jsonify({'Page':'Wordle', 'data': dataset, 'avg': 1324})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == '__main__':
    app.run(port=8000)

