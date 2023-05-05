FROM python:3.10-alpine
RUN mkdir /app
COPY ["*.py", "requirements.txt", "app/"]
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "wsgi:app", "--bind=0.0.0.0"]