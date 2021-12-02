from random import randint


def generate_numbers(n):
    rand_list = set()
    while len(rand_list) <= 5:
        rand_list.add(randint(1, 45))
    return rand_list


def draw_winning_numbers():
    gener_list = list(generate_numbers(6))
    gener_list.sort()
    gener_list.append(randint(1, 45))
    return gener_list


def count_matching_numbers(list_1, list_2):
    set_list1 = set(list_1)
    set_list2 = set(list_2)
    set_intersection = set.intersection(set_list1, set_list2)
    return len(set_intersection)


def check(numbers, winning_numbers):
    normal_numbers = winning_numbers[:6]
    bonus_number = winning_numbers[6:]
    normal_count = count_matching_numbers(numbers, normal_numbers)
    bonus_count = count_matching_numbers(numbers, bonus_number)
    if normal_count == 6:
        return 1000000000
    elif normal_count == 5 and bonus_count == 1:
        return 50000000
    elif normal_count == 5:
        return 1000000
    elif normal_count == 4:
        return 50000
    elif normal_count == 3:
        return 5000
    return 0

