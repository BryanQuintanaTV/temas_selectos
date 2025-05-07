import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
# from train import input_size, hidden_size, output_size
import nltk
nltk.download("punkt")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open("./dataset/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Bot"
print("Hola, estoy para ayudarte con cualquier duda sobre el tec")

# Función principal para obtener respuesta
def get_response(sentence):
    # Tokenizar y procesar entrada
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    # Obtener salida del modelo
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    # Probabilidad de la predicción
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    # Retornar respuesta
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                return random.choice(intent["responses"])

    return "No entiendo tu pregunta..."

# while True:
#     sentence = input("Tu: ")
#     if sentence == "quit":
#         break
#
#     sentence = tokenize(sentence)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)
#
#     output = model(X)
#     _, predicted = torch.max(output, dim=1)
#     tag = tags[predicted.cpu().item()]
#
#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#
#     if prob.item() > 0.75:
#         for intent in intents["intents"]:
#             if tag == intent["tag"]:
#                 print(f"{bot_name}: {random.choice(intent['responses'])}")
#     else:
#         print(f"{bot_name}: No entiendo tu pregunta...")
