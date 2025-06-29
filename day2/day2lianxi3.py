import os
import re
import shutil
from pathlib import Path


def natural_sort_key(s):
    """实现特定排序规则：数字按自然���序，但带前导零的数字排在相同值的数字之前"""
    def convert(text):
        if text.isdigit():
            num_val = int(text)
            # 如果是以0开头的数字，返回一个特殊的元组使其排在普通数字之前
            if text.startswith('0') and len(text) > 1:
                return (num_val - 0.5, text)
            return (num_val, text)
        return text.lower()

    return [convert(p) for p in re.split('([0-9]+)', s)]


def rename_images_with_natural_order():
    """按自然排序顺序重命名图片"""
    try:
        # 1. 读取名字文件
        names_file = input("请输入名字文本文件路径（如：名字.txt）: ").strip()
        with open(names_file, 'r', encoding='utf-8') as f:
            names = [line.strip() for line in f if line.strip()]

        # 2. 获取图片文件夹并按自然排序
        images_folder = input("请输入图片文件夹路径: ").strip()
        image_files = [
            f for f in os.listdir(images_folder)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))
        ]

        # 关键步骤：按自然排序算法排序
        image_files.sort(key=natural_sort_key)

        # 3. 检查数量并自动处理
        if len(names) < len(image_files):
            names += [f'未命名{i + 1}' for i in range(len(names), len(image_files))]
            print(f"提示：已自动补充 {len(image_files) - len(names)} 个未命名项")
        elif len(names) > len(image_files):
            names = names[:len(image_files)]
            print(f"提示：已截断 {len(names) - len(image_files)} 个多余名字")

        # 4. 预览匹配结果
        print("\n当前匹配关系：")
        for i, (name, img) in enumerate(zip(names, image_files), 1):
            print(f"{i}. {img} → {name}{os.path.splitext(img)[1]}")

        # 5. 执行重命名
        output_dir = Path.home() / "Desktop" / "SortedRenamed"
        os.makedirs(output_dir, exist_ok=True)

        success = 0
        for name, img in zip(names, image_files):
            try:
                ext = os.path.splitext(img)[1]
                safe_name = "".join(c for c in name if c not in '\\/:*?"<>|').strip()
                new_name = f"{safe_name}{ext}"

                shutil.copy2(
                    os.path.join(images_folder, img),
                    os.path.join(output_dir, new_name)
                )
                success += 1
            except Exception as e:
                print(f"错误：处理 {img} 时出错 - {str(e)}")

        print(f"\n完成！成功处理 {success}/{len(image_files)} 个文件")
        print(f"结果保存在：{output_dir}")

    except Exception as e:
        print(f"发生错误：{str(e)}")
    finally:
        input("按Enter键退出...")


if __name__ == "__main__":
    rename_images_with_natural_order()