from typing import TypeVar, Generic, Optional, List
from yookassa_api.schemas import PaymentAmount, Receipt, Airline, Transfer, Deal


T = TypeVar('T') 


class APIMethod(Generic[T]):
    """
    Base API Method
    """
    http_method: str = "GET"
    path: str


class PaymentMethod(APIMethod):
    """
    Payment Method
    """
    http_method = "GET"
    path = "/payments"

    def __init__(self, path: str):
        self.path = path

    @classmethod
    def build(cls, payment_id):
        """
        Build method
        :param payment_id: Payment ID
        :return: Method
        """
        path = cls.path.format(payment_id=payment_id)
        return cls(path=path)


class CreatePayment(APIMethod):
    """
    Create payment
    """
    http_method = "POST"
    path = "/payments"

    @staticmethod
    def build_params(**kwargs):
        if confirmation := kwargs.get("confirmation"):
            kwargs["confirmation"] = confirmation.model_dump(exclude_none=True)
        params = {
            "amount": kwargs.get("amount").model_dump(),
            "description": kwargs.get("description"),
            "receipt": kwargs.get("receipt").model_dump() if kwargs.get("receipt") else None,
            "recipient": kwargs.get("recipient").model_dump() if kwargs.get("recipient") else None,
            "payment_token": kwargs.get("payment_token"),
            "payment_method_id": kwargs.get("payment_method_id"),
            "payment_method_data": kwargs.get("payment_method_data").model_dump() if kwargs.get("payment_method_data") else None,
            "confirmation": kwargs.get("confirmation"),
            "save_payment_method": kwargs.get("save_payment_method"),
            "capture": kwargs.get("capture"),
            "client_ip": kwargs.get("client_ip"),
            "metadata": kwargs.get("metadata"),
            "airline": kwargs.get("airline").model_dump() if kwargs.get("airline") else None,
            "transfers": kwargs.get("transfers").model_dump() if kwargs.get("transfers") else None,
            "deal": kwargs.get("deal").model_dump() if kwargs.get("deal") else None,
            "merchant_customer_id": kwargs.get("merchant_customer_id"),
        }
        return params


class GetPayments(APIMethod):
    """
    Get Payments
    """
    http_method = "GET"
    path = "/payments"

    @staticmethod
    def build_params(created_at, captured_at,
                     payment_method, status,
                     limit, cursor, **kwargs):
        params = {
            "created_at_gte": created_at,
            "captured_at_gte": captured_at,
            "payment_method": payment_method.value if payment_method else None,
            "status": status.value if status else None,
            "limit": limit,
            "cursor": cursor,
            **kwargs
        }
        return params


class GetPayment(PaymentMethod):
    """
    Get Payment
    """
    http_method = "GET"
    path = "/payments/{payment_id}"


class CapturePayment(PaymentMethod):
    """
    Capture Payment
    """
    http_method = "POST"
    path = "/payments/{payment_id}/capture"

    @staticmethod
    def build_params(amount: Optional[PaymentAmount],
                     receipt: Optional[Receipt],
                     airline: Optional[Airline],
                     transfers: Optional[List[Transfer]],
                     deal: Optional[Deal]):
        params = {
            "amount": amount.model_dump() if amount else None,
            "receipt": receipt.model_dump() if receipt else None,
            "airline": airline.model_dump() if airline else None,
            "transfers": [transfer.model_dump() for transfer in transfers] if transfers else None,
            "deal": deal.model_dump() if deal else None,
        }
        return params


class CancelPayment(PaymentMethod):
    http_method = "POST"
    path = "/payments/{payment_id}/cancel"
    

class CreateRefund(APIMethod):
    """
    Create refund
    """
    http_method = "POST"
    path = "/refunds"

    @staticmethod
    def build_params(payment_id, description, 
                     amount, receipt, 
                     sources, deal, **kwargs):
        params = {
            "payment_id": payment_id,
            "amount": amount.model_dump(),
            "description": description,
            "receipt": receipt.model_dump() if receipt else None,
            "sources": sources.model_dump() if sources else None,   
            "deal": deal.model_dump() if deal else None,    
            **kwargs
        }
        return params
    

class GetRefunds(APIMethod):
    """
    Get refunds
    """
    http_method = "GET"
    path = "/refunds"

    @staticmethod
    def build_params(
        created_at_gte, 
        created_at_lt, 
        payment_id,
        status,
        limit, 
        cursor, 
        **kwargs
    ):
        params = {
            "created_at_gte": created_at_gte,
            "created_at_lt": created_at_lt,
            "payment_id": payment_id if payment_id else None,
            "status": status if status else None,
            "limit": limit if limit else None,
            "cursor": cursor if cursor else None,
            **kwargs
        }
        return params
    

class GetRefund(APIMethod):
    """
    Get refund
    """
    http_method = "GET"
    path = "/refunds/{refund_id}"
