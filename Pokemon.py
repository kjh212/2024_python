import random
import sys
class Pokemon():
    def __init__(self,name,attribute,HP):
        self.name = name
        self.attribute = attribute
        self.HP = HP

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__('피카츄','전기속성',10)


    def attack(self,enemy):
        print(f'{enemy.name}의 HP는 {enemy.HP}이다.(enter)')
        input('')
        print('다음 중 선택하세요.(enter)')
        input('')
        while enemy.HP > 0:
            attackinput = input('1.몸통박치기\n2.백만볼트\n3.도망치기\n-->')
            if attackinput=='1':
                enemy.HP=enemy.HP-2
                print('효과는 괜찮았다.(enter)')
                input('')
            elif attackinput=='2':
                if enemy.attribute=='물속성':
                    enemy.HP=enemy.HP-3
                    print('효과는 굉장했다.(enter)')
                elif enemy.attribute=='전기속성':
                    enemy.HP=enemy.HP-2
                    print('효과는 괜찮았다.(enter)')
                elif enemy.attribute=='불속성':
                    enemy.HP=enemy.HP-1
                    print('효과는 미미했다.(enter)')
                input('')
            elif attackinput=='3':
                print('상대가 너무 강하다..도망을 선택했다.(enter)')
                input('')
                break
            else:
                print('다시 선택하십쇼.(enter)')
                input('')

            if enemy.HP > 0:
                print(f'남은 체력은 {enemy.HP}이다. ')
            elif enemy.HP <= 0:
                print(f'{enemy.name}을 물리쳤다!!!(enter)')
                input('')
        your_poke = Pikachu()
        startpokemon.activity(your_poke)





class Charmander(Pokemon):
    def __init__(self):
        super().__init__('파이리','불속성',9)

    def attack(self, enemy):
        print(f'{enemy.name}의 HP는 {enemy.HP}이다.(enter)')
        input('')
        print('다음 중 선택하세요.(enter)')
        input('')
        while enemy.HP > 0:
            attackinput = input('1.머리박치기\n2.불대포\n3.도망치기\n-->')
            if attackinput == '1':
                enemy.HP = enemy.HP - 2
                print('효과는 괜찮았다.(enter)')
                input('')
            elif attackinput == '2':
                if enemy.attribute == '전기속성':
                    enemy.HP = enemy.HP - 3
                    print('효과는 굉장했다.(enter)')
                elif enemy.attribute == '불속성':
                    enemy.HP = enemy.HP - 2
                    print('효과는 괜찮았다.(enter)')
                elif enemy.attribute == '물속성':
                    enemy.HP = enemy.HP - 1
                    print('효과는 미미했다.(enter)')
                input('')
            elif attackinput == '3':
                print('상대가 너무 강하다..도망을 선택했다. (enter)')
                input('')
                break
            else:
                print('다시 선택하십쇼. (enter)')
                input('')

            if enemy.HP > 0:
                print(f'남은 체력은 {enemy.HP}이다.')
            elif enemy.HP <= 0:
                print(f'{enemy.name}을(를) 물리쳤다!!!(enter)')
                input('')
        your_poke = Charmander()
        startpokemon.activity(your_poke)
class Squirtle(Pokemon):
    def __init__(self):
        super().__init__('꼬부기','물속성',11)

    def attack(self, enemy):
        print(f'{enemy.name}의 HP는 {enemy.HP}이다.(enter)')
        input('')
        print('다음 중 선택하세요.(enter)')
        input('')
        while enemy.HP > 0:
            attackinput = input('1.머리박치기\n2.물대포\n3.도망치기\n-->')
            if attackinput == '1':
                enemy.HP = enemy.HP - 2
                print('효과는 괜찮았다. (enter)')
                input('')
            elif attackinput == '2':
                if enemy.attribute == '불속성':
                    enemy.HP = enemy.HP - 3
                    print('효과는 굉장했다.(enter)')
                elif enemy.attribute == '물속성':
                    enemy.HP = enemy.HP - 2
                    print('효과는 괜찮았다.(enter)')
                elif enemy.attribute == '전기속성':
                    enemy.HP = enemy.HP - 1
                    print('효과는 미미했다.(enter)')
                input('')
            elif attackinput == '3':
                print('상대가 너무 강하다..도망을 선택했다.(enter)')
                input('')
                break
            else:
                print('다시 선택하십쇼.(enter)')
                input('')

            if enemy.HP > 0:
                print(f'남은 체력은 {enemy.HP}이다. ')
            elif enemy.HP <= 0:
                print(f'{enemy.name}을 물리쳤다!!!(enter)')
                input('')
        your_poke=Squirtle()
        startpokemon.activity(your_poke)

class firemon(Pokemon):
    def __init__(self):
        super().__init__('불괴물','불속성',7)

class watermon(Pokemon):
    def __init__(self):
        super().__init__('물괴물','물속성',12)

class elecmon(Pokemon):
    def __init__(self):
        super().__init__('전기괴물','전기속성',8)


class pokemon:
    def start(self):
        print('게임을 시작하려면 enter을 누르시오.')
        input('')
        print('포켓몬 월드에 오신 것을 환영합니다.(enter)')
        input('')
        print('당신의 포켓몬을 고르시오.')
        startpokemon.choice()
    def choice(self):
        pokemon_who = ['피카츄', '파이리', '꼬부기']
        while True:
            num = input('1:피카츄\n2:파이리\n3:꼬부기\n-->')
            if num=='1' or num=='2' or num=='3':
                int2 = int(num)
                print(f'{pokemon_who[int2-1]}을 선택하시겠습니까?')
                answer1 = input("1.예\n2.아니오\n-->")
                if answer1 == "1":
                    print(f'{pokemon_who[int2-1]}를 선택하셨습니다.(enter)')
                    if num=='1':
                        your_pokemon=Pikachu()
                    elif num=='2':
                        your_pokemon=Charmander()
                    elif num=='3':
                        your_pokemon=Squirtle()
                    input('')
                    print(f'{pokemon_who[int2-1]}와 함께 무엇을 하실 것인가요?')
                    startpokemon.activity(your_pokemon)
                    break
                else:
                    print('다시 선택하십쇼.')
                    input('')
                    continue
            else :
                print('다시 선택하십쇼.(enter)')
                input('')
                continue

    def activity(self,your_pokemon):
        while True:
            monster = [Pikachu, Charmander, Squirtle, watermon, firemon, elecmon]
            monster_choice = random.choice(monster)
            enemy = monster_choice()
            active1 = input('1:풀숲으로 들어간다.\n2.게임 종료.\n-->')
            if active1 == '1':
                print(f'야생의 {enemy.name}이(가) 나타났다.(enter)')
                input('')
                while True:
                    b=input('1.싸운다.\n2.도망간다.\n-->')
                    if b=='1':
                        your_pokemon.attack(enemy)
                        break
                    elif b=='2':
                        print('상대가 너무 강하다..도망을 선택했다.(enter)')
                        input('')
                        break
                    else:
                        print('다시 입력하세요(enter)')
                        input('')
                        continue

            elif active1 == '2':
                print('게임을 종료하시겠습니까?')
                a=input('1.예\n2.아니오.\n-->')
                if a == '1':
                    sys.exit()
                if a == '2':
                    continue
                else :
                    print('다시 입력하세요(enter)')
                    input('')
                    pass
            else:
                print('다시 선택하십쇼(enter)'
                      '')
                input('')
                continue



startpokemon=pokemon()
startpokemon.start()