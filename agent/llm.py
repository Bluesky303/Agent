from openai import OpenAI
from enum import Enum
import json

class ModelEnum(Enum):
    deepseek_client = {
        "client": OpenAI(api_key=json.load(open("./apikey.json", "r"))["key"], base_url="https://api.deepseek.com"), 
        "model": "deepseek-chat"
    }
    silicon_ds_v32 = {
        "client": OpenAI(api_key=json.load(open("./apikey.json", "r"))["key2"], base_url="https://api.siliconflow.cn/v1"),
        "model": "deepseek-ai/DeepSeek-V3.2-Exp"
    }


class llmModel:
    def __init__(self, model: ModelEnum):
        self.client: OpenAI = model.value["client"]
        self.model: str = model.value["model"]
    def chat(self, messages):
        
        return self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=1
        ).choices[0].message.content