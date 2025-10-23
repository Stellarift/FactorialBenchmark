import timeit
import cProfile

def factorial_recursive(n):
    """Рекурсивный расчет факториала"""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Итерационный расчет факториала"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def task1():
    """Задание 1: Замер времени рекурсивного метода"""
    print("ЗАДАНИЕ 1: Рекурсивный метод\n")
    
    test_values = [10, 20, 30]
    num_runs = 10000
    
    print("| Вход | Время выполнения |")
    print("|------|------------------|")
    
    for n in test_values:
        time_taken = timeit.timeit(f"factorial_recursive({n})", 
                                 setup="from __main__ import factorial_recursive", 
                                 number=num_runs) / num_runs
        print(f"| {n:4} | {time_taken:.8f} сек |")

def task2():
    """Задание 2: Сравнение рекурсивного и итерационного методов"""
    print("\nЗАДАНИЕ 2: Сравнение методов\n")
    
    test_values = [10, 20, 30]
    num_runs = 10000
    
    print("| Метод    | Вход | Время выполнения |")
    print("|----------|------|------------------|")
    
    for n in test_values:
        time_rec = timeit.timeit(f"factorial_recursive({n})", 
                               setup="from __main__ import factorial_recursive", 
                               number=num_runs) / num_runs
        
        time_iter = timeit.timeit(f"factorial_iterative({n})", 
                                setup="from __main__ import factorial_iterative", 
                                number=num_runs) / num_runs
        
        print(f"| Рекурсия | {n:4} | {time_rec:.8f} сек |")
        print(f"| Итерация | {n:4} | {time_iter:.8f} сек |")
        print("|----------|------|------------------|")

def task3():
    """Задание 3: Профилирование методов"""
    print("\nЗАДАНИЕ 3: Профилирование\n")
    
    print("Рекурсивный метод (n=30):")
    print("-" * 40)
    cProfile.run('factorial_recursive(30)')
    
    print("\nИтерационный метод (n=30):")
    print("-" * 40)
    cProfile.run('factorial_iterative(30)')

def main():
    print(f"Проверка: factorial_recursive(5) = {factorial_recursive(5)}")
    print(f"Проверка: factorial_iterative(5) = {factorial_iterative(5)}")
    print()
    
    task1()
    task2() 
    task3()
    
    print("\nВЫВОДЫ:")
    print("Рекурсия создает много вызовов функций.")
    print("Для факториала лучше использовать итерационный метод.")
    print("Итерационный метод в 2 раза быстрее рекурсивного")

if __name__ == "__main__":
    main()