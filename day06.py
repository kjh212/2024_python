class Pokemon:
    pass

pickchu=Pokemon()
squirtle=Pokemon()
pickchu.name="pizk"
pickchu.nemesis=squirtle
print(pickchu.name)
squirtle.name="Gobok"
print(pickchu.nemesis.name)