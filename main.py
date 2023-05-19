import random

# Создаем списки A и B по 12 элементов
A = [random.randint(1, 100) for i in range(12)]
B = [random.randint(1, 100) for i in range(12)]

# Создаем список C по правилу c[i]=max(a[i],b[i])
C = [max(A[i], B[i]) for i in range(12)]

# Выводим списки A, B и C
print("Список A: ", A)
print("Список B: ", B)
print("Список C: ", C)

