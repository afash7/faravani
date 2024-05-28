from twilio.rest import Client
from django.conf import settings

def send_verification_code(phone_number, code):
    # Your Account SID from twilio.com/console
    account_sid = settings.TWILIO_ACCOUNT_SID
    # Your Auth Token from twilio.com/console
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=phone_number,
        from_=settings.TWILIO_PHONE_NUMBER,
        body=f'Your verification code is {code}'
    )

    return message.sid