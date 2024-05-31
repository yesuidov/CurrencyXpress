# Currency Converter App
A Flask application that converts a user's value in USD to the equivalent value in a specified target currency using real-time exchange rate data fetched from the ExchangeRate-API

## Running Instruction

**Running locally**
```
python main.py
HOSTURL/convert-currency/[PRICE]/[TARGET_CURRENCY]
```

**Running though Docker**
```
docker buld -t myflaskapp.
docker run -p 5000:5000 myflaskapp
docker stop [docker_id]
```
docker_id can be found by calling docker ps