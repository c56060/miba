import requests
from bs4 import BeautifulSoup
import os
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 目标网页URL列表
urls = [
    "https://www.vmiba.com/bzhan-up",
    "https://www.vmiba.com/bzhan-up/page/2",
    "https://www.vmiba.com/bzhan-up/page/3",
    "https://www.vmiba.com/bzhan-up/page/4",
    "https://www.vmiba.com/bzhan-up/page/5"
    "https://www.vmiba.com/weme",
    "https://www.vmiba.com/weme/page/2",
    "https://www.vmiba.com/weme/page/3",
    "https://www.vmiba.com/weme/page/4",
    "https://www.vmiba.com/weme/page/5",
    "https://www.vmiba.com/weme/page/6",
    "https://www.vmiba.com/weme/page/7",
    "https://www.vmiba.com/weme/page/8",
    "https://www.vmiba.com/weme/page/9",
    "https://www.vmiba.com/weme/page/10",
    "https://www.vmiba.com/weme/page/11",
    "https://www.vmiba.com/weme/page/12",
    "https://www.vmiba.com/weme/page/13",
    "https://www.vmiba.com/weme/page/14",
    "https://www.vmiba.com/weme/page/15",
    "https://www.vmiba.com/weme/page/16",
    "https://www.vmiba.com/weme/page/17",
    "https://www.vmiba.com/weme/page/18",
    "https://www.vmiba.com/weme/page/19",
    "https://www.vmiba.com/weme/page/20",
    "https://www.vmiba.com/weme/page/21",
    "https://www.vmiba.com/weme/page/22",
    "https://www.vmiba.com/weme/page/23",
    "https://www.vmiba.com/weme/page/24",
    "https://www.vmiba.com/weme/page/25",
    "https://www.vmiba.com/weme/page/26",
    "https://www.vmiba.com/weme/page/27",
    "https://www.vmiba.com/weme/page/28",
    "https://www.vmiba.com/weme/page/29",
    "https://www.vmiba.com/weme/page/30",
    "https://www.vmiba.com/weme/page/31",
    "https://www.vmiba.com/weme/page/32",
    "https://www.vmiba.com/weme/page/33",
    "https://www.vmiba.com/weme/page/34",
    "https://www.vmiba.com/weme/page/35",
    "https://www.vmiba.com/weme/page/36",
    "https://www.vmiba.com/weme/page/37",
    "https://www.vmiba.com/weme/page/38",
    "https://www.vmiba.com/weme/page/39",
    "https://www.vmiba.com/weme/page/40",
    "https://www.vmiba.com/weme/page/41",
    "https://www.vmiba.com/weme/page/42",
    "https://www.vmiba.com/zbrw",
    "https://www.vmiba.com/zbrw/page/2",
    "https://www.vmiba.com/zbrw/page/3",
    "https://www.vmiba.com/cdhs",
    "https://www.vmiba.com/weibo",
    "https://www.vmiba.com/weibo/page/2",
    "https://www.vmiba.com/weibo/page/3",
    "https://www.vmiba.com/weibo/page/4",
    "https://www.vmiba.com/weibo/page/5",
    "https://www.vmiba.com/weibo/page/6",
    "https://www.vmiba.com/scj"
    "https://www.vmiba.com/scj/page2",
]

# 保存路径
save_path = r"C:\Users\Administrator\Desktop\作品名称"
os.makedirs(save_path, exist_ok=True)

def extract_links(url):
    """
    从指定网页中提取所有 <h3 itemprop="name headline"> 标签下的网址
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        h3_tags = soup.find_all('h3', itemprop="name headline")
        
        links = [tag.find('a')['href'] for tag in h3_tags if tag.find('a')]
        
        return links

    except requests.RequestException as e:
        logging.error(f"请求异常: {e} - {url}")
        return []
    except Exception as e:
        logging.error(f"发生未知错误: {e} - {url}")
        return []

def save_to_file(content, filename):
    """
    保存内容到txt文件
    """
    filepath = os.path.join(save_path, filename)
    try:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        logging.info(f"内容已保存到 {filepath}")
    except Exception as e:
        logging.error(f"保存文件时出错: {e} - {filepath}")

def main():
    all_links = []
    for i, url in enumerate(urls, 1):  # 从1开始计数页面
        links = extract_links(url)
        all_links.extend(links)
        all_links.append(f"\n--- Page {i} End ---\n")  # 添加换行标记

    # 提取第一个页面的标题作为文件名
    soup = BeautifulSoup(requests.get(urls[0], timeout=10).text, 'html.parser')
    title = soup.find('title').get_text(strip=True)
    filename = f"{title}.txt"
    save_to_file('\n'.join(all_links), filename)

if __name__ == "__main__":
    main()
