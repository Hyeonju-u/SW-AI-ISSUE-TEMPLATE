"""
[분할 정복 - 배열의 최댓값 찾기]

문제 설명:
- 분할 정복(Divide and Conquer) 방식으로 배열의 최댓값을 찾습니다.
- 배열을 반으로 나누고, 각 부분의 최댓값을 구한 후 비교합니다.

입력:
- arr: 정수 배열
- left: 시작 인덱스
- right: 끝 인덱스

출력:
- 배열의 최댓값

예제:
입력: [3, 5, 1, 8, 2, 9, 4]
출력: 9

힌트:
- Base case: left == right일 때 arr[left] 반환
- 배열을 반으로 나누어 재귀 호출
- 왼쪽과 오른쪽의 최댓값 중 큰 값 반환
"""

def find_max_divide_conquer(arr, left, right):
    """
    분할 정복으로 최댓값 찾기
    
    Args:
        arr: 배열
        left: 시작 인덱스
        right: 끝 인덱스
    
    Returns:
        최댓값
    """
    # TODO: base case - 원소가 하나면 그 값 반환
    if left==right:
        return arr[right] # left든,right 이든 어떤거를 반환하라고 하든 상관없음 어차피 위에 왼쪽 오른쪽이 같으면 그값 반환하라고 한거라 같은값임
    #원소가 하나 남으면 그 자체가 이 범위의 최댓값
    
    # TODO: 중간 지점 계산
    mid= (left+right) // 2
    
    # TODO: 왼쪽 절반의 최댓값
    left_max=find_max_divide_conquer(arr,left,mid)
    # 재귀호출은 지금 만들고있는 이함수 자체를 이 함수 정의안에서 다시 부르는것
    #파이썬은 함수가 def로 정의되는 순간 그 이름의 함수 전체를 가르키게됨
    #그러니까 이 함수 본문 코드가 실행될때 그 코드 안에서 자기 이름을 부르면 나 자신을 처음부터 다시 실행하라는 뜻
        
    # TODO: 오른쪽 절반의 최댓값
    right_max=find_max_divide_conquer(arr,mid+1,right)
    #함수 파라미터 순서가 두번째 자리엔 항상 왼쪽 인덱스 역할이 와야함,세번째 자리 끝에는 끝인덱스 역할이 와야함
    # TODO: 둘 중 큰 값 반환
    if left_max>right_max:
        return left_max
    return right_max

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [3, 5, 1, 8, 2, 9, 4]
    result1 = find_max_divide_conquer(arr1, 0, len(arr1) - 1)
    print(f"배열: {arr1}")
    print(f"최댓값: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [10, 20, 30, 40, 50]
    result2 = find_max_divide_conquer(arr2, 0, len(arr2) - 1)
    print(f"배열: {arr2}")
    print(f"최댓값: {result2}")
    print()
    
    # 테스트 케이스 3
    arr3 = [100]
    result3 = find_max_divide_conquer(arr3, 0, len(arr3) - 1)
    print(f"배열: {arr3}")
    print(f"최댓값: {result3}")


