"""이열형(yhlee) 계산기 공통 유틸"""

from src.bal_utils import subtract
from src.son_utils import multiply
from src.thin_utils import add
from src.yeri_utils import modulo


def calculate(a: float, b: float, operator: str) -> float:
    """기호에 따라 적절한 연산을 수행한다."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': modulo,
    }

    if operator not in operations:
        raise ValueError(f'지원하지 않는 연산입니다: {operator}')

    return operations[operator](a, b)


if __name__ == '__main__':
    print(calculate(10, 3, '+'))
    print(calculate(10, 3, '-'))
    print(calculate(10, 3, '*'))
    print(calculate(10, 3, '/'))
