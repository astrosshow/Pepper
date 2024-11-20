from pep_openai_model import get_response
from speech_to_text import listen
from text_to_speech import speak

def chat():
    print("Hello! I am Pepper, your personal assistant. How can I help you today?")
    while True: 
        print("Listening for user input...")
        user_input = listen()
        if not user_input:
            print("No input detected. Please try again.")
            continue
        if user_input.lower() in ["exit", "quit", "goodbye"]:
            print("Goodbye!")
            speak("Goodbye!")
            break
        print(f"User input: {user_input}")
        response = get_response(user_input)
        print(f"Pepper: {response}")
        speak(response)

if __name__ == "__main__":
    print("Starting the chatbot...")
    chat()