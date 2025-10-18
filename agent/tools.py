import os
import importlib.util
import inspect
TOOLS_DIR = "./agent/utils"
class Tools:
    def __init__(self):
        # 保存函数和描述
        self.functions = {}

        # 遍历 tools 文件夹
        for filename in os.listdir(TOOLS_DIR):
            if filename.endswith(".py") and not filename.startswith("__"):
                filepath = os.path.join(TOOLS_DIR, filename)
                module_name = filename[:-3]

                # 动态导入模块
                try:
                    spec = importlib.util.spec_from_file_location(module_name, filepath)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # 遍历模块中的类
                    for name, cls in inspect.getmembers(module, inspect.isclass):
                        # 只导入定义在这个模块里的类（排除 import 的类）
                        if cls.__module__ == module_name:
                            self.functions[name] = cls()
                except Exception as e:
                    print(e)

    def function_list(self):
        re = ""
        for name, cls in self.functions.items():
            re += f"""
    函数名: {name}
    描述: {getattr(cls, "desc", "")}
    """
        if not re: 
            re = "无"
        return re 

    def function_call(self, name, args = None, kargs = None):
        # 根据函数名调用函数
        if args is None:
            args = []
        if kargs is None:
            kargs = {}
        if name in self.functions:
            try:
                result = self.functions[name](*args, **kargs)  # 调用函数
            except Exception as e:
                return e
            return result
        else:
            return f"函数 {name} 不存在"

if __name__ == "__main__":
    to = Tools()
    print(to.function_list())
    to.function_call("balance")