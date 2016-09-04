# Lesson 4

from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACa45b607472f4b217fab9f3f0dd7ead31"
auth_token = "f29a357efe667d46040e30705121b31d"
client = TwilioRestClient(account_sid, auth_token)

phone_twilio = "+19179243011"
phone_marc = "+19178858674"
phone_chelsea = "+17187579008"

message = client.messages.create(to=phone_marc,
    from_=phone_twilio,
    body="Coucou Chelsea ! C'est Marc qui envoie des textos depuis internet. :)")

print(message.sid)
