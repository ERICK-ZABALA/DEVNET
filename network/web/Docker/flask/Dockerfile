#FROM tiangolo/uwsgi-nginx-flask:python3.11-alpine3.18
FROM tiangolo/uwsgi-nginx:python3.11

ADD . /flask
WORKDIR /flask
#WORKDIR /App

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#COPY app.ini /app/app.ini
#WORKDIR /app

# Upgrade pip
#RUN pip install --upgrade pip
# Install the latest version of uWSGI
RUN pip install uwsgi
CMD ["uwsgi", "app.ini"]
