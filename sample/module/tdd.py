#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""TDD練習用関数モジュール
"""


def fizzbuzz(number: int):
    """数値に対応して 'Fizz', 'Buzz', 'FizzBuzz' いずれかの文字列を戻す

    numberの値に応じて、下記の文字列を戻します。
    - 3の倍数 -> 'Fizz'を表示
    - 5の倍数 -> 'Buzz'を表示
    - 3の倍数 or 5の倍数 -> 'FizzBuzz'を表示
    - それ以外 -> numberを文字列として表示

    Args:
        number (int): 文字列を表示する条件に用いる数値

    Returns:
        string: 関数説明で記載している文字列が戻されます

    Examples:
        >>> print(fizzbuzz(1))
        1
        >>> print(fizzbuzz(3))
        Fizz
        >>> print(fizzbuzz(5))
        Buzz
        >>> print(fizzbuzz(15))
        FizzBuzz
    """
    pass
