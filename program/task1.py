#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    """
    Запросить число и вызвать соответствующую функцию.
    
    Вызывается positive() если число положительное.
    Вызывается negative() усли отрицательное.
    Возвращает None если == 0.
    """
    number = int(input("Введите целое число: "))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        return


def positive():
    """
    Вывести на экран 'Положительное'.
    """
    print("Положительное")


def negative():
    """
    Вывести на экран 'Отрицательное'.
    """
    print("Отрицательное")


if __name__ == '__main__':
    test()
