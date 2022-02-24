import requests
import time
print("")
cc = input("your country (66) : ")
phone = input(f"Phone : +{cc}")
me = input("Message : ")
print("")

for i in range(1):
	requests.post("https://textbelt.com/text", data={"phone": "+66"+phone,"message": me,"key": "textbelt"})
	print("message sent")