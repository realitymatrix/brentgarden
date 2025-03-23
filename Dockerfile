FROM python:3.12.7-bullseye

WORKDIR /brentgarden

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD python ./app.py