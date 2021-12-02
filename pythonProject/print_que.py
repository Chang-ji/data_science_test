import datetime

start_time = datetime.datetime.now()
############################################
test_case_enumerate = int(input(f"문서의 개수: "))

for idx in range(test_case_enumerate):
    n, m = list(map(int, input(f"정수 값과 중요도를 입력하세요 : ").split(" ")))
    queue_list = list(map(int, input(f"Queue_list 값을 입력하세요 : ").split(" ")))
    queue_list = [(i, idx) for idx, i in enumerate(queue_list)]
    print(queue_list)

    count = 0
    while True:
        if queue_list[0][1] == max(queue_list, key=lambda x: x[0])[1]:
            count += 1
            if queue_list[0][1] == m:
                print(count)
                break
            else:
                queue_list.pop(0)
        else:
            queue_list.append(queue_list.pop(0))



############################################
end_time = datetime.datetime.now()

print(f"수행시간 : {end_time - start_time}")
