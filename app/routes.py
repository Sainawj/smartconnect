import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import BertForSequenceClassification, BertTokenizer
import torch
from services.nlp_service import predict_question
from pymongo import MongoClient
from datetime import datetime

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']
collection = db['faq_questions']

app = Flask(__name__)
# CORS(app)

# Fonction pour insérer dans la base de données
def insert_question_to_db(question_id, question, answer, category):
    question_data = {
        "id": question_id,
        "question": question,
        "answer": answer,
        "category": category,
        "date": datetime.now()
    }
    try:
        collection.insert_one(question_data)
        print(f"Question '{question}' inserted into MongoDB.")
    except Exception as e:
        print(f"Error inserting question into MongoDB: {e}")

@app.route('/')
def home():
    print("Rendering index.html")
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Error rendering index.html: {e}")
        return jsonify({'error': 'Failed to load the home page'}), 500

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        question = data.get("question")

        if not question:
            return jsonify({'error': 'No question provided'}), 400

        # Predict answer
        question_id, answer, category = predict_question(question)
        print(f"Predicted answer: {answer}")

        # Insert in MongoDB
        insert_question_to_db(question_id, question, answer, category)

        return jsonify({'question_id': question_id, 'question': question, 'answer': answer})
    except Exception as e:
        print(f"Error in /ask route: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

