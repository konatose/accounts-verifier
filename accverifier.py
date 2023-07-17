
import json, aminofix as amino
from aminofix.lib.util.exceptions import *
from hashlib import sha1
from webbrowser import open as OP
from time import sleep
import os
import hmac
from hashlib import sha1


identifier = os.urandom(20)
x= ("19" + identifier.hex() + hmac.new(bytes.fromhex("E7309ECC0953C6FA60005B2765F99DBBC965C8E9"), b"\x19" + identifier, sha1).hexdigest()).upper()
devi = x



accs = json.load(open("accounts.json"))
for acc in accs:
 email = acc['email']
 password = acc['password']
 print("trying")
 client = amino.Client(deviceId=x)
 try:client.login(email,password);print(f"Logged in {email}")
 except AccountDisabled:
  print("rip bozo {email}")
 except VerificationRequired as e:
  print(f"\nVerification required for {email}")
  OP(e.args[0]["url"])
  print(e.args[0]["url"])
  sleep(35)
  input(" If you are finished, press Enter \n ==> ")
 except ActionNotAllowed:
  print("\nWait half an hour, then restart")
  sleep(100) 
 except AccountLimitReached:
  sleep(100)
 except Exception as e:
  print(e)
  sleep(16)
  
 
print("\nDone for all accounts")
