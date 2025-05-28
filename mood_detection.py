# mood_detection.py
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained("IsmaelMousa/bert-finetuned-emotion")
model = AutoModelForSequenceClassification.from_pretrained("IsmaelMousa/bert-finetuned-emotion")

def detect_emotion(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    predicted_class = torch.argmax(outputs.logits, dim=1)
    return model.config.id2label[predicted_class.item()]

# Optional test
if __name__ == "__main__":
    print(detect_emotion("I'm feeling hardworking today"))