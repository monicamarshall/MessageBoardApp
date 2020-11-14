# pull official base image
FROM python:3.7

# set work directory
WORKDIR .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY requirements.txt .

#install dependencies
RUN pip install -r requirements.txt

# Copy project
COPY . .

