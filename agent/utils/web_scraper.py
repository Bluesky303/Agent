import requests
from bs4 import BeautifulSoup
import time

class WebScraper:
    def __init__(self, delay=1):
        self.delay = delay
        self.session = requests.Session()
        
    def scrape_url(self, url, parser='html.parser'):
        """
        爬取指定URL的内容
        
        Args:
            url (str): 要爬取的URL
            parser (str): BeautifulSoup解析器，默认使用'html.parser'
            
        Returns:
            dict: 包含爬取结果的字典
        """
        try:
            # 添加延迟避免频繁请求
            time.sleep(self.delay)
            
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, parser)
            
            # 提取基本信息
            result = {
                'url': url,
                'status_code': response.status_code,
                'title': soup.title.string if soup.title else None,
                'text_content': soup.get_text(separator=' ', strip=True),
                'links': [link.get('href') for link in soup.find_all('a') if link.get('href')],
                'images': [img.get('src') for img in soup.find_all('img') if img.get('src')]
            }
            
            return result
            
        except requests.exceptions.RequestException as e:
            return {
                'url': url,
                'error': f"请求失败: {str(e)}",
                'status_code': None
            }
        except Exception as e:
            return {
                'url': url,
                'error': f"解析失败: {str(e)}",
                'status_code': None
            }
    
    def scrape_multiple_urls(self, urls, parser='html.parser'):
        """
        批量爬取多个URL
        
        Args:
            urls (list): URL列表
            parser (str): BeautifulSoup解析器
            
        Returns:
            list: 包含所有URL爬取结果的列表
        """
        results = []
        for url in urls:
            result = self.scrape_url(url, parser)
            results.append(result)
        return results

# 使用示例
if __name__ == "__main__":
    scraper = WebScraper()
    
    # 单个URL爬取示例
    result = scraper.scrape_url("https://example.com")
    print(result)
    
    # 多个URL爬取示例
    urls = ["https://example.com", "https://example.org"]
    results = scraper.scrape_multiple_urls(urls)
    print(results)