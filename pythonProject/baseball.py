from random import randint


def generate_numbers():
    numbers = []
    while len(numbers) != 3:
        rand_input = randint(0, 9)
        if rand_input not in numbers:
            numbers.append(rand_input)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    while len(new_guess) != 3:
        number_guess = int(input(f"{len(new_guess) + 1}번째 숫자를 입력하세요: "))
        if number_guess < 0 or number_guess > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif number_guess in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(number_guess)
    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for idx in range(len(guess)):
        if guess[idx] == solution[idx]:
            strike_count += 1

    for guess_value in guess:
        if guess_value in solution:
            ball_count += 1
    ball_count -= strike_count
    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    tries += 1
    guess_answer = take_guess()
    strike, ball = get_score(guess_answer, ANSWER)
    print(f"{strike}S {ball}B")
    if strike == len(guess_answer):
        print(f"{tries}번 만에 숫자 {len(guess_answer)}개의 값과 위치를 모두 맞추셨습니다.")
        break





