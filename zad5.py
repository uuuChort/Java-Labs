class TwiceEvenNumber:
    def __init__(self):
        self.number = None

    def input_number(self):
        while True:
            try:
                self.number = int(input("Введите трехзначное положительное число: "))
                if 100 <= self.number <= 999:
                    break
                else:
                    print("Число должно быть трехзначным!")
            except ValueError:
                print("Введите корректное целое число!")

    def is_twice_even(self):
        #проверка суммы на четность
        digit_sum = sum(int(digit) for digit in str(self.number))
        is_digit_sum_even = digit_sum % 2 == 0

        #проверка произведения на четность
        digit_product = 1
        for digit in str(self.number):
            digit_product *= int(digit)
        is_digit_product_even = digit_product % 2 == 0

        return is_digit_sum_even and is_digit_product_even


#создание обЪекта класса и прооверка на число
twice_even_checker = TwiceEvenNumber()
twice_even_checker.input_number()
is_twice_even = twice_even_checker.is_twice_even()

if is_twice_even:
    print("Число является дважды четным.")
else:
    print("Число не является дважды четным.")

