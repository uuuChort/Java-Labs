def collatz_steps(n):
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps

#использования функции
start_number = 27  #стартовое число
steps_to_one = collatz_steps(start_number)
print(f"Для числа {start_number} потребовалось {steps_to_one} шагов, чтобы достичь 1")
