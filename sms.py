
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACCOUNT_SID_PASTE_HERE'
auth_token = 'AUTH_TOKEN_PASTE_HERE'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="sms with python through twillio api.",
                     from_='twilio_allocated_number',
                     to='reciever_phone_number'
                 )

print(message.sid)
