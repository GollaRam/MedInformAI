import cv2
import pytesseract
import spacy
import re

nlp = spacy.load("en_core_web_sm")
def preprocess_and_ocr(file_path):
    if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValueError("Unsupported file format. Please provide an image file.")

    image = cv2.imread(file_path)
    if image is None:
        raise ValueError("Unable to read the file. Please check the path and try again.")

    raw_text = pytesseract.image_to_string(image)

    lines = raw_text.splitlines()
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        line = re.sub(r'[ \t]+', ' ', line)
        doc = nlp(line)
        has_content = any(token.pos_ in ("NOUN", "PROPN", "NUM") for token in doc)
        if not has_content:
            continue

        cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines)
    return cleaned_text
