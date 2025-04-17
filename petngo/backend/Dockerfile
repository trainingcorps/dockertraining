FROM python:3.9-slim as petback

WORKDIR /app/petback

ADD test.tar.gz /opt/

COPY . /app/petback  

RUN pip install -r requirements.txt 


EXPOSE 8000 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


