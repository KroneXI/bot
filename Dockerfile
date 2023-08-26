FROM python:latest

WORKDIR /app

COPY . .
# ПЕРВАЯ точка путь в моем пк, ВТОРАЯ - путь WORKDIR
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py"]