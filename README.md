# Diabetes Prediction API

## Overview

This project implements a **FastAPI-based API** for predicting diabetes progression using a **RandomForestRegressor** trained on the [scikit-learn diabetes dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html).

The API provides:
- `GET /` → Health check endpoint.
- `POST /predict` → Accepts JSON input with 10 features and returns a predicted diabetes progression value.

The project includes:
- `train_model.py` → Script to train and save the model.
- `main.py` → FastAPI application.
- `requirements.txt` → Pinned dependencies.
- `Dockerfile` → Containerization of the API.

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/baileyam99/CSCI-632-Fast-API-And-Docker.git
cd {path-to-CSCI-632-Fast-API-And-Docker}
```

### 2. Create a Python environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# .\venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model
```bash
python3 app/train_model.py
```
This will create `app/models/diabetes_rf_model.joblib`.

---

## Running the API

### 1. Locally (Python)
```bash
uvicorn app.main:app --reload --port 8000
```
Access the API at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2. Using Docker
1. Build the image:
```bash
docker build -t fastapi-diabetes-app .
```
2. Run the container:
```bash
docker run -d -p 8000:8000 fastapi-diabetes-app
```

---

## Example Request/Response

### Valid Request
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [0.0381,0.0507,0.0617,0.0219,-0.0442,-0.0348,-0.0434,-0.0026,0.0199,-0.0176]}'
```

**Response:**
```json
{
  "prediction": 153.42
}
```

### Invalid Request (wrong feature length)
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [0.1,0.2]}'
```

**Response:**
```json
{
  "detail": [
    {
      "type": "too_short",
      "loc": ["body","features"],
      "msg": "List should have at least 10 items after validation",
      "input": [0.1,0.2]
    }
  ]
}
```

---

## Troubleshooting

- **Docker errors**:
    - `Cannot connect to the Docker daemon` → Ensure Docker Desktop is installed and running.
    - On macOS, open Docker Desktop and wait until it shows **Docker is running**.

- **Dependency issues**:
    - Make sure you use the pinned versions in `requirements.txt`.
    - For Python version issues, create a virtual environment using Python 3.11 or 3.14.

- **Model not found**:
    - Run `python app/train_model.py` first to create `app/models/diabetes_rf_model.joblib`.

- **Port conflicts**:
    - If port 8000 is already in use, change the port:
      ```bash
      uvicorn app.main:app --reload --port 8080
      ```
