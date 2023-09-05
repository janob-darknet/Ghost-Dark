import os , sys

while True:
	from banners import banner
	banner = banner.banner
	if banner == "1":
		os.system("cd projects && python webcloner.py")
	
	elif banner == "2":
		os.system("cd projects && python sms-bomber.py")
	
	elif banner == "4":
		os.system("cd projects && python zip-crack.py")
	
	elif banner == '3':
		os.system("cd projects && python image-encode-decode.py")
	
	elif banner == '5':
		os.system("cd projects && python admin-finder.py")
		