from flask import Flask
from flask import jsonify, request
from flask.views import MethodView
from flask_cors import CORS
from config import mongo_client
from datetime import datetime

app = Flask(__name__)
CORS(app)


class AuthAPI(MethodView):
    def post(self):
        data = request.get_json(force=True)
        if not mongo_client.find_one({'user_id': data['user_id']}):
            mongo_client.insert({'user_id': data['user_id']})
        mongo_client.update({'user_id': data['user_id']}, {'$set': {'last_login': datetime.utcnow()}})
        return jsonify({'message': 'User is authenticated'}), 200

view = AuthAPI.as_view('auth_api')
app.add_url_rule('/auth', view_func=view, methods=['POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)