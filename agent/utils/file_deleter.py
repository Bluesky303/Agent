import os

def FileDeleter(file_path):
    desc="""
    删除指定路径的文件
    
    参数:
        file_path (str): 要删除的文件路径
        
    返回:
        str: 删除结果信息
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return f"文件 {file_path} 删除成功"
        else:
            return f"文件 {file_path} 不存在"
    except Exception as e:
        return f"删除文件时出错: {str(e)}"
