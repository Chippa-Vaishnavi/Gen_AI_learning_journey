import os
from dotenv import load_dotenv
from google import genai
#Load .env
load_dotenv(dotenv_path="env/.env")
# Get API key

api_key = os.getenv("GEMINI_API_KEY")

#print("Loaded key:", api_key)  # Debug check

#create client
client=genai.Client(
    api_key=os.getenv("GEMINI API KEY")
)
#user prompt
user_prompt = input("Enter your prompt: ")

#Generate response
response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_prompt

)
print(response.text)