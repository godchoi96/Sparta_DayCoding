from random import randint

class Object:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    # 기본 공격 함수
    def attack(self, target):
        target.hp -= 10
        print('{0}(이)가 {1}(을)를 공격했습니다.'.format(self.name, target.name))

class Player(Object):
    def __init__(self, name, hp, damage):
        Object.__init__(self, name, hp, damage)

    # 마법 공격 함수
    def magicattack(self, target):
        target.hp -= 50
        print('{0}(이)가 {1}(을)를 마법으로 공격했습니다.'.format(self.name, target.name))
        print('{0}의 남은 체력은 {1}입니다.'.format(target.name, target.hp))
        return target.hp

    # 플레이어 정보 확인 함수
    def show_info(self):
        print('{0}의 현재 체력은 {1}입니다.'.format(user.name, user.hp))

    # 플레이어 턴 함수
    def player_turn(self):
        select = input('공격? 마법? : ')
        monsterSelect = input('대상은 누구에게 하시겠습니까? : ')

class Monster(Object):
    def __init__(self, name, hp, damage):
        Object.__init__(self, name, hp, damage)

    # 몬스터 대기 함수
    def stop(self):
        print('{0}(이)가 대기했습니다.'.format(self.name))

    # 몬스터 힐 함수
    def heal(self):
        self.hp += 10
        print('{0}(이)가 자신의 체력을 10만큼 회복했습니다.'.format(self.name))
        return self.hp

    # 몬스터 정보 확인 함수
    def show_info(self):
        for monster in monster_list:
            if monster.hp != 0:
                print('{0}의 현재 체력은 {1}입니다.'.format(monster.name, monster.hp))
        # if monster1.hp != 0:
        #     print('{0}의 현재 체력은 {1}입니다.'.format(monster1.name, monster1.hp))
        # if monster2.hp != 0:
        #     print('{0}의 현재 체력은 {1}입니다.'.format(monster2.name, monster2.hp))
        # if monster3.hp != 0:
        #     print('{0}의 현재 체력은 {1}입니다.'.format(monster3.name, monster3.hp))

    # 몬스터 사망 여부 함수
    def monster_is(self):
        while True:
            for i in range(len(monster_list)):
                if monster_list[i].hp <= 0:
                    monster_list.pop(i)
                    break
                if len(monster_list) == 0:
                    print('승리')
                    break
                else:
                    continue

    # 몬스터 턴 함수
    def monster_turn(self):
        # 몬스터 치료
        if computerSelect == 1:
            print('몬스터가 치료합니다.')

        # 몬스터 대기
        if computerSelect == 2:
            print('몬스터가 대기합니다.')

        # 몬스터 공격
        if computerSelect == 3:
            print('몬스터가 공격합니다.')


computerSelect = randint(1, 3)
user = Player('전사', 100, 10)
monster1 = Monster('미니 고블린', 10, 10)
monster2 = Monster('고블린', 30, 30)
monster3 = Monster('슈퍼 고블린', 50, 50)
monster_list = [monster1, monster2, monster3]




