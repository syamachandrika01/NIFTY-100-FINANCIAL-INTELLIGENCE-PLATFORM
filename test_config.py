from dotenv import load_dotenv
import os

load_dotenv()

print("Project:", os.getenv("PROJECT_NAME"))
print("Environment:", os.getenv("ENVIRONMENT"))
print("Database:", os.getenv("DATABASE_NAME"))
print("Raw data:", os.getenv("RAW_DATA_DIR"))