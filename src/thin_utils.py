"""이경희(thin) 유틸 예시
"""

def greet(name: str) -> str:
    """간단한 인사 문자열 반환 예시

    >>> greet('Park')
    'Hello, Park'
    """
    return f"Hello, {name}"


if __name__ == '__main__':
    print(greet('thin'))
