## How to create payment ?

```python
from yookassa_api import (
    YooKassa, PaymentAmount,
    Confirmation
)
from yookassa_api.enums import ConfirmationType


def main():
    with YooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:                                     
        payment = client.create_payment(
            PaymentAmount(value=100, currency='RUB'),
            description='Test payment',
            confirmation=Confirmation(                                      
                type=ConfirmationType.REDIRECT,
                return_url="https://t.me/BotFather",                  
            )
        )
        return payment.confirmation.confirmation_url 
        # so it returns payment link                     


if __name__ == '__main__':
    main()
```

### Or you can do it like this:

```python
from yookassa_api import (
    YooKassa, PaymentAmount,
    Confirmation
)
from yookassa_api.enums import ConfirmationType


def main():
    client = YooKassa(
        api_key='API_KEY',
        shop_id=999999
    )                                  
    payment = client.create_payment(
        PaymentAmount(value=100, currency='RUB'),
        description='Test payment',
        confirmation=Confirmation(                                      
            type=ConfirmationType.REDIRECT,
            return_url="https://t.me/BotFather",                                                    
            confirmation_url="Smth interestimg"
        )
    )
    return payment.confirmation.confirmation_url 
    # so it returns payment link                     


if __name__ == '__main__':
    main()
```

### Async version:

```python
import asyncio

from yookassa_api import (
    AsyncIOYooKassa, PaymentAmount,
    Confirmation
)
from yookassa_api.enums import ConfirmationType


async def main():
    client = AsyncIOYooKassa(
        api_key='API_KEY',    
        shop_id=999999
    )                               
    payment = await client.create_payment(
        PaymentAmount(value=100, currency='RUB'),
        description='Test payment',
        confirmation=Confirmation(                                      
            type=ConfirmationType.REDIRECT,
            return_url="https://t.me/BotFather",                                                    
            confirmation_url="Smth interestimg"
        )
    )
    return payment.confirmation.confirmation_url 
    # so it returns payment link                     


if __name__ == '__main__':
    asyncio.run(main())
```

## How to get payment ? 

```python
from yookassa_api import (
    YooKassa, PaymentAmount,
    Confirmation
)
from yookassa_api.enums import ConfirmationType


def main():
    with YooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:                                     
        payment = client.get_payment(
            payment_id="YOUR_PAYMENT_ID"
        )
        return payment.status == "successed"                    


if __name__ == '__main__':
    main()
```

### Async version:

```python
import asyncio

from yookassa_api import (
    AsyncIOYooKassa, PaymentAmount,
    Confirmation
)
from yookassa_api.enums import ConfirmationType


async def main():
    client = AsyncIOYooKassa(
        api_key='API_KEY',
        shop_id=999999
    )
    payment = await client.get_payment(
        payment_id="YOUR_PAYMENT_ID"
    )
    return payment.status == "successed" 


if __name__ == '__main__':
    asyncio.run(main())
```

## How to cancel payment ?

```python
from yookassa_api import (
    YooKassa, PaymentAmount,
    Confirmation
)
from yookassa_api.enums import ConfirmationType


def main():
    with YooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:                                     
        payment = client.cancel_payment(
            payment_id="YOUR_PAYMENT_ID"
        )
        print(payment)                 


if __name__ == '__main__':
    main()
```

### Async version:

```python
import asyncio

from yookassa_api import (
    AsyncIOYooKassa, PaymentAmount,
    Confirmation
)
from yookassa_api.enums import ConfirmationType


async def main():
    client = AsyncIOYooKassa(
        api_key='API_KEY',
        shop_id=999999
    )
    payment = await client.cancel_payment(
        payment_id="YOUR_PAYMENT_ID"
    )
    print(payment)


if __name__ == '__main__':
    asyncio.run(main())
```
