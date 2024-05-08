FROM python:3.10

WORKDIR /app

COPY . /app


RUN pip install PyPDF2

RUN pip install spacy && \
    python -m spacy download en_core_web_sm

CMD ["python", "main.py"]