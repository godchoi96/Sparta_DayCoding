from random import randint

last_number = 0
who_first = randint(0, 2)

def computer_say():
    c = randint(1, 3)
    for i in range(1, 1 + c):
        print('컴퓨터 : {0} '.format(last_number + i))
    return last_number + i

def user_say():
    p = int(input('숫자를 입력하세요. '))
    for i in range(1, 1 + p):
        print('{0}을 입력하셨습니다. '.format(last_number + i))
    return last_number + i

if who_first == 1:
    last_number = user_say()

while True:
    last_number = computer_say()
    if last_number == 31:
        print('유저의 승리!')
        break
    last_number = user_say()
    if last_number == 31:
        print('컴퓨터의 승리!')
        break