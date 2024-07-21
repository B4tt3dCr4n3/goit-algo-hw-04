"""Python має дві вбудовані функції сортування: sorted і sort. Функції сортування 
Python використовують Timsort — гібридний алгоритм сортування, що поєднує в собі 
сортування злиттям і сортування вставками.

Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом 
виконання. Аналіз повинен бути підтверджений емпіричними даними, отриманими 
шляхом тестування алгоритмів на різних наборах даних. Емпірично перевірте 
теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах. 
Для заміру часу виконання алгоритмів використовуйте модуль timeit.

Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм 
Timsort набагато ефективнішим, і саме з цієї причини програмісти, в більшості 
випадків, використовують вбудовані в Python алгоритми, а не кодують самі. Зробіть висновки."""

import random
import timeit
import pandas as pd

# Функція для генерації випадкових масивів
def generate_random_array(size):
    return [random.randint(0, size) for _ in range(size)]

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Знаходимо середину масиву
        L = arr[:mid]  # Ліва половина
        R = arr[mid:]  # Права половина

        merge_sort(L)  # Рекурсивне сортування лівої половини
        merge_sort(R)  # Рекурсивне сортування правої половини

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Перевірка наявності залишкових елементів
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для вимірювання часу виконання
def measure_time(func, data):
    start_time = timeit.default_timer()
    func(data)
    return timeit.default_timer() - start_time

# Випробування алгоритмів
array_sizes = [1000, 2000, 5000, 10000, 20000]
results = []

for size in array_sizes:
    data = generate_random_array(size)  # Генерація випадкового масиву
    merge_sort_time = measure_time(merge_sort, data.copy())  # Час сортування злиттям
    insertion_sort_time = measure_time(insertion_sort, data.copy())  # Час сортування вставками
    timsort_time = measure_time(lambda arr: sorted(arr), data.copy())  # Час Timsort
    
    results.append({
        "Розмір": size,
        "Сортування злиттям": merge_sort_time,
        "Сортування вставками": insertion_sort_time,
        "Timsort": timsort_time
    })

df = pd.DataFrame(results)
print(df)
