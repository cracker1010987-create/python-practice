class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0 
        self.boredom = 0 


    def feed(self):
        print(f"\n[밥] {self.name}가 밥을 먹습니다. 냠냠!")
        self.hunger -= 20
        self.boredom += 5
        if self.hunger < 0:
            self.hunger = 0
        elif self.hunger > 100:
            self.hunger = 100

        if self.boredom < 0:
            self.boredom = 0
        elif self.boredom > 100:
            self.boredom = 100


    def play(self):
        print(f"\n[놀기] {self.name}가 공놀이를 합니다. 와아!")
        self.boredom -= 20
        self.hunger += 10
        if self.hunger < 0:
            self.hunger = 0
        elif self.hunger > 100:
            self.hunger = 100

        if self.boredom < 0:
            self.boredom = 0
        elif self.boredom > 100:
            self.boredom = 100


    def show_status(self):
        print(f"[{self.name}]의 상태")
        print(f"배고픔: {self.hunger} / 100")
        print(f"지루함: {self.boredom} / 100")


name_input = input("키우실 펫의 이름을 지어주세요: ")

my_pet = Pet(name_input)
print(f"{my_pet.name}가 태어났습니다! 잘 돌봐주세요.")

while True:
    my_pet.show_status()
    
    choice = input("행동을 선택하세요 (1.밥주기 2.놀아주기 3.종료): ")

    if choice == "1":
        my_pet.feed()
    elif choice == "2":
        my_pet.play()
    elif choice == "3":
        break