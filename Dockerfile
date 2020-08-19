FROM python:3

COPY app/ /app/
WORKDIR /app
RUN apt-get -y update && apt-get -y install dos2unix && find /app -type f -print0 | xargs -0 dos2unix && pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT python -u app.py