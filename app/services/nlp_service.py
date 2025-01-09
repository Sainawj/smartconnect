import json
from flask import Flask, request, jsonify
from transformers import BertForSequenceClassification, BertTokenizer
import torch

# Load the model and tokenizer from file_nlp
model = BertForSequenceClassification.from_pretrained('../data/file_nlp')
tokenizer = BertTokenizer.from_pretrained('../data/file_nlp')


# Load the JSON file 
with open('../data/dataset/faq_dataset.json', 'r') as file:
    data = json.load(file)

# function to predict the category
def predict_question(question):
    inputs = tokenizer(question, return_tensors="pt", truncation=True, padding=True, max_length=128)

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predicted_class_idx = torch.argmax(logits, dim=1).item()

    # Labels of categories
    labels = ['shipping', 'returns', 'produt', 'general']
    predicted_label = labels[predicted_class_idx]

    # Chech ID and answer for category predict
    matching_data = [item for item in data if item['label'] == predicted_label]

    # Return ID question and her la reponse corresponding
    question_data = matching_data[0]  # I review this after
    return question_data['idQuestion'], question_data['answer'], predicted_label
