# 1. 判断回文数
def is_palindrome(num):
    """判断一个数是否为回文数"""
    num_str = str(num)
    return num_str == num_str[::-1]

print(is_palindrome(121))  # True
print(is_palindrome(123))  # False

# 2. 计算任意数量参数的平均值
def average(*args):
    """计算任意数量参数的平均值"""
    return sum(args) / len(args) if args else 0

print(average(1, 2, 3, 4))  # 2.5
print(average(10, 20))      # 15.0

# 3. 返回最长的字符串
def longest_string(*strings):
    return max(strings, key=len, default=None)

print(longest_string("apple", "banana", "orange"))  # "banana"
print(longest_string("a", "bb", "ccc"))            # "ccc"

# 4. 创建模块并导入使用
# 直接在同一个文件中定义和使用
def area(length, width):
    return length * width
def perimeter(length, width):
    return 2 * (length + width)
print("面积:", area(5, 3))
print("周长:", perimeter(5, 3))