# 8-puzzle_solution

## 기능
사용자가 풀기를 원하는 문제를 입력하면, 해당 퍼즐의 풀이 과정을 차례로 보여준다.

## 구현 방법
BFS나 DFS보다 빠르게 탐색하기 위한 방법을 찾기 위해, 최고 우선 탐색을 바탕으로 하여 문제를 풀이한
다.
처음 입력받은 문제 상태(start)를 현재 문제 상태(now_problem)에 넣는다.
현재 문제 상태에서 빈칸이 이동될 수 있는 모든 경우의 수를 확인하고, 처음 보는 문제 상태일 경우에는 그
상태(visited)와 평가 함수의 값(score), 그 상태의 바로 이 전 값(visited_dic, 풀이 과정을 보여주기 위한
딕셔너리)을 저장한다. 해당 문제 상태의 모든 경우의 수를 확인하면 탐색하지 않은 상태 중 가장 큰 평가
함수의 값을 가진 상태를 현재 문제 상태로 가져와 해당 과정을 반복한다.
i) 목표와 동일한 상태가 나올 경우, 문제 풀이에 성공한 것이므로, visited_dic을 거꾸로 올라가 풀이 과정
을 사용자에게 보여주고 종료한다.
ii) 만일, 모든 경로를 탐색했음에도 목표 상태에 도달할 수 없거나, 방문 상태 수(visited)가 10000이 넘어
가면(무한 루트) 풀 수 없는 문제나 입력이 잘못된 문제로 판단하고 문제 풀이를 종료한다.
