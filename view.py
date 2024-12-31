from spay.client import SpayClient

MERCHANT_ID = "XXXXXXXXXXXXXXX"  # your merchant id
AMOUNT = 10000  # amount in rials
CALLBACK_URL = "https://google.com"  # your callback url
DESCRIPTION = ""  # optional
EMAIL = ""  # optional
MOBILE = ""  # optional
spay = SpayClient(
    merchant_id=MERCHANT_ID,
    amount=AMOUNT,
    callback_url=CALLBACK_URL,
    description=DESCRIPTION,
    email=EMAIL,
    mobile=MOBILE,
)

# Get Token
token = spay.get_token()

# Request Payment
payment_response = spay.request_payment()

# Verify Payment
verify_response = spay.verify_payment(token=token)
