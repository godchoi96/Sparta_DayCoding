from random import randint, randrange

last_number = 0

def computer_say():
    if (last_number + 3 + 2) % 4 == 0:
        c = 3
    elif (last_number + 2 + 2) % 4 == 0:
        c = 2
    elif (last_number + 1 + 2) % 4 == 0:
        c = 1
    else:
        c = randrange(1, 4)

    for i in range(1, c + 1):
        print('컴퓨터 : {0}'.format(last_number + i))
    return last_number + c

def user_say():
    user = int(input('사용자 : '))
    while user not in [1, 2, 3]:
        print('다시 입력하세요!')
        user = int(input('사용자 : '))
    for i in range(1, user + 1):
        print('사용자 : {0}'.format(last_number + i))
    return last_number + user

who_first = randint(0, 1)
if who_first == 1:
    last_number = computer_say()

while True:
    last_number = user_say()
    if last_number == 31:
        print('컴퓨터의 승리')
        break
    last_number = computer_say()
    if last_number == 31:
        print('유저의 승리')
        break
