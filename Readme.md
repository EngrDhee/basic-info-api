# Public API for Basic Information

This is a FastAPI-based public API that returns basic information in JSON format, including a registered email address, the current UTC datetime in ISO 8601 format, and a link to the GitHub repository.

## Features

* Returns a registered email address
* Provides the current datetime dynamically in ISO 8601 format
* Includes a link to the GitHub repository
* Supports Cross-Origin Resource Sharing (CORS)

## Installation & Setup

### Prerequisites

* Python 3.8+
* pip (Python package manager)

### Installation Steps

1. **Clone this repository:**

   ```bash
   git clone [https://github.com/EngrDhee/basic-info-api.git](https://github.com/EngrDhee/basic-info-api.git)
   cd basic-info-api
Create and activate a virtual environment:

Bash

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

Bash

pip install -r requirements.txt
Run the API:

Bash

uvicorn main:app --reload
API Documentation
Endpoint: GET /

Response Format (200 OK)

JSON

{
    "registered_email": "talk2dayoabdul@yahoo.com",
    "current_datetime": "2025-02-06T12:34:56.789Z",
    "github_url": "[https://github.com/EngrDhee/basic-info-api](https://github.com/EngrDhee/basic-info-api)"
}
Deployment
Deploying on Railway
Go to Railway.app and sign up using GitHub.

Click "New Project" → Select "Deploy from GitHub Repo".

Choose your repository and let Railway detect the environment.

Add a Procfile with the following content:

web: uvicorn info_api:app --host 0.0.0.0 --port $PORT
Click "Deploy" and wait for completion.

Once deployed, Railway will provide a public URL like:

https://your-app-name.up.railway.app/

Test your API using:

Bash

curl [https://your-app-name.up.railway.app/](https://your-app-name.up.railway.app/)
License
This project is licensed under the MIT License.
