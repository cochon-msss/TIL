# 2단계: 경사는 컴퓨터가 구해준다 (backward)
# 실행: python3 llm/code/02_autograd.py
import torch

# 1. 사과 2개 + 우유 1개: 누가 얼마나 영향을 줬나 물어보기
print("== backward()로 영향 물어보기 ==")
apple = torch.tensor(500.0, requires_grad=True)   # "얘 영향 알고 싶어" 표시
milk = torch.tensor(500.0, requires_grad=True)
total = 2 * apple + 1 * milk
total.backward()                                  # 누가 얼마나 영향 줬어?
print("사과 영향:", apple.grad.item())             # 1단계에서 손으로 정한 2
print("우유 영향:", milk.grad.item())              # 1단계에서 손으로 정한 1

# 2. 1단계 사과·우유 맞히기를 backward()로 다시 하기
print("\n== 1단계를 backward()로 다시 ==")
data = [((2, 1), 4000),                           # 사과 2 + 우유 1 = 4000
        ((1, 3), 7000)]                           # 사과 1 + 우유 3 = 7000
apple = torch.tensor(500.0, requires_grad=True)
milk = torch.tensor(500.0, requires_grad=True)
for step in range(1, 201):
    for (n_apple, n_milk), answer in data:
        diff = n_apple * apple + n_milk * milk - answer
        (diff * diff / 2).backward()              # 영향 = 차이 × 개수, 컴퓨터가 구함
        with torch.no_grad():                     # 고치는 건 1단계와 같음
            apple -= apple.grad * 0.02
            milk -= milk.grad * 0.02
        apple.grad.zero_()                        # 다음 영수증 전에 비우기
        milk.grad.zero_()
    if step in (1, 10, 200):
        print(f"{step}회: 사과 {round(apple.item())}, 우유 {round(milk.item())}")
