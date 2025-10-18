import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Union, List, Dict, Any
import numpy as np

class DataVisualizer:
    """数据可视化工具类"""
    
    def __init__(self):
        plt.style.use('seaborn')
        self.figsize = (10, 6)
    
    def line_plot(self, x_data: List, y_data: List, title: str = "折线图", 
                  xlabel: str = "X轴", ylabel: str = "Y轴") -> str:
        """创建折线图"""
        plt.figure(figsize=self.figsize)
        plt.plot(x_data, y_data, marker='o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('line_plot.png')
        plt.close()
        return "折线图已保存为 line_plot.png"
    
    def bar_chart(self, categories: List, values: List, title: str = "柱状图",
                  xlabel: str = "类别", ylabel: str = "数值") -> str:
        """创建柱状图"""
        plt.figure(figsize=self.figsize)
        plt.bar(categories, values, color='skyblue')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('bar_chart.png')
        plt.close()
        return "柱状图已保存为 bar_chart.png"
    
    def scatter_plot(self, x_data: List, y_data: List, title: str = "散点图",
                     xlabel: str = "X轴", ylabel: str = "Y轴") -> str:
        """创建散点图"""
        plt.figure(figsize=self.figsize)
        plt.scatter(x_data, y_data, alpha=0.7)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('scatter_plot.png')
        plt.close()
        return "散点图已保存为 scatter_plot.png"
    
    def histogram(self, data: List, bins: int = 10, title: str = "直方图",
                  xlabel: str = "数值", ylabel: str = "频数") -> str:
        """创建直方图"""
        plt.figure(figsize=self.figsize)
        plt.hist(data, bins=bins, alpha=0.7, edgecolor='black')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.tight_layout()
        plt.savefig('histogram.png')
        plt.close()
        return "直方图已保存为 histogram.png"
    
    def pie_chart(self, labels: List, sizes: List, title: str = "饼图") -> str:
        """创建饼图"""
        plt.figure(figsize=self.figsize)
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title(title)
        plt.tight_layout()
        plt.savefig('pie_chart.png')
        plt.close()
        return "饼图已保存为 pie_chart.png"
    
    def heatmap(self, data: Union[List, np.ndarray], title: str = "热力图",
                xlabels: List = None, ylabels: List = None) -> str:
        """创建热力图"""
        plt.figure(figsize=self.figsize)
        sns.heatmap(data, annot=True, fmt=".2f", cmap='YlOrRd',
                   xticklabels=xlabels, yticklabels=ylabels)
        plt.title(title)
        plt.tight_layout()
        plt.savefig('heatmap.png')
        plt.close()
        return "热力图已保存为 heatmap.png"

# 使用示例
if __name__ == "__main__":
    visualizer = DataVisualizer()
    
    # 示例数据
    x_data = [1, 2, 3, 4, 5]
    y_data = [2, 4, 6, 8, 10]
    categories = ['A', 'B', 'C', 'D']
    values = [10, 25, 15, 30]
    
    # 测试各种图表
    print(visualizer.line_plot(x_data, y_data))
    print(visualizer.bar_chart(categories, values))
    print(visualizer.scatter_plot(x_data, y_data))
    print(visualizer.histogram(y_data))
    print(visualizer.pie_chart(categories, values))