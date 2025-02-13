# 🔧 Mechanic Shop Customer Management API

A modern, RESTful API built with Flask for managing customer data in an automotive repair shop. This project demonstrates best practices in API design, data validation, and database management.

## 🌟 Features

- **Full CRUD Operations**: Complete customer management functionality
- **Data Validation**: Request validation using Marshmallow schemas
- **Database Integration**: SQLite database with SQLAlchemy ORM
- **RESTful Design**: Following REST architectural principles
- **Clean Architecture**: Separation of concerns between models, schemas, and routes

## 🛠️ Technologies Used

- **Flask**: Lightweight WSGI web application framework
- **SQLAlchemy**: SQL toolkit and ORM
- **Marshmallow**: Object serialization/deserialization library
- **SQLite**: Lightweight disk-based database

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mechanic-shop-api.git
cd mechanic-shop-api
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## 📚 API Documentation

### Customer Endpoints

#### Create Customer
- **URL**: `/customers`
- **Method**: `POST`
- **Body**:
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St"
}
```
- **Success Response**: `201 Created`

#### Get All Customers
- **URL**: `/customers`
- **Method**: `GET`
- **Success Response**: `200 OK`

#### Get Single Customer
- **URL**: `/customers/<customer_id>`
- **Method**: `GET`
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`

#### Update Customer
- **URL**: `/customers/<customer_id>`
- **Method**: `PUT`
- **Body**: Same as create customer
- **Success Response**: `200 OK`
- **Error Response**: `404 Not Found`

#### Delete Customer
- **URL**: `/customers/<customer_id>`
- **Method**: `DELETE`
- **Success Response**: `204 No Content`
- **Error Response**: `404 Not Found`

## 🧪 Testing

Test the API using curl:

```bash
# Create a customer
curl -X POST http://localhost:5000/customers \
-H "Content-Type: application/json" \
-d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St"
}'

# Get all customers
curl http://localhost:5000/customers
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📬 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/mechanic-shop-api](https://github.com/yourusername/mechanic-shop-api)
