from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mechanic_shop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Customer Model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))
    
    def __repr__(self):
        return f'<Customer {self.first_name} {self.last_name}>'

# Customer Schema for serialization/deserialization
class CustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Customer
        load_instance = True
        
    id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    address = ma.auto_field()

# Initialize schemas
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

# CRUD Routes

# Create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        customer = customer_schema.load(request.json, session=db.session)
        db.session.add(customer)
        db.session.commit()
        return customer_schema.dump(customer), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return customers_schema.dump(customers), 200

# Get a specific customer
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return customer_schema.dump(customer), 200

# Update a customer
@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    
    try:
        updated_customer = customer_schema.load(request.json, instance=customer, session=db.session)
        db.session.commit()
        return customer_schema.dump(updated_customer), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete a customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return '', 204

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
