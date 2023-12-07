import vonage

client = vonage.Client(key="479aaf01", secret="V3w3NMQNjnZqDKYS")
verify = vonage.Verify(client)


response = verify.start_verification(number="918848697113", brand="AcmeInc")

if response["status"] == "0":
    print("Started verification request_id is %s" % (response["request_id"]))
else:
    print("Error: %s" % response["error_text"])


REQUEST_ID=response['request_id']
CODE=input('CODE : ')

response = verify.check(REQUEST_ID, code=CODE)

if response["status"] == "0":
    print("Verification successful, event_id is %s" % (response["event_id"]))
else:
    print("Error: %s" % response["error_text"])