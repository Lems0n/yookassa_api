<div align="center">

# YooKassa API Library

[![YooKassaAPI](https://img.shields.io/badge/0.1.1-blue?style=flat&logo=pypi&label=pypi&labelColor=gray)](https://github.com/Lems0n)
[![YooKassaAPI](https://img.shields.io/badge/license-MIT-12C4C4?style=flat&logo=gitbook&logoColor=12C4C4)](https://github.com/Lems0n)
[![YooKassaAPI](https://img.shields.io/badge/3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14%20-yellow?logo=python&logoColor=yellow&label=python&labelColor=gray)](https://github.com/Lems0n)
</div>

# 📌 Description

YooKassa API Library is a Python package designed to simplify interaction with YooKassa's API. This library provides a convenient way to handle payments, refunds, and various operations by utilizing the comprehensive methods available in the YooKassa API.

Also there is both a synchronous and asynchronous variation

## 🔨 Features

- Easy-to-use interface for YooKassa API.
- Supports payment creation, capture, and cancellation.

## 🗃️ Installation

To install the library, use pip:

```shell
pip install yookassa_api
```

Or you can install it by Poetry:

```shell
poetry add yookassa_api
```

## 💻 Getting Started

Here is a simple example to demonstrate how to use the library:

```python
from yookassa_api import (
    YooKassa, PaymentAmount,
    Confirmation
)
from yookassa_api.types import CurrencyType 


# Initialize the YooKassa client
client = YooKassa(
    'SECRET_KEY',
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

## 👤 Author of YooKassa API Library
**© [Lemson](https://t.me/nveless)**