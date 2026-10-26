"""함선우(bal) 뺄셈 계산기 유틸"""


def subtract(a: float, b: float) -> float:
    """두 수의 차를 반환한다.

    >>> subtract(5, 3)
    2
    >>> subtract(5.0, 3.0)
    2.0
    """
    return a - b


if __name__ == '__main__':
    print(subtract(5, 3))
