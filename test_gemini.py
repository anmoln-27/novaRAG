import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found in .env")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)

print("===================================")
print("Testing Gemini API Connection...")
print("===================================")

try:
    response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents="Say OK"
    )

    print("\n✅ Gemini API Connection Successful!")
    print("\nResponse:")
    print(response.text)

except Exception as e:
    print("\n❌ Gemini API Connection Failed")
    print("\nError:")
    print(e)