from flask import Flask

from controller.ecommerce.category import category
from controller.ecommerce.product import product
from controller.ecommerce.customer import customer
from controller.ecommerce.order import order
from controller.ecommerce.payment import payment

# Metrics Blueprints
from controller.ecommerce.metrics.sales import sales
from controller.ecommerce.metrics.orders import orders
from controller.ecommerce.metrics.payments import payments
from controller.ecommerce.metrics.products import products
from controller.ecommerce.metrics.geography import geography

app = Flask(__name__)

app.register_blueprint(category)
app.register_blueprint(product)
app.register_blueprint(customer)
app.register_blueprint(order)
app.register_blueprint(payment)

app.register_blueprint(sales)
app.register_blueprint(orders)
app.register_blueprint(payments)
app.register_blueprint(products)
app.register_blueprint(geography)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)