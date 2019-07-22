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
client = Client("**hidden**", "**hidden**")
client.messages.create(to="+918167597272", 
                       from_="+14432956802", 
                       body=totp.now())





