FROM python:3.9-slim

RUN mkdir /code

WORKDIR /code

COPY req.txt .

RUN pip install -r req.txt

COPY . .

# CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]