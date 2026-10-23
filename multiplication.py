def multiply(num1, num2):
    return num1 * num2

# 메인 실행부
if __name__ == "__main__":
    print("--- 곱셈 계산기 ---")
    
    try:
        # 사용자로부터 숫자 두 개 입력받기
        a = float(input("첫 번째 숫자를 입력하세요: "))
        b = float(input("두 번째 숫자를 입력하세요: "))
        
        # 함수 호출 및 결과 계산
        result = multiply(a, b)
        
        # 결과 출력 (f-string 사용)
        print(f"결과: {a} * {b} = {result}")
        
    except ValueError:
        # 숫자가 아닌 값을 입력했을 때의 예외 처리
        print("에러: 숫자만 입력해 주세요!")