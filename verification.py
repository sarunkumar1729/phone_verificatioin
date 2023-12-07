# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACf5de1cb094d36c85c4d3dc771e1bd153"
auth_token = "dbce743a0605204a5bb9996c74fa3c03"
verify_sid = "VA0a3769037a53832dc6ce85f2b3cd4b71"
verified_number = "+918848697113"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)