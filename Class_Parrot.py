class parrot:
    x="hello"
    def __init__(self, age, name):
        self.name=name
        self.age=age
bird=parrot(10, "Max")
print(bird.age)
print(bird.name)
print(bird.x)