# 1. 定义Car类
class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand  # 品牌
        self.speed = speed  # 速度

    def accelerate(self, m):
        """加速方法，速度增加m次，每次增加10"""
        self.speed += 10 * m
        return self

    def brake(self, n):
        """刹车方法，速度减少n次，每次减少10，不低于0"""
        self.speed = max(0, self.speed - 10 * n)
        return self

    def __str__(self):
        return f"{self.brand}当前速度: {self.speed}"


# 2. 创建Car实例并测试
my_car = Car("Xiaomi")
print(my_car)  # 初始速度

my_car.accelerate(3)  # 加速3次
print(my_car)  # 加速后速度

my_car.brake(2)  # 刹车2次
print(my_car)  # 刹车后速度


# 3. 定义ElectricCar子类
class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        super().__init__(brand, speed)
        self.battery = battery  # 电量

    def charge(self):
        """充电方法，电量增加20，不超过100"""
        self.battery = min(100, self.battery + 20)
        return self

    def __str__(self):
        return f"{super().__str__()}，当前电量: {self.battery}%"


# 测试ElectricCar
my_electric = ElectricCar("Tesla")
print(my_electric)  # 初始状态

my_electric.accelerate(2).charge()  # 加速2次并充电
print(my_electric)  # 操作后状态

my_electric.brake(1).charge()  # 刹车1次并充电
print(my_electric)  # 最终状态