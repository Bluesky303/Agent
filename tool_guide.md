# 可用工具使用指南

## 1. file_reader
- **功能**: 读取指定路径的文件内容
- **参数**: file_path - 文件路径字符串
- **示例**: file_reader("example.txt")

## 2. balance
- **功能**: 查询模型剩余余额
- **参数**: 无
- **示例**: balance()

## 3. list_files
- **功能**: 列出指定目录下的文件和文件夹
- **参数**: directory_path - 目录路径字符串（默认为当前目录）
- **示例**: list_files("./") 或 list_files("/home/user")

## 4. file_writer
- **功能**: 写入内容到指定文件路径
- **参数**: 
  - file_path - 文件路径字符串
  - content - 要写入的内容字符串
- **示例**: file_writer("output.txt", "Hello World")