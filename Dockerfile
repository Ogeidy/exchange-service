FROM python:3

WORKDIR /usr/src/app

COPY . .

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["-m", "exchange_service"]