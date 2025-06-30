import time
import random
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from typing import Optional, Dict, List


class ScholarCitationFetcher:
    """Google Scholar文献引用获取器"""

    def __init__(self):
        self.driver = self._setup_browser()
        self.wait = WebDriverWait(self.driver, 15)

    def _setup_browser(self) -> webdriver.Chrome:
        """配置Chrome浏览器"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def _human_type(self, element, text: str):
        """模拟人类输入"""
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.05, 0.15))

    def search_scholar(self, query: str) -> bool:
        """在Google Scholar中搜索文献"""
        try:
            print(f"\n🔍 正在搜索: {query}")
            self.driver.get("https://scholar.google.com")
            time.sleep(2)

            # 切换到英文界面确保结果准确
            try:
                self.wait.until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "English"))
                ).click()
                time.sleep(1)
            except:
                pass

            search_box = self.wait.until(
                EC.element_to_be_clickable((By.NAME, "q"))
            )
            search_box.clear()
            self._human_type(search_box, query)
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            return True
        except Exception as e:
            print(f"搜索失败: {str(e)}")
            return False

    def get_bibtex(self) -> Optional[str]:
        """获取BibTeX引用"""
        try:
            # 定位第一篇结果的引用按钮
            first_result = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.gs_ri"))
            )
            cite_btn = first_result.find_element(By.CSS_SELECTOR, "a.gs_or_cit")
            article_title = first_result.find_element(By.CSS_SELECTOR, "h3").text
            print(f"📄 找到文献: {article_title}")

            cite_btn.click()
            time.sleep(2)

            # 选择BibTeX格式
            self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "BibTeX"))
            ).click()
            time.sleep(2)

            # 获取BibTeX内容
            bibtex = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "pre"))
            ).text

            print("\n✅ BibTeX获取成功")
            return bibtex.strip()

        except Exception as e:
            print(f"获取BibTeX失败: {str(e)}")
            return None

    def process_article(self, title: str) -> Optional[str]:
        """处理单篇文章"""
        if not self.search_scholar(title):
            return None

        try:
            citation = self.get_bibtex()
            if citation:
                try:
                    pyperclip.copy(citation)
                    print("(已复制到剪贴板)")
                except:
                    pass
            return citation
        except Exception as e:
            print(f"处理文献失败: {str(e)}")
            return None

    def batch_process(self, titles: List[str]) -> Dict[str, str]:
        """批量处理文献"""
        results = {}
        for title in titles:
            print(f"\n{'=' * 50}\n处理文献: {title}\n{'=' * 50}")
            citation = self.process_article(title)
            results[title] = citation if citation else "获取失败"
            time.sleep(random.randint(3, 7))  # 随机延迟避免封禁
        return results

    def __del__(self):
        if hasattr(self, 'driver'):
            self.driver.quit()


def main():
    """主函数"""
    fetcher = ScholarCitationFetcher()

    # 文献列表
    articles = [
        "Deep learning based systems for crater detection: A review",
        "Attention is all you need",
        "You only look once: Unified, real-time object detection"
    ]

    try:
        # 批量处理并打印结果
        results = fetcher.batch_process(articles)

        print("\n\n=== 最终结果 ===")
        for title, citation in results.items():
            print(f"\n文献: {title}")
            print("-" * 60)
            print(citation)

    except KeyboardInterrupt:
        print("\n用户中断操作")
    finally:
        input("\n按回车键退出程序...")


if __name__ == "__main__":
    main()