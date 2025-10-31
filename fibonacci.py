def caching_fibonacci():
    cache = {}  # порожній словник 
    def fibonacci(n):   #внутрішня функція
        if n <= 0:
            return 0  
        if n == 1:
            return 1  
        if n in cache:
            return cache[n]  
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)   # інакше обчислюємо рекурсивно та зберігаємо у кеш
        return cache[n]

    return fibonacci

fib = caching_fibonacci() # Отримуємо функцію fibonacci

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

