FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /annserver
WORKDIR /annserver
COPY requirements.txt /annserver/
RUN pip install -r requirements.txt
COPY . /annserver/
RUN chmod +x /annserver/docker-entrypoint.sh