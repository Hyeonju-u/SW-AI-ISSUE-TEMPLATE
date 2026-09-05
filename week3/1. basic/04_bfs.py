"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용￼￼
- 방문 체크 필요
- 가까운 것부터 방문
"""

# ""
# BFS 핵심
# 여러개를 한개씩 때리면서 감 시간복잡도 낮음
# 시작 정점으로 부터 제일 가까운곳 먼저 방문
# 맨처음 시작 노드에 큐를 삽입해서 시작
# 또한 노드를 방문했다면 방문 처리 해줘야함
# 다음과 같은 알고리즘에 의해 작동
# 1 큐에서 노드를 하나꺼냄
# 2. 해당 노드에 연결된 노드 중 방문하지않은 노드를 방문하고 차례대로 큐에 삽입
# 3.큐가 빌때까지 해당 동작 반복

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited = []
    
    # TODO: 큐 생성 및 시작 정점 추가
    ## 방문한 정점 집합
    visited=[start] #시작 정점 추가
    queue= deque([start])



    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들 확인
    ## 방문하지 않은 정점이면 큐에 추가
    while queue: # queue가 빌때 까지 반복
        current_node = queue.popleft() #큐에서 먼저 들어간거 먼저 빼고 현재 노드에 값 씌우기
        #print(current_node) #현재 노드 확인(인접한 정점들 확인?)
        for next_node in graph[current_node]: #다음 노드 확인
            if next_node not in visited: #방문하지않은 정점이면 큐에 추가
                visited.append(next_node) 
                queue.append(next_node)

    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

# visited=[start]
#     queue= deque([start])



#     # TODO: 큐가 빌 때까지 반복
#     ## 큐에서 정점 꺼내기
#     ## 인접한 정점들 확인
#     ## 방문하지 않은 정점이면 큐에 추가
#     while len(queue) < 0: # queue가 0이면
#         current_node = queue.popleft() #큐에서 먼저 들어간거 먼저 빼고 현재 노드에 값 씌우기
#         print(current_node) #현재 노드 확인(인접한 정점들 확인?)
#         for next_node in graph(current_node): #다음 노드 확인
#             if current_node not in visited[next_node]: #방문하지않은 정점이면 큐에 추가
#                 visited.append(next_node) 
#                 queue.append(visited)