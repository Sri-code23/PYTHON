import json
import nltk
import random
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import tkinter as tk
from tkinter import scrolledtext

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

# Load intents from JSON file
with open("intents.json") as file:
    data = json.load(file)

# Prepare the data
patterns = []
labels = []
responses = {}

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        labels.append(intent["tag"])
        responses[intent["tag"]] = intent["responses"]

# Encode labels
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Create a bag of words model
vectorizer = CountVectorizer(tokenizer=nltk.word_tokenize)
X = vectorizer.fit_transform(patterns).toarray()

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X, encoded_labels)

# Function for chatting
def chat():
    print("Start talking with the bot (type quit to stop)!")

    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        # Convert input to bag of words
        inp_vector = vectorizer.transform([inp]).toarray()
        prediction = model.predict(inp_vector)
        tag = label_encoder.inverse_transform(prediction)[0]

        # Get response
        response = random.choice(responses[tag])
        print("Bot:", response)

# Function for GUI chat
def gui_chat():
    def send():
        inp = input_field.get("1.0", "end-1c")
        output_field.insert(tk.END, "You: " + inp + "\n")
        inp_vector = vectorizer.transform([inp]).toarray()
        prediction = model.predict(inp_vector)
        tag = label_encoder.inverse_transform(prediction)[0]
        response = random.choice(responses[tag])
        output_field.insert(tk.END, "Bot: " + response + "\n")
        input_field.delete("1.0", tk.END)

    root = tk.Tk()
    root.title("Chatbot")

    input_field = scrolledtext.ScrolledText(root, width=50, height=10)
    input_field.pack(padx=10, pady=10)

    send_button = tk.Button(root, text="Send", command=send)
    send_button.pack(padx=10, pady=10)

    output_field = scrolledtext.ScrolledText(root, width=50, height=10)
    output_field.pack(padx=10, pady=10)

    root.mainloop()

# Start the GUI chat
gui_chat()