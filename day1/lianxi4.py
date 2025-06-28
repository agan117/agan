# 1. 给定字符串 s1
s1 = "Python is a powerful programming language"
s2 = "Let's learn together"

# (1) 提取单词 "language"
words = s1.split()
print("最后一个单词:", words[-1])  # 输出: language

# (2) 连接s1和s2并重复输出3次
combined = s1 + " " + s2
print((combined + "\n") * 3)  # 重复3次，每次换行

# (3) 输出所有以p或P开头的单词
p_words = [word for word in words if word.lower().startswith('p')]
print("以p或P开头的单词:", p_words)  # 输出: ['Python', 'powerful', 'programming']

# 2. 对字符串s3进行操作
s3 = "Hello, World! This is a test string. "

# (1) 去除字符串前后的空格
s3_stripped = s3.strip()
print("去除空格后:", f"'{s3_stripped}'")  # 输出: 'Hello, World! This is a test string.'

# (2) 将所有字符转换为大写
s3_upper = s3_stripped.upper()
print("大写转换:", s3_upper)  # 输出: HELLO, WORLD! THIS IS A TEST STRING.

# (3) 查找子串"test"的起始下标
test_index = s3_stripped.find("test")
print("'test'的起始下标:", test_index)  # 输出: 21

# (4) 将"test"替换为"practice"
s3_replaced = s3_stripped.replace("test", "practice")
print("替换后:", s3_replaced)  # 输出: Hello, World! This is a practice string.

# (5) 分割并连接字符串
s3_split = s3_stripped.split()
s3_joined = "-".join(s3_split)
print("分割并连接:", s3_joined)  # 输出: Hello,-World!-This-is-a-test-string.