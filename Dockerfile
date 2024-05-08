FROM python:3.10

WORKDIR /app

COPY . /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN pip install spacy && \
    python -m spacy download en_core_web_sm

CMD ["python", "main.py"]