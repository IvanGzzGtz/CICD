FROM python:3.11.0rc1

ENV SECRET_KEY=django-insecure-z&kqdv)@l2q8afv2amkndg0o%(bm&62y_3p)#r!sykr*isdsk6
ENV DEBUG=True
ENV ALLOWED_HOSTS=.correkaminos.com
ENV EMAIL_HOST_USER=info@correkaminos.com
ENV EMAIL_HOST_PASSWORD=32@EdfvXivcYc^

WORKDIR /correkaminos
COPY ./requirements.txt ./

RUN apt-get update && \
    apt-get install -y \
      gcc \
      pkg-config \
      curl && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y \
      gcc \
      pkg-config && \
    rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000
