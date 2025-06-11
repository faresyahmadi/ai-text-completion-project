import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv() 
api_key = os.getenv("GEMINI_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

generation_config = {
    "temperature": 0.8,    
    "top_p": 0.9,          
    "max_output_tokens": 100
}

def generate_response(prompt):
    try:

        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"


print("***** Gemini Text Completion App *****")
print("Type 'exit' to quit.")
    
while True:
    prompt = input("\nEnter your prompt: ").strip()
    if prompt.lower() == "exit":
        print("Goodbye!")
        break
    if not prompt:
        print("Prompt cannot be empty. Try again.")
        continue

    result = generate_response(prompt)
    print("\nGemini's Response:\n" + result)

