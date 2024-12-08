# flask-api-rbac
# Flask API with Role-Based Access Control (RBAC)

This project is a simple API built with Flask that implements role-based access control (RBAC) and uses MongoDB for data storage. It also integrates JWT-based authentication and includes Swagger API documentation.

## Features

- User Registration
- User Login with JWT Authentication
- Role-Based Access Control (RBAC)
- CRUD operations for Projects (admin-only access)
- Swagger UI for API documentation

## Setup Instructions

### 1. Clone the repository
```bash


2. Create and activate a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

3. Install dependencies
bash
Copy code
pip install -r requirements.txt

4. Configure MongoDB
Ensure MongoDB is installed and running on your local machine. You can download MongoDB and run it by executing mongod in your terminal.

Alternatively, you can use a MongoDB cloud service like MongoDB Atlas.

5. Set up environment variables
Create a .env file in the project directory and add your secret key:

makefile
Copy code
SECRET_KEY=your_secret_key
6. Run the Flask app
bash
Copy code
python app.py
By default, the API will run on http://localhost:5000.

7. Access the Swagger UI
Once the app is running, you can access the Swagger UI at:

bash
Copy code
http://localhost:5000/apidocs/
Testing with Postman or cURL
You can test the endpoints using tools like Postman or cURL. Here's an example of testing the login endpoint using cURL:

bash
Copy code
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password"}'
Deployment (Optional)
To deploy the application to AWS Lambda, you can use Zappa. Please follow the instructions in the Zappa documentation for deployment steps.

Swagger Documentation Link
Once deployed, you can access the API documentation at:

bash
Copy code
http://localhost:5000/apidocs/  # Local development
Or if deployed on AWS Lambda:

ruby
Copy code
https://your-api-url.amazonaws.com/dev/apidocs/
