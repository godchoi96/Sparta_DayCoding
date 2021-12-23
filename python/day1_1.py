from random import randint

c = randint(1, 100)
print(c)
clear = 0

for i in range(0, 5):
    p = int(input('값을 입력하세요 : '))
    if p > c:
        print('다운')
    elif p < c:
        print('업')
    else:
        clear = 1
        break

if clear == 1:
    print('성공')
else:
    print('실패 ! 정답은 {0}였습니다.'.format(c))

