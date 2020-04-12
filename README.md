# exchange-service

Test project of a web service using only standard http library


## Deploy
~~~bash
docker-compose up
~~~

## How to use exchange service

### Using GET request

From USD to RUB:
~~~bash
$ curl -s 'http://127.0.0.1:8080/?from=USD&to=RUB&amount=100'
{"currency": "RUB", "amount": 7375.15}
~~~
From RUB to USD
~~~bash
$ curl -s 'http://127.0.0.1:8080/?from=RUB&to=USD&amount=100'
{"currency": "USD", "amount": 1.36}
~~~

### Using POST request
From USD to RUB:
~~~bash
$ curl -s -d '{"from":"USD","to":"RUB","amount":100}' 'http://127.0.0.1:8080/'
{"currency": "RUB", "amount": 7375.15}
~~~
From RUB to USD
~~~bash
$ curl -s -d '{"from":"RUB","to":"USD","amount":100}' 'http://127.0.0.1:8080/'
{"currency": "USD", "amount": 1.36}
~~~

## Testing
~~~bash
python -m  unittest tests\test_exchange.py
~~~