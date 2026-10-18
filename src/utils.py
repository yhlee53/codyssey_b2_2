"""팀 유틸 함수 템플릿
각 팀원은 자신의 파일에 함수를 추가하고 간단한 사용 예시를 docstring 또는 README에 작성하세요.
"""

def hello(name: str) -> str:
    """간단한 예시 함수: 인사 문자열 반환

    예시:
    >>> hello('Park')
    'Hello, Park'
    """
    return f"Hello, {name}"


if __name__ == '__main__':
    print(hello('Team'))
