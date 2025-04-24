FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

RUN find . -name "*.pyc" -delete

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]