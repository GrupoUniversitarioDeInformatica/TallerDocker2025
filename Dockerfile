FROM python:3.11

WORKDIR /app

ENV MAIN="main"

COPY README.md /app/README.md
COPY pyproject.toml /app/pyproject.toml
COPY uv.lock /app/uv.lock
COPY src/  /app/src/

RUN pip install uv
RUN uv sync

CMD uv run uvicorn src.${MAIN}:app --host 0.0.0.0 --port 8000
