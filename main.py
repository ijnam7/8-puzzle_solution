from collections import deque

# 사용자에게서 문제를 입력 받아 문자열 start에 저장한다.
print("start: ")
start = ""
for _ in range(3):
    start += "".join(list(input().split()))

# 문제 목표를 설정한다.
goal = "123456780"
goal_list = list(goal)

# 큐 q: 방문할 문제 상태의 순서를 관리한다.
# 리스트 visited: 문제 상태를 저장한다.
# 리스트 score: index가 동일한 visited의 평가함수 값을 저장한다.
# 딕셔너리 visited_dic: 문제 상태와 그 직전 상태를 저장하여, 순서를 확인한다.
q = deque([start])
visited = [start]
visited_dic = {start:-1}
score = [-1]

# 빈 칸이 이동할 때 사용한다.
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 퍼즐 상태를 출력할 때 사용한다.
def puzzle_print(pro):
    for i in range(3):
        for j in range(3):
            print(pro[i*3+j], end=" ")
        print("")
    print("------")

# 평가함수 값을 계산할 때 사용한다.
def check_score(pro):
    c = 0
    pro_list = list(pro)
    for i in range(9):
        if goal_list[i] == pro_list[i]:
            c += 1
    return c


def solution():
    # 문제 풀이 전, start가 goal과 동일할 경우,
    # 문제를 종료한다.
    if start == goal:
        print("The problem is equal to the goal.")
        return 0

    # 빈 칸이 더 이상 이동할 수 없거나, 문제를 풀 수 없을 경우,
    # 반복을 종료한다.
    while q:
        # 현재 무제 상태와 그 상태의 빈칸의 위치를 찾아온다.
        now_problem = q.popleft()
        now_blank = now_problem.index('0')
        x, y = now_blank//3, now_blank%3

        # 빈칸을 사방으로 이동시켜,
        # 퍼즐 내에서 이동이 가능하고 해당 상태가 이전에 기록된 적이 없다면,
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                ext_blank = 3*nx + ny
                change_problem = list(now_problem)
                change_problem[ext_blank], change_problem[now_blank] = change_problem[now_blank], change_problem[ext_blank]
                ext_problem = "".join(change_problem)

                if ext_problem not in visited:
                    # 해당 상태를 visited와 visited_dic, score에 기록한다.
                    visited.append(ext_problem)
                    visited_dic[ext_problem] = now_problem
                    score.append(check_score(ext_problem))

                    # 해당 상태가 목표 상태일 경우, 문제 풀이를 출력하고 종료한다.
                    if ext_problem == goal:
                        result_q = []
                        p, k = 0, ext_problem
                        while p != -1:
                            result_q.append(k)
                            p = visited_dic.get(k)
                            k = p
                        count = 0
                        while result_q:
                            r = result_q.pop()
                            print("(%d)" %(count))
                            puzzle_print(r)
                            count += 1
                        return 0

        # 가장 높은 평가함수를 가진 상태를 큐 q에 넣는다.
        # 탐색한 상태를 구분하기 위하여 탐색한 적 있는 상태의 점수는 -1로 한다.
        max_score_i = score.index(max(score))
        if score[max_score_i] != -1:
            q.append(visited[max_score_i])
            score[max_score_i] = -1

        # 문제를 풀 수 없다 판단되면 반복을 종료한다.
        if len(visited) > 10000:
            break
    print("You have entered an incorrect or unresolved puzzle.")
    return -1


print("=======")
print("reselt: ")
solution()

