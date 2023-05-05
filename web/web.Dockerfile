FROM python:3.10-alpine
RUN mkdir /app
COPY ["*.py", "requirements.txt", "static", "templates", "app/"]
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 10000
ENV AUTH_URL=http://localhost:9000
CMD ["gunicorn", "wsgi:app", "--bind=0.0.0.0"]