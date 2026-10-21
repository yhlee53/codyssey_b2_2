"""우광택(yeri) 나머지 계산기 유틸"""


def modulo(a: float, b: float) -> float:
    """두 수를 나눈 나머지를 반환한다.

    >>> modulo(7, 3)
    1.0
    """
    if b == 0:
        raise ZeroDivisionError('0으로 나눌 수 없습니다.')
    return a % b


if __name__ == '__main__':
    print(modulo(7, 3))
