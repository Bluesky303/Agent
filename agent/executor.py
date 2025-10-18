from .llm import llmModel
from .tools import Tools

import json

class Executor:
    def __init__(self, client: llmModel, tools: Tools):
        self.client = client
        self.tools = tools
        
    def run(self, step):
        print(f"stage: {step}")
        messages = []
        executor_prompt = f"""角色定义: 
你是计划执行器(Executor), 负责通过思考和工具执行Planner制定的步骤。

核心职责: 
1. 解析Planner指示的执行步骤
2. 思考步骤的解决方案
3. 选择合适的工具并完成单次调用, 如果不需要使用工具则直接回复, 比如说查询可用工具列表和返回代码的时候
4. 如果使用了工具, 对工具返回结果进行初步判断和整理
5. 向Planner反馈执行情况

工具调用规则: 
每个执行步骤最多进行一次工具调用
非必要情况下不进行工具调用
调用完成后必须立即回复Planner
如需多次调用, 在回复中明确说明原因和后续需求

可用工具: 
{self.tools.function_list()}

返回必须使用严格的JSON格式, 但是需要使用纯文本, 也即不添加这个标记: ```
而且句子中不能使用英文引号，应该使用中文引号
返回格式: (不要标记```)
{{
    "type": "工具类型或Reply",
    "args": ["参数1", "参数2"],
    "kargs": {{"参数名": "参数值"}},
    "content": "仅Reply类型时使用"
}}
特殊情况处理: 
当Planner询问工具类型或无需工具调用时, 可以使用Reply类型直接回复
Reply内容应简洁明了, 避免冗长描述, 但是代码等必要信息需要完整
被要求具体数据时应该原封不动返回，不过长度应该有一个上限，由你来判断
无参数的工具调用返回空列表和字典
当前执行步骤: 
{step}

执行流程: 
分析步骤 → 选择工具 → 准备参数 → 执行调用 → 整理结果 → 返回反馈
或者: 
分析步骤 → 返回反馈
"""
        messages.append({"role": "system", "content": executor_prompt})
        messages.append({"role": "user", "content": "请按照格式输出你的调用"})
        
        response: str = self.client.chat(messages)
        messages.append({"role": "assistant", "content": response})
        if not response.startswith("{"):
            response[7:-3]
        tool = json.loads(response)
        
        if tool["type"] == "Reply":
            return tool["content"]
        else:
            re = self.tools.function_call(tool["type"], tool["args"], tool["kargs"])
        messages.append({"role": "user", "content": f"工具提供了返回信息: {re}, 请根据内容进行reply"})
        response = json.loads(self.client.chat(messages))
        
        return response["content"]
        
        
