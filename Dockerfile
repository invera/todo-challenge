FROM python:3.10.8-alpine3.16

EXPOSE 8000

# Copy inside the /app directory
COPY . /app
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
