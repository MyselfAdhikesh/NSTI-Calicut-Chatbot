# chatbot.py

import json
from sentence_transformers import SentenceTransformer, util

# Load data
with open("admission_info.json", "r") as f:
    data = json.load(f)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')
question_embeddings = model.encode(questions, convert_to_tensor=True)

def get_answer(user_input):
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(input_embedding, question_embeddings)
    best_match_idx = similarity.argmax()
    return answers[best_match_idx]
