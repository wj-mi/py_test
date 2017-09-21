# -*- coding:utf-8 -*-

from flask import Flask, request, jsonify
# from models import User, DBsession
from flask_migrate import Migrate
from flask_restful import fields


app = Flask(__name__)
app.config["USER_SECRET_KEY"] = "@#$%^&whhdd)()*&*&hshbd--"
# session = DBsession()
# migrate = Migrate(app, DBsession)



@app.route("/")
def hello():
    return jsonify("hello world!")


@app.route("/register", methods=['OPTIONS', 'POST'])
def register():
    args = request.json
    print '---login args:', args
    # user = User()
    # if args.get("username", ''):
    #     user.name = args.get("username")
    # passwd = args.get("password", '')
    # user.hash_password(passwd)
    # session.add(user)
    # session.commit()
    # session.close()
    return jsonify({'code': 1, 'data': args})


@app.route("/login", methods=['OPTIONS', 'POST'])
def login():
    args = request.json
    # if not args:
    #     return jsonify({'code': -1, 'message': 'args error!'})
    # user = User.query.filter_by('name', args.get('username'))
    # passwd = args.get('password', '')
    # if user.verify_password(passwd):
    #     token = user.generate_auth_token()
    #     return jsonify({'code': 1, 'data': token})
    # return jsonify({'code': -1, 'data': "password error"})
    if args:
        return jsonify({'code':1, 'data':args})
    return jsonify({'code':-1, 'data': 'no args'})


user_fileds = {
    'id': fields.Integer,
    'name': fields.String
}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
