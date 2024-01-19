class Pokemon:
    pass

pickchu=Pokemon()
squirtle=Pokemon()
pickchu.name="pizk"
pickchu.nemesis=squirtle
print(pickchu.name)
squirtle.name="Gobok"
print(pickchu.nemesis.name)


class Pokemon:
    def __init__(self,name):
        self.name=name
        print(f"{name} 포켓몬스터 생성")

    def attack(self,target):
        print(f"{self.name}이 {target.name}을 공격")

ch=Pokemon('리자몽')
pickchu=Pokemon('피카츄')
squirtle=Pokemon('꼬북이')
