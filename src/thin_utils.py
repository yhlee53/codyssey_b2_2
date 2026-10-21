"""이경희(thin) 덧셈 계산기 유틸"""


def add(a: float, b: float) -> float:
    """두 수의 합을 반환한다.

    >>> add(2, 3)
    5.0
    """
    return a + b


if __name__ == '__main__':
    print(add(2, 3))
