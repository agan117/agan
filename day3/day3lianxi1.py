import requests
from bs4 import BeautifulSoup

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = "https://movie.douban.com/chart"

try:
    # 发送请求获取网页内容
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功

    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取前10个电影名称
    print("豆瓣电影排行榜Top10：")
    movies = soup.select('.pl2 a')[:10]  # 选择前10个电影链接
    for i, movie in enumerate(movies, 1):
        # 去除名称中的空格和换行符，并提取纯文本
        name = movie.text.strip().replace('\n', '').replace(' ', '')
        print(f"{i}. {name}")

except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except Exception as e:
    print(f"发生错误: {e}")