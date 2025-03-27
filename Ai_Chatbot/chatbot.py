import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="The NCRP Chatbot will assist users in filing cybercrime reports by guiding them step-by-step and using NLP to map their inputs to relevant cybercrime categories and laws. It will explain cyber laws in simple terms, answer FAQs about reporting procedures and required documents, and auto-suggest details to minimize errors. The chatbot will ensure accessibility, possibly supporting multiple languages, and provide real-time assistance with the NCRP Portal. It will maintain user privacy by not storing any data and will offer direct links to official resources. The goal is to streamline the reporting process, educate users, and enhance cybercrime awareness.",
    tools=["code_execution"],  
)

history = []
chat_session = model.start_chat(history=history) 

print("Bot: How can I help you?")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit","Thanks For help"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    response = chat_session.send_message(user_input)
    model_response = response.text

    print(f"Bot: {model_response}\n")

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
