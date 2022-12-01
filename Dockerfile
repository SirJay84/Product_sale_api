FROM python:3.9

WORKDIR /app

COPY . /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn app.main:app --reload --host 0.0.0.0 --port 8000