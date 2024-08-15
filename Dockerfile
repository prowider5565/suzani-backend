FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# Copy requirements file and install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Copy the rest of the application code
COPY . /code/

# Expose port
EXPOSE 8000
