"""Задание состоит из двух частей:
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

Вариант 4:
Дан одномерный массив. Сформировать все возможные варианты данного массива путем замены отрицательных элементов на нечетных местах модулями.

Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода.

Ограничение: максимальная сумма элементов массива не должна превышать некоторое число .
Целевая функция: вывести массив с максимальной  суммой элементов , не превышая данное ограничение."""

import itertools
import copy
from random import randint

class Array:
    def __init__(self, n,max_sum):
        if n <= 0:
            raise ValueError("Размер массива должен быть больше 0")

        self.n = n

        self.max_sum = max_sum
        self.arr = self.generate_array()

    def generate_array(self):
        arr = [0] * self.n
        for i in range(self.n):
            arr[i] = randint(-100, 0)
        return arr

    def variants(self):
        if self.max_sum < sum(x for x in self.arr if x > 0):
            raise ValueError("Максимальная сумма не может быть меньше суммы положительных элементов")

        variants = []
        negative_indices = [i for i in range(0, len(self.arr), 2) if self.arr[i] < 0]

        for i in range(len(negative_indices) + 1):
            for combination in itertools.combinations(negative_indices, i):
                variant = copy.deepcopy(self.arr)
                for index in combination:
                    variant[index] = abs(variant[index])

                # Проверка на соответствие максимальной сумме
                if sum(variant) <= self.max_sum:
                    print(f"Полученный вариант: {variant}, сумма элементов: {sum(variant)}")
                    variants.append(variant)

        # Находим вариант с максимальной суммой элементов
        best_variant = max(variants[::-1], key=sum)
        return best_variant


n = int(input("Введите размер массива: "))

max_sum = int(input("Введите максимальную сумму элементов массива : "))
array_manipulator = Array(n, max_sum)
best_variant = array_manipulator.variants()

print(f"Массив с максимальной суммой элементов,не превышающей заданное ограничение: {best_variant}, сумма элементов: {sum(best_variant)}")
