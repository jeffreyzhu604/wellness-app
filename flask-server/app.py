from flask import Flask, jsonify, request
from db import db


app = Flask(__name__)

@app.route('/api/addOne', methods=["PUT"])
def addOne():
    addOneQuery =   '''
                        UPDATE score
                            SET score = score + 1
                    '''
    return ''


@app.route('/test')
def getNames():
    if request.method == 'GET':
        for name in names:
            print(name)
    return ''

@app.route('/test', methods=["POST"])
def addName():
    if request.method == 'POST':
        print(request, hello)
        names.append(request.get_json())
    return ''

if __name__ == '__main__':
    app.run(debug=True, port=5000)