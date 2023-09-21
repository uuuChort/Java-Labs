def alternating_sum(n, numbers):
    result = 0
    for i in range(n):
        if i % 2 == 0:
            result += numbers[i]
        else:
            result -= numbers[i]
    return result

#счет данных с клавы
n = int(input("Введите количество чисел (n): "))
numbers = []
for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)

#вление знакочередующейся суммы
result_sum = alternating_sum(n, numbers)

#ввод результата
print("Знакочередующаяся сумма ряда:", result_sum)
