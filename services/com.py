from twilio.rest import TwilioRestClient
import os
import sys

sys.path.append(os.path.dirname(__file__) + '/../../')
os.environ['DJANGO_SETTINGS_MODULE'] = 'base.settings'


from api.models import Ticket

def send_text(to, msg):
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC630bc2eaa9a19496b9f1015aa6ebbb5a"
    auth_token  = "9d3eaa009f0ae6bec3231ad0f8f5e4d2"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.sms.messages.create(body=msg,
        to="9785619093",    # Replace with your phone number
        from_="+14152336787") # Replace with your Twilio number
    print message.sid

ticket = Ticket.objects.get(pk=5)
send_text("+18176148394", "Hi, are the tickets still available from your craigslist listing ("+ticket.title+")?")