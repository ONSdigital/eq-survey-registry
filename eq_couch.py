from couchdb import ResourceNotFound, PreconditionFailed, Server
import os
import time


try:
    # temporary solution whilst we continue to use docker compose
    time.sleep(3)
    server = Server(url=os.environ.get('COUCHDB_SERVER', 'http://couchdb:5984/'))
    db = server['survey-registry']
except ResourceNotFound:
    try:
        db = server.create('survey-registry')
    except PreconditionFailed:
        raise SystemError

