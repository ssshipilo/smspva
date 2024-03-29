![SMSPVA service](https://github.com/ssshipilo/smspva/blob/main/image.png?raw=true)

## SMSPVA API (Activations)

I needed this site for my project, so I give you a simple code to interact with [SMSPVA service](https://smspva.com/).

Important! In this code, there is only interaction with the Activations API, no Rent API but in fact if you are an experienced developer you can use the server class method __requests__() to make requests to their site without writing your own API. By calling smspva.__requests__(endpoint, headers_array, method)

### Installation: 
```python
git clone https://github.com/ssshipilo/smspva.git
```

### Beginning of interaction 
Get an API token to interact on the page https://smspva.com/user/{your_username}/

##### Code: 
```python
from smspva.api import SMSPVActivator

if __name__ == "__main__":
    smspva = SMSPVActivator("<YOU-API-TOKEN>")
```

### Basic methods: 
#### Balance
```python
result = smspva.get_balance()
print(result)
```

#### Get number
```python
result = smspva.get_number(country="TZ", service="opt1")
print(result)
```

#### Users info
```python
result = smspva.get_users_info()
print(result)
```

#### Get all prices
```python
result = smspva.get_all_prices()
print(result)
```

#### Get service prices
```python
resut = smspva.get_prices_service("opt219", filter="lower")
print(result)
```

#### Get orders
```python
resut = smspva.get_orders()
print(result)
```

#### Get all countries
```python
resut = smspva.get_all_countries()
print(result)
```

#### Get all services
```python
resut = smspva.get_all_services()
print(result)
```

#### Get available numbers
```python
resut = smspva.get_available_numbers(country="SI")
print(result)
```

