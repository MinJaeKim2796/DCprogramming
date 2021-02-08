FROM python:3.7.5-slim
MAINTAINER minj2796 "kmj5596@khu.ac.kr"
RUN pip install flask==1.1.1
WORKDIR /app
ADD . /app
ENV FLASK_APP app.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]