from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"] ,  # Allow all HTTP methods
    allow_headers=["*"]  # Allow all headers
)

@app.get("/")
def get_info():
    return {
        "registered_email": "talk2dayoabdul@yahoo.com",
        "current_datetime": datetime.utcnow().isoformat(),
        "github_url": "https://github.com/EngrDhee/basic-info-api"
    }

# Run the application using: uvicorn filename:app --reload
