import time
start_time = time.time() # 측정 시작

test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    print(queue)
    count = 0
    while True:
        print(queue, '1')
        if queue[0][0] == max(queue, key = lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))


# 프로 그램 소스코드
end_time = time.time()
print("time: ", end_time-start_time)










