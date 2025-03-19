from dotenv import load_dotenv
import os

load_dotenv()

RAPID_URL = os.environ.get("RAPID_URL")
RAPID_HOST = os.environ.get("RAPID_HOST")
API_KEY = os.environ.get("API_KEY")
