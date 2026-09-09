"""
[위상 정렬 - Topological Sort]
A를 먼저 해야 B를 할수 있다는 순서 규칙들이 있을때 이 규칙을 모두 만족하는 하나의 전체 순서를 만드는것
선행 조건이 있는 일들을 순서대로 나열하기

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""
#위상 정렬은 방향그래프 위에서 정의 됨 그래프의 노드들을 한줄로 나열하는데 다음 조건을 만족해야함 그래프 노드들을 한줄로 나얄하는데 다음 조건을 만족해야함
#간선 A->B가 있으면 나열한 순서에는 반드시 A 가 B보다 앞에 와야함
#중요한 조건 DAG(방향 비순환 그래프)에서만 가능
# 정답이 하나로 정해지지 않을 수있음 조건을 만족하는 순서가 여러개 있을수있다.
#진입차수:어떤 노드로 들어오는 간선의 개수
#어떤 노드에게 나를 가리키는 화살표가 몇개있는지 세어본 숫자
#진입차수가 0인 노드부터 순서에 넣고-> 그 노드를 순서에 넣고 제거하면->그 노드가 가리키던 다른 노드들의 진입차수가 1씩 줄어듦->그러면 또 진입차수 0이되는 노드가 생기고 그걸 또 순서에 넣는다->반복

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    graph = [[] for i in range(vertices)]
    indegree=[0] * (vertices)  #진입 차수 초기화 0부터 시작해야 화살표가 몇개있는지 카운트 할수 있음
    queue = deque()
    
    # TODO: 그래프 구성 및 진입 차수 계산
    for a,b in edges:
        graph[a].append(b)
    for i in range(vertices): #정점을 하나씩 꺼내서 출발점 확인
        for j in graph[i]: # 출발점이 가리키는 도착점을 순회
            indegree[j] += 1        #j가 화살표를 받는 노드라 가리켜지는쪽 진입차수 +1


    
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    for q in range(vertices):
        if indegree[q] == 0:
            queue.append(q)
            
    
    result = []
    
    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]: #인접한 정점들 꺼내서
            indegree[neighbor] -= 1 # 진입 차수 감소
            if indegree[neighbor] == 0: # 진입차수 0인것들은
                queue.append(neighbor) #큐에 추가
                    





    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
