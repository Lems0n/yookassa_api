from enum import StrEnum


class PaymentStatus(StrEnum):
    """
    Payment status

    More detailed documentation:
    https://yookassa.ru/developers/payment-acceptance/getting-started/payment-process#lifecycle
    """
    WAITING_FOR_CAPTURE = 'waiting_for_capture'
    SUCCEEDED = 'succeeded'
    CANCELED = 'canceled'
    PENDING = 'pending'


class RefundStatus(StrEnum):
    PENDING = 'pending'
    SUCCEEDED = 'succeeded'
    CANCELLATION_DETAILS = "cancellation_details"


class ConfirmationType(StrEnum):
    """
    Confirmation type

    More detailed documentation:
    https://yookassa.ru/developers/payment-acceptance/getting-started/payment-process#confirmation
    """
    REDIRECT = 'redirect'
    EXTERNAL = 'external'
    EMBEDDED = 'embedded'
    MOBILE_APPLICATION = 'mobile_application'
    QR_CODE = 'qr'


class CurrencyType(StrEnum):
    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"
    BYN = "BYN"
    CNY = "CNY"
    KZT = "KZT"
    UAH = "UAH"


class ReceiptRegistration(StrEnum):
    """
    Receipt registration
    """
    SUCCEEDED = 'succeeded'
    PENDING = 'pending'
    CANCELED = 'canceled'


class CancellationParty(StrEnum):
    """
    Cancellation party

    More detailed documentation:
    https://yookassa.ru/developers/payment-acceptance/after-the-payment/declined-payments#cancellation-details-party
    """
    MERCHANT = 'merchant'
    PAYMENT_NETWORK = 'payment_network'
    YOO_MONEY = 'yoo_money'


class CancellationReason(StrEnum):
    """
    Cancellation reason

    More detailed documentation:
    https://yookassa.ru/developers/payment-acceptance/after-the-payment/declined-payments#cancellation-details-reason
    """
    THREE_DS_CHECK_FAILED = '3d_secure_failed'
    CALL_ISSUER = 'call_issuer'
    CANCELLED_BY_MERCHANT = 'cancelled_by_merchant'
    CARD_EXPIRED = 'card_expired'
    COUNTRY_FORBIDDEN = 'country_forbidden'
    DEAL_EXPIRED = 'deal_expired'
    EXPIRED_ON_CAPTURE = 'expired_on_capture'
    EXPIRED_ON_CONFIRMATION = 'expired_on_confirmation'
    FRAUD_SUSPECTED = 'fraud_suspected'
    GENERAL_DECLINE = 'general_decline'
    IDENTIFICATION_REQUIRED = 'identification_required'
    INSUFFICIENT_FUNDS = 'insufficient_funds'
    INTERNAL_TIMEOUT = 'internal_timeout'
    INVALID_CARD_NUMBER = 'invalid_card_number'
    INVALID_CSC = 'invalid_csc'
    ISSUER_UNAVAILABLE = 'issuer_unavailable'
    PAYMENT_METHOD_LIMIT_EXCEEDED = 'payment_method_limit_exceeded'
    PAYMENT_METHOD_RESTRICTED = 'payment_method_restricted'
    PERMISSION_REVOKED = 'permission_revoked'
    UNSUPPORTED_MOBILE_OPERATOR = 'unsupported_mobile_operator'


class PaymentMethodType(StrEnum):
    """
    Payment method types
    More detailed documentation:
    https://yookassa.ru/developers/payment-acceptance/getting-started/payment-methods#all
    """
    CARD = 'bank_card'
    YOO_MONEY = 'yoo_money'
    QIWI = 'qiwi'
    SBERBANK = 'sberbank'
    ALFABANK = 'alfabank'
    TINKOFF_BANK = 'tinkoff_bank'
    B2B_SBERBANK = 'b2b_sberbank'
    SBP = 'sbp'
    MOBILE_BALANCE = 'mobile_balance'
    CASH = 'cash'
    INSTALLMENTS = 'installments'


class RefundMethodType(StrEnum):
    SBP = "sbp"
    ELECTRONIC_CERTIFICATE = "electronic_certificate"
    