FROM python:3.11

WORKDIR /app

COPY . .

ENV PYTHONPATH=/app

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose passlib[bcrypt]

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]