FROM python:3.10-slim-buster
WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN apt update && \
    apt -y upgrade && \
    apt install -y ffmpeg && \
    pip3 install --upgrade pip && \
    pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

EXPOSE 8501

COPY . /app
COPY streamlit/secrets.toml /app/.streamlit/secrets.toml

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]