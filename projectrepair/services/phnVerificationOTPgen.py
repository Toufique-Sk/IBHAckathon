import pyotp
import random
import string
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

totp=pyotp.TOTP(str(randomString()))
print (totp.now())
from twilio.rest import Client
client = Client("ACeb71e9e2fbe4c14efa04c2e47fc6a82b", "5b65b294e374b358a73e15bb0e0730c6")

#need to get a number to send sms to unverified nos.
client.messages.create(to="+918167597272", 
                       from_="+14432956802", 
                       body=totp.now())





