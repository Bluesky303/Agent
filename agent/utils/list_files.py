class list_files:
    desc = "列出指定目录下的文件和文件夹。参数：directory_path - 目录路径字符串，默认为当前目录"

    def __call__(self, directory_path="."):
        import os
        try:
            items = os.listdir(directory_path)
            return {
                "status": "success",
                "directory": directory_path,
                "files": items,
                "count": len(items)
            }
        except FileNotFoundError:
            return {"status": "error", "message": f"目录未找到: {directory_path}"}
        except PermissionError:
            return {"status": "error", "message": f"无权限访问目录: {directory_path}"}
        except Exception as e:
            return {"status": "error", "message": f"列出文件时出错: {str(e)}"}