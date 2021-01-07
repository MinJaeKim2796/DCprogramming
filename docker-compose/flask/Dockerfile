FROM python:latest
MAINTAINER minj2796 "kmj5596@khu.ac.kr"
WORKDIR /app
ADD . /app
RUN apt-get update
RUN pip install -r requirements.txt
RUN echo "CONNECTED TIME TEST"
CMD ["uwsgi", "uwsgi.ini"]