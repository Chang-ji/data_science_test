import datetime

start_time = datetime.datetime.now()
############################################
test_case_num = int(input())

for _ in range(test_case_num):
    left_stack = []
    right_stack = []

    password_str = input()
    for str_data in password_str:
        if str_data == "-":
            if left_stack:
                left_stack.pop()
        elif str_data == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        elif str_data == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        else:
            left_stack.append(str_data)
    left_stack.extend(reversed(right_stack))
    print("".join(left_stack))



############################################
end_time = datetime.datetime.now()

print(f"수행시간 : {end_time - start_time}")