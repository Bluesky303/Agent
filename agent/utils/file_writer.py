class file_writer:
    desc = "写入内容到指定文件路径，支持创建新文件或覆盖已有文件。参数：file_path - 文件路径字符串，content - 要写入的内容字符串"

    def __call__(self, file_path, content):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return {"status": "success", "message": f"文件 {file_path} 写入成功", "content_length": len(content)}
        except Exception as e:
            return {"status": "error", "message": f"文件写入失败: {str(e)}"}