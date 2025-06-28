# 练习题 1
x = 10
y = "10"
z = True
print(f"x 的数据类型是: {type(x)}")  # 输出: <class 'int'>
print(f"y 的数据类型是: {type(y)}")  # 输出: <class 'str'>
print(f"z 的数据类型是: {type(z)}")  # 输出: <class 'bool'>

# 练习题 2
r = float(input("请输入圆的半径: "))
area = 3.14 * r ** 2
print(f"圆的面积是: {area}")

# 练习题 3
s = "3.14"
float_num = float(s)  # 转换为浮点数: 3.14
int_num = int(float_num)  # 转换为整数: 3 (直接截断小数部分)
print(f"字符串 '{s}' 转换为浮点数: {float_num}，再转换为整数: {int_num}")