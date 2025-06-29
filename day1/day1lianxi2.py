# 练习题 1: 输出1到100之间的所有素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("1到100之间的素数:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")

# 练习题 2: 计算斐波那契数列的前20项
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

fib_20 = fibonacci(20)
print("\n斐波那契数列前20项:")
print(fib_20)

# 练习题 3: 计算1-10000之间能被3或5整除且不能被15整除的数的和
total = 0
num = 1
while num <= 10000:
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        total += num
    num += 1
print("满足条件的数的和:", total)