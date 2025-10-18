class TextAnalyzer:
    """
    文本分析器工具
    
    功能：对输入的文本进行基础分析，包括字数统计、字符统计、句子数量统计等
    
    参数：
    text - 需要分析的文本字符串
    
    返回：包含分析结果的字典
    """
    
    def __init__(self):
        pass
    
    def analyze(self, text):
        """
        分析文本内容
        
        Args:
            text (str): 需要分析的文本
            
        Returns:
            dict: 包含以下分析结果的字典：
                - char_count: 字符总数
                - word_count: 单词总数
                - sentence_count: 句子总数
                - line_count: 行数
        """
        if not text:
            return {
                'char_count': 0,
                'word_count': 0, 
                'sentence_count': 0,
                'line_count': 0
            }
        
        # 字符统计
        char_count = len(text)
        
        # 单词统计（简单空格分割）
        words = text.split()
        word_count = len(words)
        
        # 句子统计（基于句号、问号、感叹号）
        import re
        sentences = re.split(r'[.!?]+', text)
        sentence_count = len([s for s in sentences if s.strip()])
        
        # 行数统计
        line_count = len(text.splitlines())
        
        return {
            'char_count': char_count,
            'word_count': word_count,
            'sentence_count': sentence_count,
            'line_count': line_count
        }