FROM python:latest
MAINTAINER khu_swcon "kmj5596@khu.ac.kr"
WORKDIR /app
COPY . /app
RUN apt-get update
RUN pip install -r requirements.txt
RUN echo "HTTP RESPONSE TEST"
CMD ["python", "/app/response.py"]
