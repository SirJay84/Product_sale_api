FROM python:3.9 

WORKDIR /app 

COPY . ./ 

EXPOSE 8000

RUN python3 -m pip install --upgrade pip
RUN pip install fastapi SQLAlchemy
RUN pip install -r requirements.txt
RUN pip install uvicorn 

 

CMD ["uvicorn", "app.main:app","--host=0.0.0.0","--reload"]