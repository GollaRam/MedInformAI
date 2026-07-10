from chatbot.ocr import preprocess_and_ocr
from chatbot.chatbot import chatbot_interaction
def submit_blood_report(context, name, age, sex, height, weight):
    """Handle the blood report submission process."""
    file_path = input("Upload your blood report (image): ")
    try:
        # Process OCR and get normalized text
        normalized_text = preprocess_and_ocr(file_path)
        report_text = f"The report contains the parameter: .\n{normalized_text}"

        print("Blood report submitted successfully.")
        context += "\nUser: Submitted a blood report."

        # Get additional user information
        user_questions = [
            "Do you have any specific symptoms you would like to mention?",
            "Do you have any known medical conditions (e.g., diabetes, hypertension)?",
            "Are you currently taking any medications?",
            "Have you experienced fatigue, dizziness, or any other symptoms recently?",
            "Do you smoke or consume alcohol? If yes, how frequently?",
            "What kind of diet do you typically follow (e.g., vegetarian, non-vegetarian)?",
            "How often do you exercise in a week?"
        ]

        for question in user_questions:
            user_response = input(f"\n{question} ").strip()
            if user_response.lower() == 'exit':
                print("Namaste, take care!")
                return context
            if user_response:
                context += f"\nUser: {user_response}\nAI: *"

        # Chatbot interaction
        question = "Please provide full dietary recommendations,check for any chronic diseases and lifestyle recommendations."
        chatbot_output = chatbot_interaction(name, age, sex, height, weight, report_text, question, context)
        print("Bot:", chatbot_output)

        context += f"\nAI: {chatbot_output}"

    except Exception as e:
        print(f"Error processing report: {e}")

    return context