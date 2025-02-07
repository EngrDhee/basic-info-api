import sys
from datetime import datetime, timezone, timedelta
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from fastapi.testclient import TestClient

# Ensure the 'ssl' module is available
if "ssl" not in sys.modules:
    raise ImportError("The 'ssl' module is required but not available in this environment.")

# Create FastAPI instance
app = FastAPI()

# Enable CORS to allow cross-origin requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"]  # Allow all headers
)

@app.get("/", summary="Retrieve basic public information", response_model=dict)
def get_info():
    """
    Retrieves and returns basic public information in JSON format.

    **Response Fields:**
    - `registered_email` (str): Predefined registered email address.
    - `current_datetime` (str): Current date and time in Nigeria (ISO 8601 format).
    - `github_url` (str): URL to the project's GitHub repository.
    
    **Returns:**
        dict: A dictionary containing the email, current datetime, and GitHub URL.
    """
    # Set timezone to Nigeria (UTC+1)
    nigeria_tz = timezone(timedelta(hours=1))
    current_datetime = datetime.now(nigeria_tz).isoformat()
    
    return {
        "registered_email": "talk2dayoabdul@yahoo.com",  # Static email
        "current_datetime": current_datetime,  # Dynamically generated Nigeria time
        "github_url": "https://github.com/EngrDhee/basic-info-api"  # GitHub repository link
    }
