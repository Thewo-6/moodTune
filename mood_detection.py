from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


tokenizer = AutoTokenizer.from_pretrained("IsmaelMousa/bert-finetuned-emotion")
model = AutoModelForSequenceClassification.from_pretrained("IsmaelMousa/bert-finetuned-emotion")

def get_emotion(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    predicted_class = torch.argmax(outputs.logits, dim=1)
    return model.config.id2label[predicted_class.item()]

print(get_emotion("I'm feeling hardworker today"))