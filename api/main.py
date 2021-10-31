import os
from flask import Flask, jsonify
from dotenv import load_dotenv
# import routes
from routes.mobility import mobility
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2a1_eqea1-^eggi7e*s2m_rv(c&s)mwxhucq59te97n!3r5t&'
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# register routes

app.register_blueprint(mobility, url_prefix='/mobility')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT"))

