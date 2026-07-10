import cv2
import pytesseract
import spacy
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Load Spacy model for NLP
nlp = spacy.load("en_core_web_sm")

# Chatbot model setup
template = """
Answer the following question based on the information provided.
Patient Information: Name: {name}, Age: {age}, Sex: {sex}, Height: {height}, Weight: {weight}

Be advised a professional doctor, physician, dietitian is looking after you, so be confident in whatever you generate. Give the answers accurately, completely, and smoothly without any errors. Be gentle with patients and always assure them as a great good and perfect doctor would do. Please answer only the questions related to this domain.
i want the anomolaies too along
Report Analysis: {report_text}

Conversation History: {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def chatbot_interaction(name, age, sex, height, weight, report_text, question, context):
    """Interact with the chatbot to get responses."""
    result = chain.invoke({
        "name": name,
        "age": age,
        "sex": sex,
        "height": height,
        "weight": weight,
        "report_text": report_text,
        "question": question,
        "context": context
    })
    return result