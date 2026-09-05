"""
[동적 프로그래밍 - 피보나치 수열 (하향식 / Top-down)]

문제 설명:
- 메모이제이션(Memoization)을 사용한 하향식 DP로 피보나치 수를 계산합니다.
- 이미 계산한 값을 저장하여 중복 계산을 방지합니다.

입력:
- n: 구하고자 하는 피보나치 수의 인덱스

출력:
- n번째 피보나치 수

예제:
입력: n = 10
출력: 55

힌트:
- 딕셔너리에 계산 결과 저장
- 이미 계산했으면 저장된 값 반환
- 계산 안 했으면 재귀 호출 후 저장

설명:
- 시간 복잡도: O(n) - 각 값을 한 번만 계산
- 공간 복잡도: O(n) - memo 딕셔너리와 재귀 스택

동적 프로그래밍 (Dynamic Programming):
- 큰 문제를 작은 부분 문제로 나누어 해결
- 부분 문제의 결과를 저장하여 재사용
- 중복 계산을 제거하여 효율성 향상

하향식 (Top-down) 방식:
- 큰 문제부터 시작
- 재귀로 작은 문제로 분해
- 메모이제이션으로 중복 제거
- fib(10) → fib(9) + fib(8) → ... → fib(0), fib(1)

메모이제이션 (Memoization):
- 계산 결과를 memo에 저장
- 같은 값을 다시 계산할 필요 없음
- 캐싱(Caching)과 유사한 개념
# 이미 한번 계산한 값은 저장해 뒀다가 다음에 똑같은걸 구해야하면 계산 하지말고 저장해둔 값을 그냥 꺼내 써라
# 하향식이라는 말의 의미: 큰 문제 부터 시작해서 그 문제를 풀려면 필요한 작은 문제로 내려가는 방식
재귀를 타고 밑으로 내려가면서 필요한 답을 구해가는것 ex) fib(5)구하고 싶으면 fib(4)랑 fib(3)이 필요하네" → 아래로 내려감
탑다운+메모이제이션을 합치면
fib(n)을 구하라는 요청이 오면 → 먼저 저장해둔 곳에 이미 답이 있는지 확인 → 있으면 그거 그대로 꺼내서 반환 → 없으면 재귀로 fib(n-1), fib(n-2)를 구해서 더한 다음, 그 답을 저장해두고 반환

계산 과정 (예: fib(5)):
일반 재귀:
                    fib(5)
                 /          \
            fib(4)            fib(3)
           /      \          /      \
       fib(3)   fib(2)   fib(2)   fib(1)
       ...      ...      ...       ...
총 계산: 15번 (중복 다수)

메모이제이션:
fib(5) 계산
→ fib(4) 계산 (저장)
→ fib(3) 계산 (저장)
→ fib(2) 계산 (저장)
→ fib(1), fib(0) 반환
→ 이후 fib(3), fib(2) 등은 memo에서 꺼내기만
총 계산: 6번 (중복 0)

DP가 필요한 경우:
1. 최적 부분 구조: 부분 문제의 최적해로 전체 최적해 구성
2. 중복 부분 문제: 같은 문제가 반복적으로 등장

응용:
- 경로 찾기 문제
- 최적화 문제
- 조합 최적화
- 자원 할당
"""

def fibonacci_memo(n, memo=None):
    """
    메모이제이션을 사용한 피보나치 (하향식 DP)
    
    Args:
        n: 피보나치 인덱스
        memo: 계산 결과를 저장할 딕셔너리
    
    Returns:
        n번째 피보나치 수
    """
    # TODO: memo가 None이면 빈 딕셔너리로 초기화
    if memo is None:
        memo ={} 
    
    # TODO: base case #더이상 재귀 안타고 바로 답이 나오는경우
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # TODO: 이미 계산한 값이 memo에 있으면 반환
    if n in memo:
        return memo[n] #재계산하지않고 바로 반환
    
    # TODO: 재귀 호출하여 계산하고 memo에 저장
    else: 
        if n not in memo:  #계산한 값이 메모에 없으면 
            memo[n] = fibonacci_memo(n-1,memo)+fibonacci_memo(n-2,memo)
            #재귀로 fib(n-1), fib(n-2)를 구하고 그 합을 memo[n]에 저장 (다음에 fib(n) 또 필요하면 재사용)
            #memo[n] = fibonacci_memo(n-1)+fibonacci_memo(n-2)
            #fibonacci_memo(n, memo)

    
    return memo[n]

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 피보나치 수열 (메모이제이션) ===")
    for i in range(11):
        result = fibonacci_memo(i)
        print(f"fib({i}) = {result}")
    print()
    
    # 테스트 케이스 2: 큰 수도 빠르게 계산
    print("=== 큰 수 계산 ===")
    n = 50
    result = fibonacci_memo(n)
    print(f"fib({n}) = {result}")
    print()
    
    # 비교: Week1의 재귀 방식은 fib(50)을 계산하기 어려움
    print("참고: 일반 재귀는 fib(40)도 몇 초 걸리지만")
    print("메모이제이션은 fib(100)도 순식간에 계산!")


