int_num = 50
float_num = 7.5

# print(int_num * float_num)

print(int_num.__mul__(float_num))
# NotImplemented: на уровне класса int не реализован
# метод умножения int на float

print(float_num.__rmul__(int_num))
# 375.0