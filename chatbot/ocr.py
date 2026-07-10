import cv2
import pytesseract
import spacy
import re

def preprocess_and_ocr(file_path):
    """Preprocess the file and perform OCR, then lightly clean the text."""
    if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValueError("Unsupported file format. Please provide an image file.")

    image = cv2.imread(file_path)
    if image is None:
        raise ValueError("Unable to read the file. Please check the path and try again.")

    raw_text = pytesseract.image_to_string(image)

    # Light cleanup only — do NOT strip numbers/units/stopwords, reports need them
    lines = raw_text.splitlines()
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # collapse multiple spaces/tabs from OCR spacing artifacts
        line = re.sub(r'[ \t]+', ' ', line)
        # drop lines that are pure OCR noise (no letters or digits at all)
        if not re.search(r'[A-Za-z0-9]', line):
            continue
        cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines)
    print(cleaned_text)
    return cleaned_text
