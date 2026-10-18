"""손희진(son) 유틸 예시
"""

def to_upper(s: str) -> str:
    """문자열을 대문자로 변환

    >>> to_upper('abc')
    'ABC'
    """
    return s.upper()


if __name__ == '__main__':
    print(to_upper('son'))
