from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/hello',methods=['GET'])
def mine_block():
    response="Welcome"
    return response
app.run(host='0.0.0.0',port=5003)