class Animal:
    def __init__(self, name):
        self.name = name

    def cry(self):
        print(f"{self.name}이 웁니다!")


class Dog(Animal):
    def cry(self):
        print(f"강아지 {self.name}이 멍멍 짖습니다!")

class Cat(Animal):
    def cry(self):
        print(f"고양이 {self.name}이 야옹거립니다.")

cat = Cat("야옹이")
cat.cry()


dog = Dog("댕댕이")
dog.cry()