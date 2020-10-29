# https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('direction', type=int, required=True, help='angle direction, entre 0 et 1024')
parser.add_argument('speed', type=int, required=True, help='vitesse, entre 0 et 1024')

class Health(Resource):
    def get(self):
        # Do your checks and return a status
        return {'state': 'ok'}

class Move(Resource):
    def get(self):
        
        # get arguments from URL
        args = parser.parse_args()
        direction = args['direction']
        speed = args['speed']

        # Do some actions

        comment = 'vitesse de zero = stop'

        # Definition du message en retour
        json = {
            'direction'   : direction,
            'speed'       : speed,
            'explication' : comment
        }

        return(json)

api.add_resource(Health,
    '/',
    '/health')
api.add_resource(Move, '/move')

if __name__ == '__main__':
    app.run(debug=True)

