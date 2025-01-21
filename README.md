[YooKassaAPI](https://img.shields.io/badge/0.1.0-blue?style=flat&logo=pypi&label=pypi&labelColor=gray)](https://github.com/Lems0n)

# YooKassa API Library

YooKassa API Library is a Python package designed to simplify interaction with YooKassa's API. This library provides a convenient way to handle payments, refunds, and various operations by utilizing the comprehensive methods available in the YooKassa API.

Also there is both a synchronous and asynchronous variation

## Features

- Easy-to-use interface for YooKassa API.
- Supports payment creation, capture, and cancellation.

## Installation

To install the library, use pip:

```bash
pip install yookassa_api
```

Or you can install it by Poetry:

```bash
poetry add yookassa_api
```

## Getting Started

Here is a simple example to demonstrate how to use the library:

```python
from yookassa_api import (
    YooKassa, PaymentAmount,
    Confirmation
)
from yookassa_api.types import CurrencyType 


# Initialize the YooKassa client
client = YooKassa(
    api_key='SECRET_KEY',
    shop_id=999999
)

# Create a payment
payment = client.create_payment(
    PaymentAmount(value=100, currency=CurrencyType.RUB),
    description='Test payment',
    confirmation=Confirmation(                                      
        type=ConfirmationType.REDIRECT,
        return_url="https://t.me/BotFather",                  
    )
)
print(payment)
```

