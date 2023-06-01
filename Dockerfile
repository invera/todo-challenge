FROM python:3.11-bullseye
ENV PYTHONUNBUFFERED 1
WORKDIR /backend
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ADD . /backend/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]