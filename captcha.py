from request import http


def game_captcha(gt: str, challenge: str):
	rep = http.post{
	url="http://api.rrocr.com/api/recognize.html" , # API地址
	data=
		"appkey": "" ,
		"gt": gt,
		"challenge" : challenge,
		"referer" : "https://api-takumi.mihoyo.com/event/bbs_sign_reward/sign"
		}
    return rep["data"]["validate"]  # 失败返回None 成功返回validate


def bbs_captcha(gt: str, challenge: str):
    return None
