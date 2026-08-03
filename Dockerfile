FROM python:3.10-slim

WORKDIR /app

# Install system dependency (FIX for libgomp error)
RUN apt-get update && apt-get install -y libgomp1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY lightgbm_model.pkl .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]