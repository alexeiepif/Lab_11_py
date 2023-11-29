#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def multiply_numbers():
    """
    Функция считывает числа с клавиатуры и перемножает их до тех пор, пока не будет введен 0.
    
    Возвращает полученное произведение.
    """
    result = 1
    while True:
        number = int(input("Введите число:"))
        if number == 0:
            break
        result *= number
    return result

if __name__ == "__main__":
    result = multiply_numbers()
    print("Результат:", result)
