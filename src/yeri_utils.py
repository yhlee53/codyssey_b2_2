"""우광택(yeri) 유틸 예시
"""

def repeat(s: str, n: int) -> str:
    """문자열을 n번 반복하여 반환

    >>> repeat('ab', 3)
    'ababab'
    """
    return s * n


if __name__ == '__main__':
    print(repeat('ye', 2))
