# stage-1-backend
*HNG 12 backend track stage-1*

A publicly accessible API that can take a number as its query parameter and returns interesting mathematical properties about it.

It makes use of [number api](http://numbersapi.com/) internally.

## Local Setup
1. Clone the Repository

        git clone https://github.com/Ayo-Oni-515/stage-1-backend.git

2. Install Dependencies

    Dependencies are available in requirements.txt

    To install dependencies locally

        pip install -r requirements.txt

3. Test locally by using this command then click on the localhst link provided in the terminal.

        uvicorn main:app --reload

# API Documentation
To access online, use endpoint URL:

    https://stage-1-backend-euok.onrender.com/api/classify-number?number=<integer_value>

Remeber to specify an actual integer value.

Typical JSON Response Format (200 OK):

    {
        "number": 371,
        "is_prime": false,
        "is_perfect": false,
        "properties": ["armstrong", "odd"],
        "digit_sum": 11,  // sum of its digits
        "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
    }

Typical JSON Response Format (400 Bad Request):

    {
        "number": "alphabet",
        "error": true
    }

Usage

    import requests

    response = requests.get("https://stage-1-backend-euok.onrender.com/api/classify-number?number=371")
    print(response.json())