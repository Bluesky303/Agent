class file_reader:
    desc = "读取指定路径的文件内容，返回文件内容字符串。参数：file_path - 文件路径字符串"
    
    def __call__(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return {"status": "success", "content": content}
        except FileNotFoundError:
            return {"status": "error", "message": f"文件未找到: {file_path}"}
        except Exception as e:
            return {"status": "error", "message": f"读取文件时出错: {str(e)}"}