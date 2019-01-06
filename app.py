from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////app/hello.db' #database file (sqlite)
dbase=SQLAlchemy(application)

class User(dbase.Model):
    id=dbase.Column(dbase.Integer,primary_key=True)
    name=dbase.Column(dbase.String(255)) # It will help in creating database in the sqlite database
    def __repr__(self):
        return '<Name %r>' % self.name 


@application.route('/hello',methods=['GET','POST'])
def hello():
    if(request.method =='POST'):
        userinput= request.get_json()
        return jsonify({'You typed':userinput}),202 #I set response code to 202
    else:
        return jsonify({'You are': 'Stranger'})
@application.route('/hello/<string:var>',methods=['GET'])
def retr(var):
    vr=User(name=var)
    dbase.session.add(vr)   #write the name to the database
    dbase.session.commit()
    us=User.query.all()
    print(us)
    return jsonify({'Hello':var}) #return the string entered at the RESSFULL endpoint as JSON data

if  __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
