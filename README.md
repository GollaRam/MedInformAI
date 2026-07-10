# MedInformAI

**MedInformAI** is a generative AI–powered medical report interpretation and health advisory system. It analyzes uploaded medical reports, extracts key diagnostic parameters via optical character recognition, and delivers personalized dietary, lifestyle, and health recommendations through a conversational interface  designed to support users in regions where access to medical professionals is limited.

---
## Overview

A significant portion of the population struggles to interpret medical reports on their own  a challenge that is amplified in rural and remote areas, where access to medical professionals is scarce and general digital literacy is often limited. **MedInformAI** addresses this gap by using generative AI to translate diagnostic reports into clear, actionable health guidance, without requiring the user to have any medical background.

The system takes a scanned or photographed medical report as input, extracts and interprets the relevant diagnostic parameters, and produces a natural-language summary covering detected anomalies, dietary recommendations, lifestyle adjustments, and possible chronic-disease risk factors. A built-in conversational assistant allows users to ask follow-up questions in plain language and receive contextual, personalized responses grounded in their own report and profile.

MedInformAI is intended to function as a first line of support helping individuals make sense of their health data at the point of need, easing the burden on healthcare professionals for routine interpretive tasks, and acting as a supplementary reference tool for nursing and clinical support staff in resource-constrained settings. It is not a diagnostic replacement for a licensed physician, but a bridge that makes medical information more accessible and actionable for the people who need it most.

The system integrates **Ollama**, **OpenCV**, **Tesseract OCR**, **spaCy**, **LangChain**, and **Meta's LLaMA 3** (served locally via Ollama) to convert scanned medical reports into structured, natural-language health insights end to end — from image upload to personalized recommendation.

---
## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Example Session](#example-session)
- [Use Cases](#use-cases)
- [Disclaimer](#disclaimer)


---

## Features

| Capability | Description |
|---|---|
| **Medical Report Analysis** | Upload a report image and receive an automated interpretation, including detection of anomalies against reference ranges. |
| **Personalized Recommendations** | Diet, lifestyle, and chronic-disease-risk guidance tailored to the user's profile (name, age, sex, height, weight). |
| **Conversational Chat Support** | General health-related queries answered with contextual, LLM-generated responses. |
| **Customer Care** | Direct access to support contact information. |
| **Context-Aware Sessions** | User profile and conversation history are retained throughout the session to inform subsequent responses. |

---

## System Architecture

MedInformAI follows a five-stage pipeline, from raw image input to natural-language health guidance:

1. **Image Preprocessing & OCR** — The uploaded report image is processed with OpenCV and passed through Tesseract OCR to extract raw text.
2. **Text Normalization** — Extracted text is cleaned to remove OCR artifacts while preserving numeric values and units critical to medical interpretation.
3. **NLP Processing** — spaCy performs tokenization and entity recognition to prepare the text for downstream analysis.
4. **LLM Reasoning** — LangChain orchestrates the flow, combining the normalized report, patient profile, and conversation history as input to LLaMA 3 (via Ollama) to generate insights and recommendations.
5. **Response Delivery** — The system presents dietary guidance, identified anomalies, and risk observations in plain, accessible language, and remains available for follow-up questions.

---

## Project Structure

```
project/
├── app.py                     # Entry point — launches the application
└── chatbot/
    ├── conversation.py        # Main conversation flow and menu handling
    ├── chat.py                # Free-form chat mode
    ├── chatbot.py              # Core LLM interaction logic (LangChain + Ollama)
    ├── report.py                # Report submission and analysis flow
    ├── ocr.py                    # Image preprocessing and OCR text extraction
    └── customer_care.py     # Customer support information
```

---

## Prerequisites

The following components must be installed and configured before running the application.

### 1. Ollama (required)

MedInformAI runs LLaMA 3 locally via **Ollama**. Ollama must be installed and the model must be available **before launching the application**.

- Install Ollama from [https://ollama.com](https://ollama.com)
- Pull the LLaMA 3 model:
  ```bash
  ollama pull llama3
  ```
- Confirm the Ollama service is running in the background prior to starting MedInformAI.

### 2. Tesseract OCR

Tesseract must be installed at the operating-system level (the Python package alone is not sufficient):

| Platform | Command |
|---|---|
| Windows | Install via the [Tesseract installer](https://github.com/UB-Mannheim/tesseract/wiki) |
| macOS | `brew install tesseract` |
| Linux (Debian/Ubuntu) | `sudo apt install tesseract-ocr` |

### 3. Python Dependencies

```bash
pip install opencv-python pytesseract spacy scikit-learn langchain-ollama langchain-core
```

### 4. spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```


## Usage

With Ollama running and all dependencies installed, launch the application:

```bash
python app.py
```

The application will prompt for basic profile details (name, age, sex, height, weight), followed by a menu of three options:

1. **Submit Blood Report** — Upload a report image for automated analysis and personalized recommendations.
2. **Chat** — Ask general health-related questions.
3. **Customer Care** — View support contact information.

Enter `exit` at any prompt to end the session.

---

## Example Session

```
Namaste! Welcome to the AI chatbot! Please type 'exit' to quit anytime.
Please enter your name: xyz
Please enter your age: 21
Please enter your sex (M/F): M
Please enter your height in cm: 165
Please enter your weight in kg: 70

Choose an option:
1) Submit Blood Report
2) Chat
3) Customer Care
Enter your choice (1/2/3): 1
Upload your blood report (image): path/to/report.jpg
Blood report submitted successfully.
...
Bot: Based on the patient information and conversation history, here are some observations
and recommendations...
```

---

## Use Cases

- **Patient self-interpretation** — Enables individuals in rural or underserved areas to understand medical reports without immediate access to a physician.
- **Clinical support tool** — Serves as a supplementary reference for nursing staff and healthcare support teams.
- **Workload reduction** — Handles routine, non-critical inquiries, allowing medical professionals to focus on cases requiring direct clinical attention.

---

## Disclaimer

MedInformAI is designed to support not replace  professional medical advice. Recommendations generated by the system should not be treated as a substitute for consultation with a qualified healthcare provider.

---
