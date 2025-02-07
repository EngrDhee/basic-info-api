# Public API for Basic Information

This is a FastAPI-based public API that provides basic information in JSON format. It includes a registered email address, the current Nigeria datetime in ISO 8601 format, and a link to the GitHub repository.

## Features

- Returns a registered email address
- Provides the current Nigeria datetime dynamically in ISO 8601 format
- Includes a link to the GitHub repository
- Supports Cross-Origin Resource Sharing (CORS)

## Installation & Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Clone this repository:**

   ```bash
   git clone https://github.com/EngrDhee/basic-info-api.git
   cd basic-info-api
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API locally:**

   ```bash
   uvicorn info_api:app --reload
   ```

## API Documentation

### Endpoint: `GET /`

#### Response Format (200 OK)

```json
{
    "registered_email": "talk2dayoabdul@yahoo.com",
    "current_datetime": "2025-02-06T12:34:56.789+01:00",
    "github_url": "https://github.com/EngrDhee/basic-info-api"
}
```

## Deployment

### Deploying on Railway

1. Go to [Railway.app](https://railway.app) and sign up using GitHub.
2. Click **"New Project"** → Select **"Deploy from GitHub Repo"**.
3. Choose your repository and let Railway detect the environment.
4. Add a `Procfile` with the following content:

   ```plaintext
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

5. Click **"Deploy"** and wait for completion.
6. Once deployed, Railway will provide a public URL like:

   ```
   https://engrdhee-infoapi.up.railway.app/
   ```

### Testing the API

You can test the API using `curl`:

```bash
curl https://engrdhee-infoapi.up.railway.app/
```

Or use a browser or tools like Postman to verify the response.

## License

This project is licensed under the MIT License.
