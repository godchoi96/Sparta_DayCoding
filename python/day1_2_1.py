from math import floor # 내림

number_list = range(1, 101)

p = int(input('값을 입력하세요 : '))
while p < 1 or p > 101:
    print('다시 입력하세요.')
    p = int(input('값을 입력하세요 : '))

while True:
    c = number_list[floor(len(number_list) / 2)]
    print('{0}?'.format(c))
    if c == p:
        print('성공')
        break

    question = input('업, 다운? : ')
    if question == '업' and p > c:
        number_list = number_list[number_list.index(c):]
    elif question == '다운' and p < c:
        number_list = number_list[:number_list.index(c)]
    else:
        print('당신은 거짓말을 쳤습니다.')
