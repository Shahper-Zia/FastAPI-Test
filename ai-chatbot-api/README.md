# README.md

# AI-Powered Q&A Chatbot API 🤖💬

## Overview
This project is an AI-Powered Q&A Chatbot API built using FastAPI. It allows users to send questions and receive responses powered by the Gemini LLM.

## Features
- **User Query Handling**: Accepts questions via FastAPI endpoints.
- **LLM Integration**: Sends queries to the Gemini API and retrieves responses.
- **Pydantic Models**: Validates input/output data.
- **Rate Limiting & Caching**: Prevents excessive API calls using Redis.
- **Basic Auth**: Implements JWT authentication for security.
- **Logging & Monitoring**: Stores user queries and responses in a database (SQLite/PostgreSQL).

## Tech Stack
- **FastAPI**: API framework
- **Pydantic**: Data validation
- **Gemini API**: LLM processing
- **Redis**: Caching responses
- **SQLite/PostgreSQL**: Data storage
- **Docker**: Containerization

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-chatbot-api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables in the `.env` file.

5. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

## Testing
To run the tests, use:
```
pytest tests/
```

## Docker
To build and run the application using Docker:
```
docker-compose up --build
```

## License
This project is licensed under the MIT License.