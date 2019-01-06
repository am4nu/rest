from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/hello',methods=['GET','POST'])
def hello():
    if(request.method =='POST'):
        userinput= request.get_json()
        return jsonify({'You typed':userinput}),202 #I set response code to 202
    else:
        return jsonify({'You are': 'Stranger'})
@app.route('/hello/<string:var>',methods=['GET'])
def retr(var):
    return jsonify({'Query':var})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')