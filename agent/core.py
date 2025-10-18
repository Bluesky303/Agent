from .planner import Planner
from .executor import Executor
from .llm import llmModel, ModelEnum
from .logger import PlanExecuteLogger
from .tools import Tools

class Agent:
    def __init__(self):
        self.client = llmModel(ModelEnum.deepseek_client)
        self.logger = PlanExecuteLogger()
        self.planner = Planner(self.client, self.logger)
        self.tools = Tools()
        self.executor = Executor(self.client, self.tools)
        
    
    def run(self):
        while True:
            command = input(">")
            
            if command.startswith(">"):
                # 重置工具和执行器
                self.tools = Tools()
                self.executor = Executor(self.client, self.tools)
                continue  # 直接进入下一次循环
                
            # 生成初始计划
            plan = self.planner.plan(command)
            print(f'Planner: {plan["reply"]}')
            
            # 执行计划循环
            while plan and plan["plan"]:
                replan_data = None
                
                # 执行计划中的每个步骤
                for step in plan["plan"]:
                    self.logger.add_conversation({"role": "step", "content": f"stage: {step}"})
                    response = self.executor.run(step)
                    replan = self.planner.handle(response)
                    
                    print(f'Planner: {replan["reply"]}')
                    
                    if replan["replan"]:
                        replan_data = replan
                        break  # 跳出当前步骤循环，准备重新规划
                
                # 如果有重新规划，更新计划；否则退出循环
                if replan_data:
                    plan = replan_data
                else:
                    break