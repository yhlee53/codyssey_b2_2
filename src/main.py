#!/usr/bin/env python3
"""CLI 4칙연산 계산기"""

import argparse

from src.yhlee_utils import calculate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='CLI 4칙연산 계산기')
    parser.add_argument('left', type=float, help='첫 번째 숫자')
    parser.add_argument('operator', choices=['+', '-', '*', '/'], help='연산 기호')
    parser.add_argument('right', type=float, help='두 번째 숫자')
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        result = calculate(args.left, args.right, args.operator)
    except ZeroDivisionError as exc:
        print(f'오류: {exc}')
        raise SystemExit(1) from exc
    except ValueError as exc:
        print(f'오류: {exc}')
        raise SystemExit(1) from exc

    print(f'{args.left} {args.operator} {args.right} = {result}')


if __name__ == '__main__':
    main()
