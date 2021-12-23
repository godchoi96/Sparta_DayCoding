lilNum = 0
bigNum = 100
num = int(input('숫자를 입력하세요'))
answer = ""

while True:
    half = int((lilNum+bigNum)/2)
    print('제생각에는...'+ str(half))
    if (half == num):
        print("정답입니다")
        break

    answer =input("up? down?")
    if (answer == "up" and half > num):
         print("Don't be a liar :(")
    elif (answer == "down" and half < num):
         print("Don't be a liar :(")
    elif (answer == "up"):
            lilNum= half
    elif (answer == "down"):
            bigNum= half