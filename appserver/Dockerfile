FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /appserver
WORKDIR /appserver
COPY requirements.txt /appserver/
RUN pip install -r requirements.txt
COPY . /appserver/
RUN chmod +x /appserver/docker-entrypoint.sh
EXPOSE 80
STOPSIGNAL SIGTERM
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait
CMD /wait
ENTRYPOINT ["/appserver/docker-entrypoint.sh"]