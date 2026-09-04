"""
[이진 검색 트리 - Binary Search Tree (BST)]

문제 설명:
- 이진 검색 트리에서 값을 검색합니다.
- BST 특징: 왼쪽 자식 < 부모 < 오른쪽 자식
- 이 특성을 이용하여 빠른 검색이 가능합니다.
- 왼쪽 서브트리의 모든 값 < 현재 노드 값
- 오른쪽 서브트리의 모든 값 > 현재 노드 값

입력:
- root: 트리의 루트 노드
- target: 찾을 값

출력:
- True: 값이 존재
- False: 값이 없음

예제:
트리:
      5
     / \
    3   7
   / \
  2   4

찾는 값: 4 → True
찾는 값: 6 → False

힌트:
- target < root.value → 왼쪽으로 이동
- target > root.value → 오른쪽으로 이동
- target == root.value → 찾음!
"""

class TreeNode: #트리 노드라는 이름의 클래스 만듬
    def __init__(self, value):#객체를 새로 만들때 자동으로 실행되는 초기화 함수 value는 이 노드에 저장할 값을 받는 매개변수
        self.value = value #전달 받은 값을 이 노드 안에 저장 TreeNode(5)를 만들면, 이 노드는 값 5를 가지고 있게됨 value= 그사람 이름
        self.left = None # 왼쪽에 연결된 자식 아직 자식이 없으니까 비어있음 처리
        self.right = None # 오른쪽에 연결된 자식 아직 자식이 없으니까 비어있음 처리

def search_bst(root, target):
    """
    BST에서 값 검색
    
    Args:
        root: 트리 루트
        target: 찾을 값
    
    Returns:
        True/False
    
    """
    # TODO: root가 None이면 False 반환
    if root is None:
        return False
    
    # TODO: 값을 찾으면 True 반환
    ## target이 작으면 왼쪽 서브트리에서 검색
    ## target이 크면 오른쪽 서브트리에서 검색
    
    if root.value == target:  # 루트값이 타겟이랑 같으면
        return True     # 참 반환
    elif root.value > target: #루트 값이 타겟보다 작으면
        return search_bst(root.left,target) #왼쪽 검색
    else:
        return search_bst(root.right,target)    #아니면 오른쪽 검색    

# ## while 문 버전
# if root is None:
#     return False

# while True:
#     if root.value == target:  # 루트값이 타겟이랑 같으면
#         return True     # 참 반환
#     elif root.value > target: #루트 값이 타겟보다 작으면
#         root=root.left #왼쪽 검색
#         else:
#             root=root.right    #아니면 오른쪽 검색  
#     if root is None:
#        return False  
    



    








# 테스트 케이스
if __name__ == "__main__":
    # BST 생성:
    #       5
    #      / \
    #     3   7
    #    / \
    #   2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    
    print("=== 이진 검색 트리 ===")
    print("트리 구조: 5를 루트로 하는 BST")
    
    test_values = [2, 4, 5, 6, 7]
    for val in test_values:
        result = search_bst(root, val)
        print(f"값 {val} 검색: {result}")


