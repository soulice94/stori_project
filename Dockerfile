FROM python:latest as base
WORKDIR /usr/src/app
COPY . .
CMD ["python", "main.py"]
