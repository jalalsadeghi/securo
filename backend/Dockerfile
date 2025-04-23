FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY ./tests ./tests
COPY ./entrypoint.sh .

# ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["sh", "./entrypoint.sh"]
