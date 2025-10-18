class ThreeLayerMemorySystem:
    def __init__(self):
        self.recent_memory = []  # 近期记忆：完整信息
        self.midterm_memory = []  # 中期记忆：摘要
        self.longterm_memory = []  # 长期记忆：大纲
        self.raw_storage = {}  # 原始信息永久存储
    
    def add_conversation(self, conversation_id, full_content):
        """添加新的对话记录"""
        # 存储原始信息
        self.raw_storage[conversation_id] = full_content
        
        # 近期记忆：直接存储
        self.recent_memory.append({
            "id": conversation_id,
            "content": full_content,
            "timestamp": self._get_timestamp()
        })
        
        # 生成摘要
        summary = self._generate_summary(full_content)
        self.midterm_memory.append({
            "id": conversation_id,
            "summary": summary,
            "timestamp": self._get_timestamp()
        })
        
        # 生成大纲
        outline = self._generate_outline(summary)
        self.longterm_memory.append({
            "id": conversation_id,
            "outline": outline,
            "timestamp": self._get_timestamp()
        })
        
        self._manage_memory_size()
    
    def _generate_summary(self, content):
        """生成对话摘要"""
        # 简化版摘要生成逻辑
        key_points = []
        lines = content.split("\n")
        for line in lines:
            if len(line.strip()) > 20:  # 简单的关键信息判断
                key_points.append(line[:100] + "..." if len(line) > 100 else line)
        return " | ".join(key_points)
    
    def _generate_outline(self, summary):
        """从摘要生成大纲"""
        # 提取主题关键词
        words = summary.split()
        key_words = [word for word in words if len(word) > 3][:5]  # 取前5个较长词
        return ", ".join(key_words)
    
    def _manage_memory_size(self):
        """管理各层记忆大小"""
        # 近期记忆保留最近50条
        if len(self.recent_memory) > 50:
            self.recent_memory = self.recent_memory[-50:]
        
        # 中期记忆保留最近200条摘要
        if len(self.midterm_memory) > 200:
            self.midterm_memory = self.midterm_memory[-200:]
    
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()
    
    def query_memory(self, query, detail_level="auto"):
        """查询记忆系统"""
        if detail_level == "auto":
            # 根据查询复杂度自动选择层级
            if len(query) < 10:
                return self._query_longterm(query)
            else:
                return self._query_midterm(query)
        elif detail_level == "outline":
            return self._query_longterm(query)
        elif detail_level == "summary":
            return self._query_midterm(query)
        else:
            return self._query_recent(query)
    
    def _query_longterm(self, query):
        """在长期记忆中查询"""
        results = []
        for memory in self.longterm_memory:
            if query.lower() in memory["outline"].lower():
                results.append(memory)
        return results
    
    def _query_midterm(self, query):
        """在中期记忆中查询"""
        results = []
        for memory in self.midterm_memory:
            if query.lower() in memory["summary"].lower():
                # 如果需要详细信息，可以从原始存储中获取
                full_content = self.raw_storage.get(memory["id"])
                memory["full_content"] = full_content
                results.append(memory)
        return results
    
    def _query_recent(self, query):
        """在近期记忆中查询"""
        results = []
        for memory in self.recent_memory:
            if query.lower() in memory["content"].lower():
                results.append(memory)
        return results

# 使用示例
if __name__ == "__main__":
    memory_system = ThreeLayerMemorySystem()
    
    # 添加一些测试对话
    test_conversation = "用户询问关于AI架构的问题，我们讨论了plan-and-execute模式的优缺点"
    memory_system.add_conversation("conv_001", test_conversation)
    
    # 查询测试
    results = memory_system.query_memory("AI架构")
    print("查询结果：", results)