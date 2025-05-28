import requests

def validate_data(data):
    required_fields = [
        "UCID", "first_name", "last_name", "github_username",
        "discord_username", "favorite_cartoon", "favorite_language",
        "movie_or_game_or_book"
    ]
    for field in required_fields:
        if field not in data or not isinstance(data[field], str) or not data[field].strip():
            raise ValueError(f"Invalid or missing value for field: {field}")

def submit_student_info():
    url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"
    data = {
        "UCID": "ez48",
        "first_name": "Elias",
        "last_name": "Zakarrya",
        "github_username": "eliaszak",
        "discord_username": "elizak",
        "favorite_cartoon": "Batman: The Animated Series",
        "favorite_language": "Python",
        "movie_or_game_or_book": "MLB The Show"
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Validate data before sending
        validate_data(data)

        # Send POST request without timeout
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()

        print(f"Submission successful! Status code: {response.status_code}")
        print("Response text:", response.text)

    except ValueError as ve:
        print(f"Data validation error: {ve}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status code: {http_err.response.status_code}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    submit_student_info()

