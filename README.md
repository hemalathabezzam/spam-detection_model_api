# Spam Detection API

## Objective
Detect spam messages using NLP and Machine Learning.

## Tech Stack
- FastAPI
- Scikit-learn
- TF-IDF
- Joblib

## Model Used
- Multinomial Naive Bayes

## Run API

```bash
uvicorn app:app --reload
```

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

## Sample Input

```json
{
  "message": "Win free iphone now"
}
```