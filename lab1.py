#3 Вариант
import math

def task1():
    while True:
        print("---")
        print("Задание 1.")
        print("         |m + n**2, если m > 0, n < 0,\n" \
              "f(m,n) = |m + 2*n, если m <= 0, n < 0,;\n" \
              "         |m + 1 в остальных случаях.")
        m = input("Введите m: ")
        n = input("Введите n: ")
        try:
            m = int(m)
            n = int(n)
            if m > 0 and n < 0:
                result = m + n**2
            elif m <= 0 and n < 0:
                result = m + 2*n
            else:
                result = m + 1
            print(f"Ответ: {result}")
            break
        except ValueError:
            print("Ошибка: Вы ввели не число! Попробуйте еще раз.")
    print("---")

def task2():
    while True:
        print("---")
        print("Задание 2.")
        print("      \033[4mln(r) - cos(r^2)\033[0m\n" \
              "      sin^2(r) + tg(3r)\n" \
              "S = e")
        r = input("Введите r (положительное число): ")
        try:
            r = int(r)
            if r <= 0:
                print("Ошибка: r должно быть положительным числом для вычисления ln(r).") 
                continue
            S = math.exp((math.log(r) - math.cos(r**2)) / (math.sin(r)**2 + math.tan(3 * r)))
            print(f"Ответ: {S}")
            break
        except ValueError:
            print("Ошибка: Вы ввели не число! Попробуйте еще раз.")
    print("---")

def task3():
    while True:
        print("---")
        print("Задание 3.")
        print("Даны два целых числа. Если они оба четные, то большее из них поделить на 2;\n" \
              "если оба нечетные, каждое умножить на 2;\n" \
              "если числа разной четности, нечетное увеличить на 1.")
        a = input("Введите первое число: ")
        b = input("Введите второе число: ")
        try:
            a = int(a)
            b = int(b)
            if a % 2 == 0 and b % 2 == 0:
                print(f"Ответ: {max(a, b) // 2}, {min(a, b)}")
            elif a % 2 != 0 and b % 2 != 0:
                print(f"Ответ: {a * 2}, {b * 2}")
            elif a % 2 != 0 and b % 2 == 0:
                print(f"Ответ: {a + 1}, {b}")
            else:
                print(f"Ответ: {a}, {b + 1}")
            break
        except ValueError:
            print("Ошибка: Вы ввели не число! Попробуйте еще раз")
    print("---")

def task4():
    print("---")
    print("Задание 4.")
    print("Составить программу поиска двузначных чисел таких,\n" \
          "что если к сумме цифр числа прибавить квадрат\n" \
          "этой суммы, то получится это число")
    result = []
    for i in range(10, 100):
        sum = sum(int(digit) for digit in str(i))
        if i == sum + sum ** 2:
            result.append(i)
    print(f"Ответ: {str(result)[1:-1]}.")
    print("---")

def task5():
    while True:
        print("---")
        print("Задание 5.")
        print("Пусть A и B — положительные вещественные числа, большие 1, причем A > B.\n" \
              "Составить программу для поиска такого наименьшего\n" \
              "натурального m, что B**m > m*A.")
        m = 1
        a = input("Введите A: ")
        b = input("Введите B: ")
        try:
            a = float(a)
            b = float(b)
            if a > 1 and b > 1 and a > b:
                while True:
                    if b**m > m*a:
                        print(f"Ответ: {m}")
                        break
                    m += 1
                break
            else:
                print("Ошибка: Убедитесь, что A > 1, B > 1 и A > B. Попробуйте еще раз.")
        except ValueError:
            print("Ошибка: Вы ввели не число! Попробуйте еще раз")
    print("---")

def task6():
    while True:
        print("---")
        print("Задание 6.")
        print("Дано натуральное число n. Составить программу \n" \
              "для сравнения цифр старшего и младшего \n" \
              "разрядов этого числа.")
        n = input("Введите натуральное число: ")
        try:
            n = int(n)
            if n <= 0:
                print("Ошибка: Введите натуральное число.")
                continue
            last_digit = n % 10
            while n >= 10:
                n //= 10
            first_digit = n
            if first_digit > last_digit:
                print(f"Старший разряд ({first_digit}) больше младшего разряда ({last_digit}).")
            elif first_digit < last_digit:
                print(f"Старший разряд ({first_digit}) меньше младшего разряда ({last_digit}).")
            else:
                print(f"Старший разряд ({first_digit}) равен младшему разряду ({last_digit}).")
            break
        except ValueError:
            print("Ошибка: Вы ввели не число! Попробуйте еще раз.")
    print("---")

def task7():
    while True:
        print("---")
        print("Задание 7.")
        print("Вычислить значение суммы бесконечного ряда  S = 1 + x/1! + x^2/2! + ... + x^n/n!\n" \
              "с точностью до члена ряда, по модулю меньшего E = 10^-4,\n" \
              "и значение функции(для проверки) f=e^x,\n" \
              "учесть, что 1 <= x <= 2.")
        x = input("Введите значение x (1 <= x <= 2): ")
        try:
            x = float(x)
            if x < 1 or x > 2:
                print("Ошибка: x должно быть в диапазоне от 1 до 2.")
                continue
            S = 0
            n = 1
            term = 1
            E = 10**-4
            while abs(term) >= E:
                S += term
                term = (x ** n) / math.factorial(n)
                n += 1
            f = math.exp(x)
            print(f"Сумма ряда S = {S:.4f}")
            print(f"Значение функции f(x) = e^x = {f:.4f}")
            break
        except ValueError:
            print("Ошибка: Вы ввели не число! Попробуйте еще раз.")
    print("---")

def task8():
    while True:
        print("---")
        print("Задание 8.")
        print("Вычислить значение суммы бесконечного ряда  S = 2[1/x + 1/3x^3 + 1/5x^5 +...]\n" \
              "с заданной точностью E = 10^-5, и значение функции(для проверки)\n" \
              "y=ln((x+1)/(x-1)), учесть, что |x| > 1.")
        x = input("Введите значение x (|x| > 1): ")
        try:
            x = float(x)
            if abs(x) <= 1:
                print("Ошибка: |x| должно быть больше 1.")
                continue
            S = 0
            n = 1
            term = 1 / x
            E = 10**-5

            while abs(term) >= E:
                S += term
                n += 1
                term = (1 / (2 * n - 1)) * (1 / (x ** (2 * n - 1)))
            S = 2 * S
            y = math.log((x + 1) / (x - 1))
            print(f"Сумма ряда S = {S:.4f}")
            print(f"Значение функции y = ln((x + 1) / (x - 1)) = {y:.4f}")
            break
        except ValueError:
            print("Ошибка: Вы ввели не число! Попробуйте еще раз.")
    print("---")

def task9():
    while True:
        print("---")
        print("Задание 8.")
        print("Для каждого из 10 значений переменной x, изменяющейся от -b до b \n" \
              "с постоянным шагом, вычислить значение произведения \n" \
              "P = x*(x + 0,2)(x + 0,4)...*(x + 1,8).")
        b = input("Введите значение b: ")
        try:
            b = float(b)
            step = (2 * b) / 9
            for i in range(10):
                x = -b + i * step
                P = 1
                for i in range(10):
                    P *= (x + i * 0.2)
                print(f"x = {x:.2f}, P = {P:.4f}")
            break
        except ValueError:
            print("Ошибка: Вы ввели не число! Попробуйте еще раз.")
    print("---")

def main():
    while True:
        print("Выберите номер задания:")
        print("1. Задание 1")
        print("2. Задание 2")
        print("3. Задание 3")
        print("4. Задание 4")
        print("5. Задание 5")
        print("6. Задание 6")
        print("7. Задание 7")
        print("8. Задание 8")
        print("9. Задание 9")
        print("0. Выход")
        choice = input("Введите номер задания: ")
        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '6':
            task6()
        elif choice == '7':
            task7()
        elif choice == '8':
            task8()
        elif choice == '9':
            task9()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный ввод. Попробуйте еще раз.") 
            print("---")
main()