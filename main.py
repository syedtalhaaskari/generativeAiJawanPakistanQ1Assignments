from flask import Flask

from controller.ecommerce.category import category
from controller.ecommerce.product import product

app = Flask(__name__)

app.register_blueprint(category)
app.register_blueprint(product)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)