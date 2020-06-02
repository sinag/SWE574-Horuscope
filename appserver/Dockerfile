FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /appserver
WORKDIR /appserver
COPY requirements.txt /appserver/
RUN pip install -r requirements.txt
COPY . /appserver/
RUN chmod +x /appserver/docker-entrypoint.sh
EXPOSE 80
STOPSIGNAL SIGTERM
ENTRYPOINT ["/appserver/docker-entrypoint.sh"]