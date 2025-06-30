import requests
from lxml import etree
import os
from urllib.parse import urljoin  # 用于正确拼接URL


def download_images():
    # 目标网站URL
    url = "http://pic.netbian.com/"

    # 创建保存图片的目录
    save_dir = r'd:\images'
    os.makedirs(save_dir, exist_ok=True)  # 自动创建目录

    try:
        # 1. 获取网页内容
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        response.encoding = 'gbk'

        # 2. 解析图片链接
        html = etree.HTML(response.text)
        img_srcs = html.xpath("//ul[@class='clearfix']/li/a/span/img/@src")

        if not img_srcs:
            print("警告：未找到任何图片链接")
            return

        print(f"共找到 {len(img_srcs)} 张图片")

        # 3. 下载图片
        for i, src in enumerate(img_srcs, 1):
            try:
                # 正确拼接URL（处理相对路径）
                img_url = urljoin(url, src)

                # 获取图片
                img_response = requests.get(img_url, headers=headers, timeout=10)
                img_response.raise_for_status()

                # 提取文件名
                file_name = os.path.basename(src)
                if not file_name:  # 如果无法提取文件名
                    file_name = f"image_{i}.jpg"

                # 保存图片
                save_path = os.path.join(save_dir, file_name)
                with open(save_path, 'wb') as f:
                    f.write(img_response.content)

                print(f"已下载 {i}/{len(img_srcs)}: {file_name}")

            except Exception as e:
                print(f"下载第 {i} 张图片失败: {e}")
                continue

        print("所有图片下载完成！")

    except requests.exceptions.RequestException as e:
        print(f"网络请求失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    download_images()