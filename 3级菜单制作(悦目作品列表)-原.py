import requests
from bs4 import BeautifulSoup
import time
import os
import logging
import re

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 监控的网页列表
# 监控的网页列表
urls = {
    "https://www.xsdixiao.com/1687.html": None,
    "https://www.xsdixiao.com/1835.html": None,
    "https://www.xsdixiao.com/1790.html": None,
    "https://www.xsdixiao.com/1717.html": None,
    "https://www.xsdixiao.com/1705.html": None,
    "https://www.xsdixiao.com/1636.html": None,
    "https://www.xsdixiao.com/1816.html": None,
    "https://www.xsdixiao.com/1640.html": None,
    "https://www.xsdixiao.com/1638.html": None,
    "https://www.xsdixiao.com/1632.html": None,
    "https://www.xsdixiao.com/1634.html": None,
    "https://www.xsdixiao.com/1652.html": None,
    "https://www.xsdixiao.com/1662.html": None,
    "https://www.xsdixiao.com/1719.html": None,
    "https://www.xsdixiao.com/1660.html": None,
    "https://www.xsdixiao.com/1834.html": None,
    "https://www.xsdixiao.com/1833.html": None,
    "https://www.xsdixiao.com/1831.html": None,
    "https://www.xsdixiao.com/1715.html": None,
    "https://www.xsdixiao.com/1669.html": None,
    "https://www.xsdixiao.com/1702.html": None,
    "https://www.xsdixiao.com/1697.html": None,
    "https://www.xsdixiao.com/1695.html": None,
    "https://www.xsdixiao.com/1644.html": None,
    "https://www.xsdixiao.com/1693.html": None,
    "https://www.xsdixiao.com/1671.html": None,
    "https://www.xsdixiao.com/1691.html": None,
    "https://www.xsdixiao.com/1642.html": None,
    "https://www.xsdixiao.com/1689.html": None,
    "https://www.xsdixiao.com/1685.html": None,
    "https://www.xsdixiao.com/1682.html": None,
    "https://www.xsdixiao.com/1680.html": None,
    "https://www.xsdixiao.com/1678.html": None,
    "https://www.xsdixiao.com/1675.html": None,
    "https://www.xsdixiao.com/1673.html": None,
    "https://www.xsdixiao.com/1667.html": None,
    "https://www.xsdixiao.com/1710.html": None,
    "https://www.xsdixiao.com/1665.html": None,
    "https://www.xsdixiao.com/1658.html": None,
    "https://www.xsdixiao.com/1656.html": None,
    "https://www.xsdixiao.com/1654.html": None,
    "https://www.xsdixiao.com/1650.html": None,
    "https://www.xsdixiao.com/1648.html": None,
    "https://www.xsdixiao.com/1646.html": None,
    "https://www.xsdixiao.com/1699.html": None
}

# 监控间隔（秒）
interval = 86400  # 一天

# 保存路径
save_path = r"C:\Users\Administrator\Desktop\详细目录"

# 确保保存路径存在
os.makedirs(save_path, exist_ok=True)

# 统一的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_page_title(url):
    """
    获取指定网页的标题
    :param url: 网页的 URL
    :return: 网页的标题
    """
    try:
        # 发送请求并设置超时时间
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        soup = BeautifulSoup(response.text, 'html.parser')
        # 提取网页标题
        title = soup.title.string if soup.title else "Untitled"
        return title
    except requests.RequestException as e:
        logging.error(f"请求异常: {e} - {url}")
        return None
    except Exception as e:
        logging.error(f"发生未知错误: {e} - {url}")
        return None

def sanitize_filename(filename):
    """
    去除文件名中的非法字符
    :param filename: 原始文件名
    :return: 合法的文件名
    """
    # 定义不合法字符的正则表达式
    invalid_chars = r'[\/:*?"<>|]'
    # 将不合法字符替换为 -
    return re.sub(invalid_chars, '-', filename)

def save_to_file(content, filename):
    """
    将内容保存到指定文件
    :param content: 要保存的内容
    :param filename: 保存的文件名
    """
    # 处理文件名
    safe_filename = sanitize_filename(filename)
    full_path = os.path.join(save_path, f"{safe_filename}.txt")
    try:
        with open(full_path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        logging.info(f"内容已保存到 {full_path}")
    except PermissionError:
        logging.error(f"没有权限保存文件: {full_path}")
    except Exception as e:
        logging.error(f"保存文件时出错: {e} - {full_path}")

def monitor_pages(urls, interval, save_path):
    """
    监控指定网页的内容变化
    :param urls: 网页 URL 与保存文件名的映射字典
    :param interval: 监控间隔时间（秒）
    :param save_path: 保存文件的路径
    """
    while True:
        for url, title in urls.items():
            if title is None:
                title = get_page_title(url)
                if title:
                    urls[url] = title
            if title:
                content = get_page_content(url)
                if content:
                    save_to_file(content, title)
        logging.info(f"完成一轮监控，等待 {interval} 秒后进行下一轮监控。")
        time.sleep(interval)

def get_page_content(url):
    """
    获取指定网页的内容
    :param url: 网页的 URL
    :return: 网页内容
    """
    try:
        # 发送请求并设置超时时间
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        soup = BeautifulSoup(response.text, 'html.parser')
        # 查找 <div class="entry-content"> 标签
        entry_content = soup.find('div', class_='entry-content')
        if entry_content:
            # 将 <br> 标签替换为换行符
            for br in entry_content.find_all('br'):
                br.replace_with('\n')

            # 提取所有 <p> 标签的文本内容
            p_contents = []
            for p in entry_content.find_all('p'):
                p_text = p.get_text()
                # 保留原有的换行符
                p_contents.append(p_text)
            return '\n'.join(p_contents)
        else:
            logging.warning(f"未找到 <div class='entry-content'> 标签: {url}")
            return ""
    except requests.RequestException as e:
        logging.error(f"请求异常: {e} - {url}")
        return None
    except Exception as e:
        logging.error(f"发生未知错误: {e} - {url}")
        return None

if __name__ == "__main__":
    monitor_pages(urls, interval, save_path)