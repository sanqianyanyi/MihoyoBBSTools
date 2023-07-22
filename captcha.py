from request import http


def game_captcha(gt: str, challenge: str):
	rep = http.post(
	url="http://api.rrocr.com/api/recognize.html" , # API地址
	data={
		"appkey": "b5432cd7ebdc4498b16aede06be48646" ,
		"gt": gt,
		"challenge" : challenge,
		"referer" : "https://api-takumi.mihoyo.com/event/bbs_sign_reward/sign"
		}
	).json()
	return rep["data"]["validate"]

def bbs_captcha(gt: str, challenge: str):
	rep = http.post(
	url="http://api.rrocr.com/api/recognize.html" , # API地址
	data={
		"appkey": "b5432cd7ebdc4498b16aede06be48646" ,
		"gt": gt,
		"challenge" : challenge,
		"referer" : "https://api-takumi.mihoyo.com/event/bbs_sign_reward/sign"
		}
	).json()
	return rep["data"]["validate"]
