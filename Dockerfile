FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN  apt-get -y update
RUN  apt-get install -y sqlite3 libsqlite3-dev
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py migrate
CMD python manage.py runserver 
