FROM tiangolo/uwsgi-nginx:python3.11
WORKDIR /app
ADD . /app
# Install Python dependencies
RUN pip install -r requirements.txt
# Upgrade pip
RUN pip install --upgrade pip
# Install the latest version of uWSGI
RUN pip install uwsgi
CMD ["uwsgi", "app.ini"]
