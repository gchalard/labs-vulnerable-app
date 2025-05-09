FROM python:3.10-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential \
    libpq-dev --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY . /app/

RUN uv sync --locked

CMD ["uv", "run", "app.py", "--host", "0.0.0.0"]