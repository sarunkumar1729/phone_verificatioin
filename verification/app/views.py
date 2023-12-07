from django.shortcuts import render
import vonage
# Create your views here.

def phone(request):
    if request.method=='POST':
        phone=request.POST['phone']
        client = vonage.Client(key="479aaf01", secret="V3w3NMQNjnZqDKYS")
        global verify
        verify = vonage.Verify(client)

        global response
        response = verify.start_verification(number=phone, brand="AcmeInc")

        if response["status"] == "0":
            print("Started verification request_id is %s" % (response["request_id"]))
        else:
            print("Error: %s" % response["error_text"])

        global REQUEST_ID
        REQUEST_ID=response['request_id']
        return render(request,'verify.html')
    else:
        return render(request,'phone.html')


def code_verify(request):

    CODE=request.POST['code']

    response = verify.check(REQUEST_ID, code=CODE)

    if response["status"] == "0":
        print("Verification successful, event_id is %s" % (response["event_id"]))
    else:
        print("Error: %s" % response["error_text"])
    
    return render(request,'phone.html')