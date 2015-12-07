from flask import Flask, request, g
from flask_restful import Resource, Api
from flaskext.couchdb import CouchDBManager
import os

app = Flask(__name__)
api = Api(app)

manager = CouchDBManager()

manager.setup(app)

registry = {}

app.config['COUCHDB_SERVER'] = os.environ.get('COUCHDB_SERVER', 'http://localhost:5984/')
app.config['COUCHDB_DATABASE'] = os.environ.get('COUCHDB_DATABASE', 'survey-registry')


class SurveyRegistry(Resource):

    def get(self, questionnaire_id):
        print questionnaire_id
        document = g.couch.get(questionnaire_id)
        print document
        if document:
            return document['content']
        else:
            return {}

    def post(self, questionnaire_id):
        questionnaire_data = request.get_json()
        document = dict(title=questionnaire_id, content=questionnaire_data)
        g.couch[questionnaire_id] = document
        return {'success': 'True'}

api.add_resource(SurveyRegistry, '/<string:questionnaire_id>')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8081)
