# Import the Flask dependency
from flask import Flask
# Create a new Flask instance called 'app'
app = Flask(__name__)
# Define the root
@app.route('/')
# Create a function
@app.route('/')
def hello_world():
    return 'Hello world'