## How to create refund ?

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
        # returns refund object

if __name__ == '__main__':
    main()
```

### Async version:

```python
import asyncio

from yookassa_api import (
    AsyncYooKassa, RefundStatus,
    PaymentAmount
)


async def main():
    async with AsyncYooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:
        refunds = await client.create_refund(
            payment_id='payment_id',
            amount=PaymentAmount(value=100, currency='RUB'),
            description='Test refund'
        )
        return refund
        # returns refund object

if __name__ == '__main__':
    asyncio.run(main())
```

## How to get list of refunds ?

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
        # returns refund objects list

if __name__ == '__main__':
    main()
```

### Async version:

```python
import asyncio

from yookassa_api import (
    AsyncYooKassa, RefundStatus
)


async def main():
    async with AsyncYooKassa(
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
        # returns refund objects list

if __name__ == '__main__':
    asyncio.run(main())
```

## How to get info about one refund ?

```python
from yookassa_api import YooKassa

def main():
    with YooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:
        refund = client.get_refund(refund_id='refund_id')
        return refund
        # returns refund object

if __name__ == '__main__':
    main()
```

### Async version:

```python
import asyncio

from yookassa_api import (
    AsyncYooKassa
)


async def main():
    async with AsyncIOYooKassa(
        api_key='API_KEY',
        shop_id=999999
    ) as client:
        refund = await client.get_refund(refund_id='refund_id')
        return refund                    
        # returns refund object

if __name__ == '__main__':
    asyncio.run(main())
```