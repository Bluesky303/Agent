class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, description=""):
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'status': 'pending'
        }
        self.tasks.append(task)
        return task
    
    def list_tasks(self):
        return self.tasks
    
    def update_status(self, task_id, status):
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = status
                return task
        return None
    
    def get_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None

# 使用示例
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("学习Python", "完成面向对象编程练习")
    manager.add_task("写报告", "项目总结报告")
    print("所有任务:", manager.list_tasks())