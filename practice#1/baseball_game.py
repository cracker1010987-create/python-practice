import random
numbers = list(range(1, 10))
ans = random.sample(numbers, 3)
attemps = 0
print("=== 숫자 야구 게임을 시작합니다 ===")
print("컴퓨터가 0~9 사이의 서로 다른 숫자 3개를 골랐습니다.")
while True:
    n = list(map(int, input("숫자 3개를 입력하세요 : ").split()))
    attemps += 1
    strike = 0
    ball = 0
    for i in range(3):
        if n[i] == ans[i]:
            strike += 1
        elif n[i] in ans:
            ball += 1
    if strike == 0 and ball == 0:
        print("[결과] 아웃")
    else:
        print("[결과]", strike, " 스트라이크 ", ball, " 볼")
    if strike == 3:
        print("[결과] 3 스트라이크!")
        print(f"축하합니다! {attemps}번 만에 맞히셨습니다")
        break