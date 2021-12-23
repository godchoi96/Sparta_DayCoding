p = int(input('값을 입력하세요: '))
c = 100

if p > 100:
    print('100 이상의 값이 입력되었습니다')

else:
    c = int(c / 2)
    print('{0} 값이 예측되었습니다.'.format(c))
    if p == c:
        print('정답')
    else:
        while 1:
            question = input('업? 다운? ')
            if question == '업':
                if p < c:
                    print('에러')
                    continue
                else:
                    c = int((p + c) / 2) + 1
                    print('{0} 값이 예측되었습니다.'.format(c))
                    if p == c:
                        print('정답')
                        break
                    if p > c:
                        continue

            if question == '다운':
                if p > c:
                    print('에러')
                    continue
                else:
                    c = int(c / 2) + 1
                    print('{0} 값이 예측되었습니다.'.format(c))
                    if p == c:
                        print('정답')
                        break
                    if p < c:
                        continue