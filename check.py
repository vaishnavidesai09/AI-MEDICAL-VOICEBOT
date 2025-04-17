from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Print to check if the variables are loaded
print(os.getenv("GROQ_API_KEY"))  # This should print your API key if loaded correctly
print(os.getenv("ELEVENLABS_API_KEY"))
