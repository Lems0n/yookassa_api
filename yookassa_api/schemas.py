from datetime import datetime
from typing import List, Literal, Union, Optional

from pydantic import BaseModel

from yookassa_api.types import CurrencyType
from yookassa_api.types import (
    PaymentStatus, ReceiptRegistration, 
    CancellationParty, CancellationReason, 
    ConfirmationType, RefundStatus, RefundMethodType
)


class Confirmation(BaseModel):
    """
    Confirmation
    """
    type: Union[ConfirmationType, str]
    enforce: Optional[bool] = None
    locale: Optional[str] = None
    return_url: Optional[str] = None
    confirmation_url: Optional[str] = None 


class PaymentAmount(BaseModel):
    """
    Payment amount
    """
    value: Union[int, float]
    currency:Union[CurrencyType, str]


class Recipient(BaseModel):
    """
    Payment receiver
    """
    account_id: str
    gateway_id: str


class PayerBankDetails(BaseModel):
    """
    Bank details of the payer
    """
    full_name: str
    short_name: str
    address: str
    inn: str
    bank_name: str
    bank_branch: str
    bank_bik: str
    bank_account: str
    kpp: Optional[str] = None


class VatData(BaseModel):
    """
    VAT data
    """
    type: str
    amount: Optional[PaymentAmount] = None
    rate: Optional[str] = None


class CardInfo(BaseModel):
    """
    Card information
    """
    first_six: Optional[str] = None
    last_four: str 
    expiry_year: str
    expiry_month: str
    card_type: str
    card_country: Optional[str] = None
    source: Optional[str] = None


class PaymentMethod(BaseModel):
    """
    Payment method
    """
    type: str
    id: str
    saved: bool
    title: Optional[str] = None
    login: Optional[str] = None
    card: Optional[CardInfo] = None
    phone: Optional[str] = None
    payer_bank_details: Optional[PayerBankDetails] = None
    payment_purpose: Optional[str] = None
    vat_data: Optional[VatData] = None
    account_number: Optional[str] = None


class Article(BaseModel):
    article_number: int
    payment_article_number: int
    tru_code: str
    quantity: int


class ElectronicCertificateDetails(BaseModel):
    basket_id: str
    amount: PaymentAmount


class ElectronicCertificate(BaseModel):
    """
    Electronic certificate
    """
    type: str = Literal["electronic_certificate"]
    articles: List[Article]
    electronic_certificate: ElectronicCertificateDetails


class SBP(BaseModel):
    """
    SBP
    """
    type: str = Literal["sbp"]
    sbp_operation_id: str


class RefundMethod(BaseModel):
    type: Union[
        ElectronicCertificate,
        SBP
    ]


class CancellationDetails(BaseModel):
    party: CancellationParty
    reason: CancellationReason


class ThreeDSInfo(BaseModel):
    """
    3DS information
    """
    applied: bool


class AuthorizationDetails(BaseModel):
    transaction_identifier: str 
    authorization_code: str 
    three_d_secure: ThreeDSInfo


class Transfer(BaseModel):
    account_id: str
    amount: PaymentAmount
    status: PaymentStatus
    fee_amount: PaymentAmount
    description: Optional[str] = None
    metadata: Optional[dict] = None


class Settlement(BaseModel):
    type: str
    amount: PaymentAmount


class Deal(BaseModel):
    id: str
    settlements: List[PaymentAmount]


class Payment(BaseModel):
    """
    Payment
    """
    id: str
    status: str
    amount: PaymentAmount
    income_amount: Optional[PaymentAmount] = None
    description: Optional[str] = None
    recipient: Recipient
    payment_method: Optional[PaymentMethod] = None
    captured_at: Optional[datetime] = None
    created_at: datetime
    expires_at: Optional[datetime] = None
    confirmation: Optional[Confirmation] = None
    test: bool
    refunded_amount: Optional[PaymentAmount] = None
    paid: bool
    refundable: bool
    receipt_registration: Optional[ReceiptRegistration] = None
    metadata: Optional[dict] = None
    cancellation_details: Optional[CancellationDetails] = None
    authorization_details: Optional[AuthorizationDetails] = None
    transfers: Optional[List[Transfer]] = None
    deal: Optional[Deal] = None
    merchant_customer_id: Optional[str] = None


class Refund(BaseModel):
    id: str
    payment_id: str
    status: RefundStatus
    cancellation_details: Optional[CancellationDetails] = None
    reciept_registration: Optional[ReceiptRegistration] = None
    created_at: datetime
    amount: PaymentAmount
    description: Optional[str] = None
    sources: Optional[List] = None
    deal: Optional[Deal] = None
    refund_method: RefundMethod


class PaymentsList(BaseModel):
    """
    Payments list
    """
    list: List[Payment] 
    cursor: Optional[str] = None


class RefundsList(BaseModel):
    """
    Refunds list
    """
    list: List[Refund]
    cursor: Optional[str] = None


class Customer(BaseModel):
    """
    Customer
    """
    full_name: Optional[str] = None
    inn: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class MarkQuantity(BaseModel):
    """
    Mark quantity
    """
    numerator: int
    denominator: int


class MarkCodeInfo(BaseModel):
    """
    Mark code information
    """
    code: Optional[str] = None
    unknown: Optional[str] = None
    ean_8: Optional[str] = None
    ean_13: Optional[str] = None
    itf_14: Optional[str] = None
    gs_10: Optional[str] = None
    gs_1m: Optional[str] = None
    short: Optional[str] = None
    fur: Optional[str] = None
    egais_20: Optional[str] = None
    egais_30: Optional[str] = None


class IndustryDetails(BaseModel):
    """
    Industry details
    """
    federal_id: str
    document_date: datetime
    document_number: str
    value: str


class PaymentItem(BaseModel):
    """
    Payment items
    """
    description: str
    amount: PaymentAmount
    vat_code: int
    quantity: str
    measure: Optional[str] = None
    mark_quantity: Optional[MarkQuantity] = None
    payment_subject: Optional[str] = None
    payment_mode: Optional[str] = None
    country_of_origin_code: Optional[str] = None
    customs_declaration_number: Optional[str] = None
    excise: Optional[str] = None
    product_code: Optional[str] = None
    mark_code_info: Optional[MarkCodeInfo] = None
    mark_mode: Optional[str] = None
    payment_subject_industry_details: Optional[IndustryDetails]


class OperationDetails(BaseModel):
    """
    Operation details
    """
    id: int 
    value: str
    created_at: datetime


class Receipt(BaseModel):
    """
    Receipt
    """
    customer: Optional[Customer] = None
    items: List[PaymentItem]
    phone: Optional[str] = None
    email: Optional[str] = None
    tax_system_code: Optional[int] = None
    receipt_industry_details: Optional[IndustryDetails] = None
    receipt_operation_details: Optional[OperationDetails] = None


class Passenger(BaseModel):
    first_name: str
    last_name: str


class Flight(BaseModel):
    departure_airport: str
    arrival_airport: str
    departure_date: datetime
    carrier_code: Optional[str] = None


class Airline(BaseModel):
    """
    Airline
    """
    ticket_number: Optional[str] = None
    booking_reference: Optional[str] = None
    passengers: Optional[List[Passenger]] = None
    flights: Optional[List[Flight]]  = None


