from flask import Flask

from controller.ecommerce.category import category

app = Flask(__name__)

app.register_blueprint(category)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)