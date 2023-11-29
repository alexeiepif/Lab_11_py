#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    """
    Функция запрашивает ввод с клавиатуры и возвращает введенную строку.
    """
    return input("Введите значение: ")


def test_input(value):
    """
    Функция проверяет, можно ли преобразовать переданное значение в целое число.

    Возвращает True, если преобразование возможно, иначе False.
    """
    return value.isdigit()


def str_to_int(value):
    """
    Функция преобразовывает переданное значение в целочисленный тип.

    Возвращает полученное число.
    """
    return int(value)


def print_int(value):
    """
    Функция выводит переданное значение на экран.
    """
    print(value)


if __name__ == "__main__":
    input_value = get_input()

    if test_input(input_value):
        int_value = str_to_int(input_value)
        print_int(int_value)
    else:
        print("Значение не может быть преобразовано в целое число")
