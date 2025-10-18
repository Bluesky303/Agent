import json
import re
import os
from datetime import datetime
from typing import List, Dict, Any

class PlanExecuteLogger:
    def __init__(self, log_file: str = None):
        # 创建logs目录
        os.makedirs("logs", exist_ok=True)
        
        # 如果没有指定日志文件，使用时间戳作为文件名
        if log_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = f"logs/{timestamp}.txt"
        else:
            # 如果指定了文件名但不在logs目录下，将其移动到logs目录
            if not log_file.startswith("logs/"):
                log_file = f"logs/{log_file}"
        
        self.log_file = log_file
        self.conversations = []
        
    def add_conversation(self, d: dict):
        role = d["role"]
        content = d["content"]
        
        if role == "assistant":
            # 解析planner的回复
            parsed_content = self._parse_planner_content(content)
            log_entry = {
                "role": "planner",
                "content": parsed_content,
                "raw_content": content
            }
        elif role == "user":
            # 解析user/executor的回复
            parsed_content = self._parse_user_content(content)
            log_entry = {
                "role": "executor" if content.startswith("Executor: ") else "user",
                "content": parsed_content,
                "raw_content": content
            }
        else:
            log_entry = {
                "role": role,
                "content": content,
                "raw_content": content
            }
            
        self.conversations.append(log_entry)
        self._write_to_log_file(log_entry)
        
    def _parse_planner_content(self, content: str) -> str:
        """解析planner的JSON内容"""
        try:
            # 提取JSON部分
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
                
                result = ""
                # 处理reply部分
                if 'reply' in data:
                    result += f"Planner: {data['reply']}\n"
                
                # 处理plan部分
                if 'plan' in data and isinstance(data['plan'], list):
                    plan_text = "Plan:\n"
                    for i, step in enumerate(data['plan'], 1):
                        plan_text += f"{i}. {step}\n"
                    result += plan_text
                    
                if 'replan' in data:
                    replan_text = "Replan: " + str(data['replan'])
                    result += replan_text
                
                return result.strip()
            else:
                return f"Planner: {content}"
                
        except json.JSONDecodeError:
            return f"Planner: {content}"
    
    def _parse_user_content(self, content: str) -> str:
        """解析user/executor内容"""
        if content.startswith("Executor: "):
            return content  # 保持原样，因为已经包含Executor标记
        else:
            return f"User: {content}"
    
    def _write_to_log_file(self, log_entry: Dict[str, Any]):
        """写入日志文件"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(f"{log_entry['content']}\n\n")
    
    def get_conversation_log(self) -> str:
        """获取完整的对话日志"""
        log_text = ""
        for entry in self.conversations:
            log_text += f"{entry['content']}\n\n"
        return log_text
    
    def get_formatted_conversation(self) -> str:
        """获取格式化后的对话内容（不含时间戳）"""
        formatted_text = ""
        for entry in self.conversations:
            formatted_text += f"{entry['content']}\n\n"
        return formatted_text
    
    def save_json_log(self, filename: str = None):
        """保存完整的JSON日志"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"logs/conversation_backup_{timestamp}.json"
        elif not filename.startswith("logs/"):
            filename = f"logs/{filename}"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.conversations, f, ensure_ascii=False, indent=2)
    
    def load_json_log(self, filename: str):
        """从JSON文件加载对话记录"""
        if not filename.startswith("logs/"):
            filename = f"logs/{filename}"
            
        with open(filename, 'r', encoding='utf-8') as f:
            self.conversations = json.load(f)
    
    def clear_log(self):
        """清空日志"""
        self.conversations = []
        # 清空文件
        with open(self.log_file, 'w', encoding='utf-8') as f:
            f.write("")