FROM python:3.10

RUN mkdir -p /home/app

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]