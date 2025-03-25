FROM python:3.12.7-bullseye

WORKDIR /brentgarden

COPY requirements.txt requirements.txt

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
EXPOSE 443

CMD ["python", "./app.py"]