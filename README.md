# **SmartConnect Chatbot**

SmartConnect is an AI-powered chatbot designed to handle business FAQs dynamically and provide personalized responses. Built with Flask, it integrates a custom RESTful API with NLP capabilities using NLTK. The app ensures seamless interaction between the frontend, backend, and database, making it scalable and efficient.

---

## **Features**
- Dynamic FAQ management with CRUD operations.
- AI-powered intent recognition and response generation.
- RESTful API for smooth interaction with the frontend.
- MongoDB for efficient data storage and retrieval.
- User authentication and session management.

---

## **Prerequisites**
Before you begin, ensure you have the following installed:
- **Python**: Version 3.8 or higher
- **pip**: Python package manager
- **MongoDB**: Local or cloud setup
- **Git**: Version control system

---

## **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sainawj/smartconnect.git
   cd smartconnect
2. **Set up a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows
4. **Install dependencies**
     ```bash
     pip install -r requirements.txt
6. **Set up environment variables**
     Create a .env file in the root directory and add the following
     ```bash
     FLASK_ENV=development
     JWT_SECRET_KEY=your_secret_key
     MONGO_URI=mongodb://localhost:27017/smartconnect
     
8. **Run the application**
    ```bash
    python run.py
9. **Access the app**
Open your browser and visit
  ```bash
   http://127.0.0.1:5000
  

