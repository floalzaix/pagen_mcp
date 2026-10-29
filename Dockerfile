FROM python:3.13.1-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd --gid 2222 app && useradd --uid 2222 --gid 2222 --no-create-home app

RUN mkdir -p /app/data && chown app:app /app/data && chmod 700 /app/data

COPY . /app

USER app:app

EXPOSE 5055

CMD ["python", "main.py"]