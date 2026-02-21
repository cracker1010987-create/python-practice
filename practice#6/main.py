import sys

class Champion:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def move(self):
        print(f"[{self.name}]이(가) 전장으로 달려갑니다. 🏃")

    def attack(self):
        print(f"[{self.name}]이(가) 기본 공격을 합니다.")

    def recall(self):
        print(f"[{self.name}]이(가) 본진으로 귀환합니다. (B버튼)")


class Warrior(Champion):
    def attack(self):
        print(f"[{self.name}]이(가) 대검을 휘두릅니다! (물리)")


class Mage(Champion):
    def attack(self):
        print(f"[{self.name}]이(가) 마법 구슬을 던집니다! (마법)")


class Support(Champion):
    def attack(self):
        print(f"[{self.name}]이(가) 아군을 치료합니다. 💖 (힐)")


print("=== 🎮 소환사의 협곡에 오신 것을 환영합니다 ===")

team = []
team.append(Warrior("가렌", 800))
team.append(Mage("아리", 500))
team.append(Support("소라카", 450))

print("\n=== 🔥 한타 시작! (전원 공격) ===")

for champ in team:
    champ.move()
    champ.attack()