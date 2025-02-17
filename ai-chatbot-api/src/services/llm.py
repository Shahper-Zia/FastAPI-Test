def query_gemini_api(question: str) -> str:
    import requests
    import os

    # Get the Gemini API endpoint and key from environment variables
    gemini_api_url = os.getenv("GEMINI_API_URL")
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    headers = {
        "Authorization": f"Bearer {gemini_api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "question": question
    }

    response = requests.post(gemini_api_url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("answer", "No answer found.")
    else:
        return f"Error: {response.status_code} - {response.text}"


def process_user_query(query: str) -> str:
    # Here you can add any preprocessing logic if needed
    return query


def handle_query(query: str) -> str:
    processed_query = process_user_query(query)
    answer = query_gemini_api(processed_query)
    return answer