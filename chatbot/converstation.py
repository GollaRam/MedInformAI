from chatbot.chat import chat_mode
from chatbot.report import submit_blood_report
from chatbot.customer_care import customer_care
def handle_conversation():
    """Main function to handle the conversation flow."""
    print("Namaste! Welcome to the AI chatbot! Please type 'exit' to quit anytime.")
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    sex = input("Please enter your sex (M/F): ")
    height = input("Please enter your height in cm: ")
    weight = input("Please enter your weight in kg: ")

    context = f"Patient: {name}, Age: {age}, Sex: {sex}, Height: {height}, Weight: {weight}"
    
    while True:
        print("\nChoose an option:")
        print("1) Submit Blood Report")
        print("2) Chat")
        print("3) Customer Care")

        choice = input("Enter your choice (1/2/3): ").strip()
        if choice.lower() == 'exit':
            print("Namaste, take care!")
            break

        if choice == '1':
            context = submit_blood_report(context, name, age, sex, height, weight)
        elif choice == '2':
            context = chat_mode(context, name, age, sex, height, weight)
        elif choice == '3':
            customer_care()
        else:
            print("Invalid choice. Please try again.")