import uuid
from datetime import datetime
from typing import List, Union, Optional, Any

from yookassa_api.api.base import AsyncBaseClient, BaseClient
from yookassa_api.api.methods import (
    CreatePayment, GetPayments, 
    GetPayment, CapturePayment, CancelPayment,
    CreateRefund, GetRefund, GetRefunds
)
from yookassa_api.schemas import (
    Confirmation, Payment, PaymentsList,
    PaymentAmount, Receipt, Airline, RefundsList,
    Transfer, Deal, Recipient,
    PaymentMethod, Refund
)
from yookassa_api.types import PaymentMethodType, PaymentStatus, RefundStatus

 

class AsyncClient(AsyncBaseClient):
    """Asynchronous client for YooKassa API"""
    def __init__(self, api_key: str, shop_id: int):
        super().__init__(api_key, shop_id)

    async def create_payment(self, amount: PaymentAmount,
                             description: Optional[str] = None,
                             receipt: Optional[Receipt] = None,
                             recipient: Optional[Recipient] = None,
                             payment_token: Optional[str] = None,
                             payment_method_id: Optional[str] = None,
                             payment_method_data: Optional[PaymentMethod] = None,
                             confirmation: Optional[Confirmation] = None,
                             save_payment_method: Optional[bool] = False,
                             capture: Optional[bool] = False,
                             client_ip: Optional[str] = None,
                             metadata: Optional[Any] = None,
                             airline: Optional[Airline] = None,
                             transfers: Optional[List[Transfer]] = None,
                             deal: Optional[Deal] = None,
                             merchant_customer_id: Optional[str] = None
                             ) -> Payment:
        """
        Create payment
        More detailed documentation:
        https://yookassa.ru/developers/api?codeLang=bash#create_payment

        :param merchant_customer_id: Payer ID in the merchant's system
        :param deal: Deal data
        :param transfers: Money distribution data
        :param airline: Object with data for selling air tickets
        :param metadata: Any additional data
        :param client_ip: IPv4 or IPv6 address of the payer
        :param capture: Automatic acceptance of incoming payment
        :param save_payment_method: Save payment data
        :param confirmation:
        :param payment_method_data: Payment method
        :param payment_method_id: Saved payment method ID
        :param payment_token: One-time payment token
        :param recipient: Payment receiver
        :param receipt: Recept generation data
        :param amount: Payment Amount
        :param currency: Payment Currency
        :param description: Payment Description
        :return: Payment
        """

        params = CreatePayment.build_params(**locals())
        headers = {'Idempotence-Key': self._get_idempotence_key()}
        result = await self._send_request(CreatePayment, json=params, headers=headers)
        return Payment(**result)

    async def get_payments(self, created_at: Optional[datetime] = None,
                           captured_at: Optional[datetime] = None,
                           payment_method: Optional[PaymentMethodType] = None,
                           status: Optional[PaymentStatus] = None,
                           limit: Optional[int] = None,
                           cursor: Optional[str] = None,
                           **kwargs) -> PaymentsList:
        """
        Get payments
        More detailed documentation:
        https://yookassa.ru/developers/api?codeLang=php#get_payments_list

        :param created_at: Created at [GTE]
        :param captured_at: Captured at [GTE]
        :param payment_method: Payment Method
        :param status: Payment Status
        :param limit: Objects limit
        :param cursor: Cursor
        :return: Payments List
        """
        params = GetPayments.build_params(created_at=created_at,
                                          captured_at=captured_at,
                                          payment_method=payment_method,
                                          status=status,
                                          limit=limit,
                                          cursor=cursor,
                                          **kwargs)
        result = await self._send_request(GetPayments, params=params)
        return PaymentsList(**result)

    async def get_payment(self, payment_id: str) -> Payment:
        """
        Get payment by id
        More detailed documentation:
        https://yookassa.ru/developers/api?codeLang=bash#get_payment

        :param payment_id: Payment ID
        :return: Payment Info
        """
        method = GetPayment.build(payment_id=payment_id)
        result = await self._send_request(method)
        return Payment(**result)

    async def capture_payment(self, payment_id: str,
                              amount: Optional[PaymentAmount] = None,
                              receipt: Optional[Receipt] = None,
                              airline: Optional[Airline] = None,
                              transfers: Optional[List[Transfer]] = None,
                              deal: Optional[Deal] = None) -> Payment:
        """
        Capture payment
        More detailed documentation:
        https://yookassa.ru/developers/api?codeLang=bash#capture_payment

        :param payment_id: Payment ID
        :param amount: Payment Amount
        :param receipt: Receipt Info
        :param airline: Airline
        :param transfers: Transfers
        :param deal: Deal
        :return: Payment
        """
        method = CapturePayment.build(payment_id=payment_id)
        params = method.build_params(
            amount=amount,
            receipt=receipt,
            airline=airline,
            transfers=transfers,
            deal=deal
        )
        headers = {'Idempotence-Key': self._get_idempotence_key()}
        result = await self._send_request(method, json=params, headers=headers)
        return Payment(**result)

    async def cancel_payment(self, payment_id: str) -> Payment:
        """
        Cancel payment
        More detailed documentation:
        https://yookassa.ru/developers/api#cancel_payment

        :param payment_id: Payment ID
        :return: Payment
        """
        method = CancelPayment.build(payment_id=payment_id)
        headers = {'Idempotence-Key': self._get_idempotence_key()}
        result = await self._send_request(method, headers=headers)
        return Payment(**result)
    
    async def create_refund(
        self, 
        payment_id: str,
        amount: PaymentAmount,
        description: Optional[str] = None,
        receipt: Optional[Receipt] = None,
        sources: Optional[List] = None,
        deal: Optional[Deal] = None,
        **kwargs
    ) -> None:
        """
        Create refund
        More detailed documentation:
        https://yookassa.ru/developers/api#refund_object

        :param payment_id: Payment ID
        :param amount: Payment Amount
        :param description: description
        :param receipt: Receipt Info
        :param sources: sources
        :param deal: deal
        :return: Payment
        """
        params = CreateRefund.build_params(
            payment_id=payment_id,
            description=description,
            amount=amount,
            receipt=receipt,
            sources=sources,
            deal=deal,
            **kwargs)
        headers = {'Idempotence-Key': self._get_idempotence_key()}
        result = await self._send_request(
            CreateRefund, 
            json=params, 
            headers=headers
        )
        return Refund(**result)

    async def get_refunds(
        self,
        created_at_gte = None, 
        created_at_lt = None, 
        payment_id: Optional[str] = None, 
        status: Optional[RefundStatus] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        **kwargs
    ):
        """
        Get all refunds
        More detailed documentation:
        https://yookassa.ru/developers/api#get_refunds_list
        
        :param created_at_gte: created at gte
        :param created_at_lt: created at lt
        :param payment_id: payment ID
        :param status: status
        :param limit: limit
        :param cursor: cursor

        return: Refund
        """
        params = GetRefunds.build_params(
            created_at_gte, 
            created_at_lt, 
            payment_id=payment_id,
            status=status,
            limit=limit,
            cursor=cursor,
            **kwargs
        )
        headers = {'Idempotence-Key': self._get_idempotence_key()}
        result = await self._send_request(
            GetRefunds, 
            json=params,
            headers=headers
        )
        return RefundsList(**result)

    async def get_refund(self, refund_id: str) -> Refund:
        """
        Get refund by id
        More detailed documentation:
        https://yookassa.ru/developers/api#get_refunds_list

        :param refund_id: refund ID

        :return: Refund
        """
        method = GetRefund.build(refund_id=refund_id)
        result = await self._send_request(method)
        return Refund(**result)

    @staticmethod
    def _get_idempotence_key() -> str:
        return uuid.uuid4().hex


class Client(BaseClient):
    """Synchronous client for YooKassa API"""
    def __init__(self, api_key: str, shop_id: Union[int, str]):
        super().__init__(api_key, shop_id)
    
    def create_payment(self, amount: PaymentAmount,
                             description: Optional[str] = None,
                             receipt: Optional[Receipt] = None,
                             recipient: Optional[Recipient] = None,
                             payment_token: Optional[str] = None,
                             payment_method_id: Optional[str] = None,
                             payment_method_data: Optional[PaymentMethod] = None,
                             confirmation: Optional[Confirmation] = None,
                             save_payment_method: Optional[bool] = False,
                             capture: Optional[bool] = False,
                             client_ip: Optional[str] = None,
                             metadata: Optional[Any] = None,
                             airline: Optional[Airline] = None,
                             transfers: Optional[List[Transfer]] = None,
                             deal: Optional[Deal] = None,
                             merchant_customer_id: Optional[str] = None
                             ) -> Payment:
        """
        Create payment
        More detailed documentation:
        https://yookassa.ru/developers/api?codeLang=bash#create_payment

        :param merchant_customer_id: Payer ID in the merchant's system
        :param deal: Deal data
        :param transfers: Money distribution data
        :param airline: Object with data for selling air tickets
        :param metadata: Any additional data
        :param client_ip: IPv4 or IPv6 address of the payer
        :param capture: Automatic acceptance of incoming payment
        :param save_payment_method: Save payment data
        :param confirmation:
        :param payment_method_data: Payment method
        :param payment_method_id: Saved payment method ID
        :param payment_token: One-time payment token
        :param recipient: Payment receiver
        :param receipt: Recept generation data
        :param amount: Payment Amount
        :param currency: Payment Currency
        :param description: Payment Description
        :return: Payment
        """
        
        params = CreatePayment.build_params(**locals())
        headers = {'Idempotence-Key': self._get_idempotence_key()}
        result = self._send_request(CreatePayment, json=params, headers=headers)
        return Payment(**result)
    
    def get_payments(self, created_at: Optional[datetime] = None,
                           captured_at: Optional[datetime] = None,
                           payment_method: Optional[PaymentMethodType] = None,
                           status: Optional[PaymentStatus] = None,
                           limit: Optional[int] = None,
                           cursor: Optional[str] = None,
                           **kwargs) -> PaymentsList:
        """
        Get payments
        More detailed documentation:
        https://yookassa.ru/developers/api?codeLang=php#get_payments_list

        :param created_at: Created at [GTE]
        :param captured_at: Captured at [GTE]
        :param payment_method: Payment Method
        :param status: Payment Status
        :param limit: Objects limit
        :param cursor: Cursor
        :return: Payments List
        """
        params = GetPayments.build_params(created_at=created_at,
                                          captured_at=captured_at,
                                          payment_method=payment_method,
                                          status=status,
                                          limit=limit,
                                          cursor=cursor,
                                          **kwargs)
        result = self._send_request(GetPayments, params=params)
        return PaymentsList(**result)

    def get_payment(self, payment_id: str) -> Payment:
        """
        Get payment by id
        More detailed documentation:
        https://yookassa.ru/developers/api?codeLang=bash#get_payment

        :param payment_id: Payment ID
        :return: Payment Info
        """
        method = GetPayment.build(payment_id=payment_id)
        result = self._send_request(method)
        return Payment(**result)

    def capture_payment(self, payment_id: str,
                              amount: Optional[PaymentAmount] = None,
                              receipt: Optional[Receipt] = None,
                              airline: Optional[Airline] = None,
                              transfers: Optional[List[Transfer]] = None,
                              deal: Optional[Deal] = None) -> Payment:
        """
        Capture payment
        More detailed documentation:
        https://yookassa.ru/developers/api?codeLang=bash#capture_payment

        :param payment_id: Payment ID
        :param amount: Payment Amount
        :param receipt: Receipt Info
        :param airline: Airline
        :param transfers: Transfers
        :param deal: Deal
        :return: Payment
        """
        method = CapturePayment.build(payment_id=payment_id)
        params = method.build_params(
            amount=amount,
            receipt=receipt,
            airline=airline,
            transfers=transfers,
            deal=deal
        )
        headers = {'Idempotence-Key': self._get_idempotence_key()}
        result = self._send_request(method, json=params, headers=headers)
        return Payment(**result)

    def cancel_payment(self, payment_id: str) -> Payment:
        """
        Cancel payment
        More detailed documentation:
        https://yookassa.ru/developers/api#cancel_payment

        :param payment_id: Payment ID
        :return: Payment
        """
        method = CancelPayment.build(payment_id=payment_id)
        headers = {'Idempotence-Key': self._get_idempotence_key()}
        result = self._send_request(method, headers=headers)
        return Payment(**result)

    def create_refund(
        self, 
        payment_id: str,
        amount: PaymentAmount,
        description: Optional[str] = None,
        receipt: Optional[Receipt] = None,
        sources: Optional[List] = None,
        deal: Optional[Deal] = None,
        **kwargs
    ) -> None:
        """
        Create refund
        More detailed documentation:
        https://yookassa.ru/developers/api#refund_object

        :param payment_id: Payment ID
        :param amount: Payment Amount
        :param description: description
        :param receipt: Receipt Info
        :param sources: sources
        :param deal: deal
        :return: Payment
        """
        params = CreateRefund.build_params(
            payment_id=payment_id,
            description=description,
            amount=amount,
            receipt=receipt,
            sources=sources,
            deal=deal,
            **kwargs)
        headers = {'Idempotence-Key': self._get_idempotence_key()}
        result = self._send_request(
            CreateRefund, 
            json=params, 
            headers=headers
        )
        return Refund(**result)

    def get_refunds(
        self,
        created_at_gte = None, 
        created_at_lt = None, 
        payment_id: Optional[str] = None, 
        status: Optional[RefundStatus] = None,
        limit: Optional[int] = None,
        cursor: Optional[str] = None,
        **kwargs
    ):
        """
        Get all refunds
        More detailed documentation:
        https://yookassa.ru/developers/api#get_refunds_list
        
        :param created_at_gte: created at gte
        :param created_at_lt: created at lt
        :param payment_id: payment ID
        :param status: status
        :param limit: limit
        :param cursor: cursor

        return: Refund
        """
        params = GetRefunds.build_params(
            created_at_gte, 
            created_at_lt, 
            payment_id=payment_id,
            status=status,
            limit=limit,
            cursor=cursor,
            **kwargs
        )
        headers = {'Idempotence-Key': self._get_idempotence_key()}
        result = self._send_request(
            GetRefunds, 
            json=params,
            headers=headers
        )
        return RefundsList(**result)

    def get_refund(self, refund_id: str) -> Refund:
        """
        Get refund by id
        More detailed documentation:
        https://yookassa.ru/developers/api#get_refunds_list

        :param refund_id: refund ID

        :return: Refund
        """
        method = GetRefund.build(refund_id=refund_id)
        result = self._send_request(method)
        return Refund(**result)


    @staticmethod
    def _get_idempotence_key() -> str:
        return uuid.uuid4().hex
    


AsyncYooKassa = AsyncClient
YooKassa = Client
