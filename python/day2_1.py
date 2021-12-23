from random import randint

numbers_list = list(range(1, 32))
who_first = randint(1, 2)
win = 0

def computer_Say():
    index = randint(1, 3)
    print('컴퓨터의 차례입니다 : {0}'.format(index))
    computer_list = numbers_list[: index]
    del numbers_list[: index]
    print(computer_list)

def user_Say():
    num = int(input('당신의 차례입니다 : '))
    user_list = numbers_list[: num]
    if len(user_list) < 4:
        del numbers_list[: num]
        print(user_list)
    else:
        print('잘못된 값을 입력하였으므로 컴퓨터의 차례로 변경됩니다.')

while True:
    if who_first == 1:
        if numbers_list != [ ]:
            user_Say()
            win = 1
            if numbers_list == [ ]:
                break
            else:
                computer_Say()
                win = 0
                continue
        else:
            break
    elif who_first == 2:
        if numbers_list != [ ]:
            computer_Say()
            win = 0
            if numbers_list == [ ]:
                break
            else:
                user_Say()
                win = 1
                continue
        else:
            break
    else:
        print('에러')
        break

if win == 0:
    print('컴퓨터 패배')
if win == 1:
    print('유저 패배')