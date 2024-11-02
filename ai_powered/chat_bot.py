import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow as tf
import random
import json

# Initialize the stemmer
stemmer = LancasterStemmer()

# Load intents from JSON file
with open("intents.json") as file:
    data = json.load(file)

# Prepare the data
words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

# Stem and sort words
words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

# Sort labels
labels = sorted(labels)

# Prepare training data
training = []
output = []
out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []
    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)

# Reset TensorFlow graph
tf.compat.v1.reset_default_graph()

# Build the model
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

# Create and train the model
model = tflearn.DNN(net)
model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")

# Function to create the bag of words
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

# Function for chatting
def chat():
    print("Start talking with the bot (type quit to stop)!")

    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        print(random.choice(responses))

# Function for GUI chat
def gui_chat():
    def send():
        inp = input_field.get("1.0", "end-1c")
        output_field.insert(tk.END, "You: " + inp + "\n")
        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        output_field.insert(tk.END, "Bot: " + random.choice(responses) + "\n")
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