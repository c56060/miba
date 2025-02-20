import requests
from bs4 import BeautifulSoup
import os

# 目标网页URL列表
urls = [
    "https://www.xsdixiao.com/xrqx",
    "https://www.xsdixiao.com/xrqx/page/2"

    
    
    
    
    
    
    
    
    
    
    # 添加更多URL
]

# 保存路径
save_path = r"C:\Users\Administrator\Desktop\作品链接"
os.makedirs(save_path, exist_ok=True)  # 确保保存路径存在，如果不存在则创建

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

for url in urls:
    try:
        # 发送HTTP请求获取网页内容
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 确保请求成功

        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取网页标题作为文件名
        title = soup.find('title').text.strip()
        # 替换文件名中不合法的字符
        title = ''.join([c for c in title if c.isalnum() or c in (' ', '_')]).rstrip()
        filename = f"{title}.txt"
        filepath = os.path.join(save_path, filename)

        # 查找所有的列表项<li>，这些列表项包含了我们想要的链接
        list_items = soup.find_all('li', class_='post-list-item item-post-style-1')

        # 提取每个列表项中的链接和对应的文本
        with open(filepath, 'w', encoding='utf-8') as file:
            for item in list_items:
                a_tag = item.find('h2').find('a')  # 根据你的HTML结构，链接在<h2>标签内的<a>标签中
                if a_tag and a_tag.has_attr('href'):
                    link = a_tag['href']
                    text = a_tag.get_text().strip()
                    file.write(f"{link}\t{text}\n")  # 每个链接和文本后添加换行符

        print(f"链接和文本已保存到 {filepath}")
    except requests.RequestException as e:
        print(f"请求错误: {e} - {url}")
    except Exception as e:
        print(f"处理URL时发生错误: {e} - {url}")