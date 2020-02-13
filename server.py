from os import environ
from flask import Flask

app = Flask(__name__)
app.run(host= environ.get('HOST'), port=environ.get('PORT'))