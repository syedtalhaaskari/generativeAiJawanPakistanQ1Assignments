from flask import Flask

# Notes Blueprints imports
from controller.notes.signup import signup
from controller.notes.signin import signin
from controller.notes.category import notes_category
from controller.notes.notes import notes

app = Flask(__name__)

# Notes
app.register_blueprint(signup)
app.register_blueprint(signin)
app.register_blueprint(notes_category)
app.register_blueprint(notes)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)