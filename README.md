# exchange-service

Test project of a web service using only standard http library


~~~
curl -s 'http://127.0.0.1:8080/?from=USD&to=RUB&amount=100'
~~~

~~~
curl -s -d '{"from":"USD","to":"RUB","amount":100}' 'http://127.0.0.1:8080/'
~~~

Testing:
~~~
python -m  unittest tests\test_exchange.py
~~~