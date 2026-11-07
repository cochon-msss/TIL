# 1단계: 틀린 만큼 조금씩 고친다 (경사하강)
# 실행: python3 llm/code/01_gradient_descent.py
import numpy as np

# 1. 사과값 하나 맞히기: 사과 3개 = 3000원
print("== 사과값 하나 맞히기 ==")
guess = 500                          # 대충 찍고 시작
for i in range(10):
    diff = guess * 3 - 3000          # 얼마나 틀렸나 (마이너스면 업, 플러스면 다운)
    print(f"{round(guess)}원이라고 생각함, 차이: {round(diff)}")
    guess = guess - diff * 0.1       # 차이 반대로 조금 고치기

# 2. 한 번에 얼마나 크게 고칠지(학습률)를 바꿔보기
print("\n== 학습률 비교 ==")
for lr in [0.01, 0.1, 0.5, 0.7]:
    guess, history = 500, []
    for i in range(8):
        history.append(round(guess))
        guess = guess - (guess * 3 - 3000) * lr
    print(f"{lr}: {history}")

# 3. 사과값, 우유값 둘 다 맞히기: 많이 들어간 쪽이 많이 고친다
print("\n== 사과값, 우유값 둘 다 맞히기 ==")
data = [((2, 1), 4000),              # 사과 2 + 우유 1 = 4000
        ((1, 3), 7000)]              # 사과 1 + 우유 3 = 7000
apple, milk = 500, 500
for step in range(1, 201):
    for (n_apple, n_milk), answer in data:
        diff = n_apple * apple + n_milk * milk - answer
        apple = apple - diff * n_apple * 0.02
        milk = milk - diff * n_milk * 0.02
    if step in (1, 5, 10, 50, 200):
        print(f"{step}회: 사과 {round(apple)}, 우유 {round(milk)}")

# 4. 추론: 학습으로 찾은 값은 고정하고 계산만 한다
print("\n== 추론 ==")
print("사과 4 + 우유 2 =", 4 * round(apple) + 2 * round(milk))

# 5. LLM의 틀린 정도: 정답에 준 확률이 낮을수록 벌점(손실)이 크다
print("\n== 확률 → 벌점 ==")
for p in [1.0, 0.9, 0.5, 0.1, 0.01]:
    print(f"정답에 {p:.0%} → 벌점 {-np.log(p) + 0.0:.1f}")
