# Number Classification API

A simple FastAPI project that classifies numbers based on mathematical properties and provides fun facts.

## Features
- Check if a number is prime, perfect, Armstrong, odd, or even.
- Get a fun fact using the Numbers API.
- CORS enabled for cross-origin requests.

## Tech Stack
- **Backend:** FastAPI (Python)
- **Deployment:** Publicly accessible via the platform of choice

## API Endpoint

### Classify Number

- **URL:** `/api/classify-number`
- **Method:** `GET`
- **Query Parameter:** `number` (integer)

#### Example Request:

#### Successful Response (200 OK):
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error Response (400)
```json
{
    "number": "abc",
    "error": true
}
```
```bash
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api
```

```
pip install -r requirements.txt
```

```
uvicorn main:app --reload
```

