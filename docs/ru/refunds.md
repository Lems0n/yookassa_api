## Как создать возврат?

```python
from yookassa_api import YooKassa, PaymentAmount

def main():
    with YooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:
        refund = client.create_refund(
            payment_id='payment_id',
            amount=PaymentAmount(value=100, currency='RUB'),
            description='Test refund'
        )
        return refund
        # возвращает объект возврата

if __name__ == '__main__':
    main()
```

### Асинхронный вариант:

```python
import asyncio

from yookassa_api import (
    AsyncIOYooKassa, RefundStatus,
    PaymentAmount
)


async def main():
    async with AsyncIOYooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:
        refunds = await client.create_refund(
            payment_id='payment_id',
            amount=PaymentAmount(value=100, currency='RUB'),
            description='Test refund'
        )
        return refund
        # возвращает объект возврата

if __name__ == '__main__':
    asyncio.run(main())
```

## Как получить список возвратов?

```python
from yookassa_api import YooKassa, RefundStatus

def main():
    with YooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:
        refunds = client.get_refunds(
            payment_id='payment_id',
            status=RefundStatus.SUCCEEDED,
            limit=10,
            cursor='cursor'
        )
        return refunds
        # возвращает список объектов возвратов

if __name__ == '__main__':
    main()
```

### Асинхронный вариант:

```python
import asyncio

from yookassa_api import (
    AsyncIOYooKassa, RefundStatus
)


async def main():
    async with AsyncIOYooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:
        refunds = await client.get_refunds(
            payment_id='payment_id',
            status=RefundStatus.SUCCEEDED,
            limit=10,
            cursor='cursor'
        )
        return refunds
        # возвращает список объектов возвратов

if __name__ == '__main__':
    asyncio.run(main())
```

## Как получить информацию о возврате?

```python
from yookassa_api import YooKassa

def main():
    with YooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:
        refund = client.get_refund(refund_id='refund_id')
        return refund
        # возвращает объект возврата

if __name__ == '__main__':
    main()
```

### Асинхронный вариант:

```python
import asyncio

from yookassa_api import (
    AsyncIOYooKassa
)


async def main():
    async with AsyncIOYooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:
        refund = await client.get_refund(refund_id='refund_id')
        return refund                    
        # возвращает объект возврата

if __name__ == '__main__':
    asyncio.run(main())
```