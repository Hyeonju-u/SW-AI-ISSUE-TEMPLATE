"""
[그래프 - 다익스트라 최단경로 (Dijkstra's Shortest Path)]

▣ 문제 배경
- 가중치가 음이 아닌(0 이상) 방향 그래프에서, 한 출발점 'start' 에서 다른 모든 정점까지의
  최단 거리를 구하는 표준 알고리즘입니다.
- 1959년 Edsger W. Dijkstra 가 발표하였으며, 우선순위 큐(min-heap) 와 결합한 구현은
  공지된 표준 기법입니다. 본 지문과 테스트 케이스는 본 학습 자료를 위해
  자체적으로 작성되었습니다.
- 본 학습에서는 `week2/2. advanced/03_priority_queue` 에서 다룬 힙 자료구조를 활용합니다.
최단 거리를 구하는 알고리즘
하나의 노드에서 다른 모든 노드까지의 거리를 구할수있음
알고리즘 원리
최단거리를 구할 노드에서 시작하여 거리가 입력된 노드 중 최단거리가 가장 작은 노드를 돌아가며 선택
노드를 돌아가면서 더 거리가 짧은게 나오면 값을 갱신해서 넣는다




▣ 작은 예시
    정점: 0, 1, 2, 3, 4
    방향 간선(u, v, w):
        0 -> 1 (4)
        0 -> 2 (1)
        2 -> 1 (2)
        2 -> 3 (5)
        1 -> 3 (1)
        3 -> 4 (3)

    그림:
              4
        0 --------> 1
        |\         ^|
        | \1     2/ |
        |  \    /   |1
        |   v  /    v
        |    2 ---> 3 ---> 4
        |    5      3

    start = 0 일 때 최단 거리:
        0 -> 0 : 0
        0 -> 1 : 3   (0->2->1: 1+2)
        0 -> 2 : 1
        0 -> 3 : 4   (0->2->1->3: 1+2+1)
        0 -> 4 : 7   (0->2->1->3->4: 1+2+1+3)

▣ 구현할 함수
dijkstra(n: int, edges: list[tuple[int, int, int]], start: int) -> list
  - 정점은 0, 1, ..., n-1 의 정수로 식별됩니다.
  - edges 는 (u, v, w) 형식의 방향 간선들의 리스트 (w >= 0).
  - 반환값은 길이 n 의 리스트 dist 로, dist =len(n)
        dist[i] = start 에서 정점 i 까지의 최단 거리,
        도달 불가능하면 float('inf').
  - dist[start] 는 항상 0 이어야 합니다.

▣ 제약
- 0 <= n <= 1000, 간선 수 <= 5000 정도면 충분.
- 0 <= w <= 10000

▣ 힌트 (heapq 사용, O((V+E) log V))
  import heapq
  - dist 를 INF 로 초기화하고 dist[start] = 0
  - 우선순위 큐에 (0, start) 를 push
  - 큐가 빌 때까지:
      (d, u) = heappop
      if d > dist[u]: continue     # 이미 더 짧은 경로로 처리됨
      for v, w in graph[u]:
          if dist[u] + w < dist[v]:
              dist[v] = dist[u] + w
              heappush(pq, (dist[v], v))
"""

import heapq

# 우선순위 큐를 위해 만들어진 자료구조
# 여러 값 중 최대/최소 값을 빠르게 찾아내도록 만들어진 반정렬 상태
# 힙트리는 중복된 값을 허용함
# #힙은 완전 이진 트리 자료구조의 일종
# # 힙은 항상 루트 노드를 제거함
# # 최소힙 루트 노드가 가장 작은 값을 가짐
# # 따라서 값이 작은 데이터가 우선적으로 제거 됨
# # 최대 힙
# # 루트 노드가 가장 큰 값을 가짐
# # 따라서 큰 데이터가 우선적으로 제거 됨
# # #우선 순위 큐란 들어간 순서와 상관없이 우선 순위를 가진 원소는 낮은 우선 순위를 가진 원소보다 먼저 처리
# 들어온 순서는 무시하고 중요도(우선순위)가 높은 애가 먼저 나감
# 우선순위가 똑같은 애들끼리는 먼저 들어온게 먼저 나가는 규칙 성립 함
# # 만약 두원소가 같은 우선 순위를 가진다면 큐에서 그들의 순서에 의해 처리
# # 힙큐: 파이썬 내장모듈 내부적으로 최소 힙의 형태로 정렬됨
# heappush(heap, item)-> 힙 함수를 통해 아이템을 힙에 추가 아이템을 추가하면 최소 힙으로 정렬됨
# heapify(list)->함수를 통해 list를 heap으로 변환한다.


INF = float("inf")


def dijkstra(n: int, edges: list, start: int) -> list:
    """
    n: 정점 수 (정점 번호 0 ~ n-1)
    edges: (u, v, w) 형식 방향 간선 리스트
    start: 출발 정점
    반환: 길이 n 의 거리 리스트 (도달 불가 = float('inf'))
    """
    # TODO: 인접 리스트 graph 구성 (graph[u] = [(v, w), ...])
    # TODO: dist 를 INF 로 초기화하고 dist[start] = 0
    # TODO: 우선순위 큐(heapq)로 BFS-like 최단경로 탐색
    # TODO: dist 반환

    dist = [INF] * (n)
    graph = [[] for i in range(n)]
    dist[start] = 0
    pq = []

    # edges(u,v,w) edges의 간선 하나 u번 정점에서 v번 정점으로 가는, 가중치 w인 길
    # graph[1] = [(2, 1)]           # 1번에서 2번까지 비용1

    for u, v, w in edges:  # 간선 순회
        graph[u].append((v, w))
    heapq.heappush(pq, (0, start))

    while pq:
        dist_u, u = heapq.heappop(pq)
        if dist[u] < dist_u:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist_u + w
                heapq.heappush(pq, (dist[v], v))
        if dist_u > dist[u]:
            continue
    return dist


def _format(dist):
    """출력 표기를 위한 헬퍼: float('inf') 는 'INF' 로 보여줌"""
    return [("INF" if x == INF else x) for x in dist]


if __name__ == "__main__":
    print("[테스트 1] 예시 그래프 (5개 정점)")
    n = 5
    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (2, 3, 5),
        (1, 3, 1),
        (3, 4, 3),
    ]
    print(f"  n={n}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 2] 정점 1개")
    print(f"  n=1, edges=[], start=0")
    print(f"  최단 거리: {_format(dijkstra(1, [], 0))}")
    print()

    print("[테스트 3] 도달 불가능한 정점 포함")
    n = 4
    edges = [(0, 1, 5)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 4] 동일한 거리의 두 경로 (둘 다 7)")
    n = 4
    edges = [(0, 1, 3), (1, 3, 4), (0, 2, 5), (2, 3, 2)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 5] 0 가중치 간선 포함")
    n = 3
    edges = [(0, 1, 0), (1, 2, 0), (0, 2, 5)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")

# for value in range(n):
#     heapq.heappush()
#     current = len(heapq)-1
#     while heapq:
#         (d, u) = heappop
#     if d > dist[u]: continue
#     for v, w in graph[u]:
#                 if dist[u] + w < dist[v]:
#                     dist[v] = dist[u] + w
#                     heappush(pq, (dist[v], v))
