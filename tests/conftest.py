import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# Access the API token globally
API_TOKEN = os.getenv("API_TOKEN")
