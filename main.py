from flask import Flask

from controller.ecommerce.category import category
from controller.ecommerce.product import product
from controller.ecommerce.customer import customer
from controller.ecommerce.order import order
from controller.ecommerce.payment import payment

# Metrics Blueprints


app = Flask(__name__)

app.register_blueprint(category)
app.register_blueprint(product)
app.register_blueprint(customer)
app.register_blueprint(order)
app.register_blueprint(payment)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)