FROM tiangolo/uwsgi-nginx-flask:python3.11-alpine3.18
RUN apk --update add bash vim
RUN mkdir /App
ENV STATIC_URL /static
ENV STATIC_PATH /TestApp/static
COPY ./requirements.txt /App/requirements.txt
WORKDIR /App
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
