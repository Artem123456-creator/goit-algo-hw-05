def caching_fibonacci():
    cache = {}  # Створення порожнього словника для кешування результатів
    def fibonacci(n):
        # Врахування варіантів якщо n <= 0 та n = 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Перевірка, чи вже збережено значення для n у cache
        elif n in cache:
            return cache[n]
        else:
            # Обчислення числа Фібоначчі за допомогою рекурсії
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()
# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610