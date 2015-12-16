# eq-survey-registry

## Installing Couch DB

1. Ubuntu: sudo apt-get install couchdb
   Mac: brew install couchdb
2. Verify installation http://localhost:5984/_utils/index.html
3. Browse http://localhost:5984/_utils/index.html
4. Create database `survey-registry`


## Running the Survey Registry
1. Either:
    Set an environment variable for couchdb: COUCHDB_SERVER=http://localhost:5984
    Add an entry in /etc/hosts for couchdh: 127.0.0.1 couchdb
2. python survey_registry.py
