from twilio.rest import Client


TWILIO_SID: str = YOUR_TWILIO_SID
TWILIO_AUTH_TOKEN: str = YOUR_TWILIO_AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER: str = YOUR_TWILIO_VIRTUAL_NUMBER
TWILIO_VERIFIED_NUMBER: str = YOUR_TWILIO_VERIFIED_NUMBER


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message: str) -> None:
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
