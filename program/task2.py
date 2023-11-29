#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def cylinder():
    """
    Вычисляет площадь цилиндра в зависимости от выбора пользователя.

    Функция спрашивает у пользователя какую площадь считать:
    только боковой поверхности или полную площадь цилиндра.
    При выборе полной площади вызывается дополнительно функция circle().
    """

    def circle(radius):
        """
        Вычисляет площадь круга по радиусу.

        Принимает радиус круга и возвращает площадь, используя формулу
        площади круга: pi * r^2.
        """
        return math.pi * radius ** 2

    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    side_area = 2 * math.pi * radius * height

    sw = True
    while sw:
        sw = False

        user_choice = input(
            "Введите 'боковая' для площади боковой поверхности" +
            " или 'полная' для полной площади цилиндра: "
        )

        match user_choice.lower():
            case 'боковая':
                print(f"Площадь боковой поверхности цилиндра: {side_area:.2f}")
            case 'полная':
                base_area = circle(radius)
                full_area = side_area + 2 * base_area
                print(f"Полная площадь цилиндра: {full_area:.2f}")
            case _:
                print(
                    "\n\nНеправильный ввод. Пожалуйста, введите 'боковая' или 'полная'.\n\n")
                sw = True


# Основная ветка программы
if __name__ == '__main__':
    cylinder()
