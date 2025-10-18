import requests
import json

class balance:
    desc = "函数用于查询模型剩余的余额, 无参数"
    def __call__(self):
        url = "https://api.deepseek.com/user/balance"

        payload={}
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {json.load(open("./apikey.json", "r"))["key"]}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.text
