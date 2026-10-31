# 0단계: 파이썬 + numpy 기초
# 실행: python3 llm/code/00_python_numpy.py
import numpy as np

# 1. 토큰 리스트와 "앞부분 보고 다음 칸 맞히기"
tokens = ["나는", "밥을", "먹었다"]
print("앞부분:", tokens[0:2], "→ 맞힐 것:", tokens[2])

# 2. 글자 ↔ 숫자 사전 (stoi / itos는 관습적인 변수 이름)
stoi = {w: i for i, w in enumerate(tokens)}   # 글자 → 숫자
itos = {i: w for w, i in stoi.items()}        # 숫자 → 글자

def encode(ws):
    return [stoi[w] for w in ws]

def decode(ids):
    return [itos[i] for i in ids]

ids = encode(tokens)
print("encode:", ids, "→ decode:", decode(ids))

# 3. numpy는 묶음 전체를 한 번에 계산한다
a = np.array([1, 2, 3])
print("리스트 * 2:", [1, 2, 3] * 2, "/ numpy * 2:", a * 2)

# 4. 임베딩 표: 토큰마다 숫자 한 줄. 번호로 행을 꺼낸다
emb = np.array([
    [0.2, -0.5, 0.9],   # 나는
    [0.7, 0.1, -0.3],   # 밥을
    [-0.4, 0.8, 0.6],   # 먹었다
])
print("emb.shape:", emb.shape)
print("emb[encode(...)]:\n", emb[ids])

# 5. 행렬 곱셈 = 장보기 영수증 계산 (같은 칸끼리 곱해서 더하기)
count = np.array([3, 1, 2])            # 사과, 우유, 빵 개수
prices = np.array([[1000, 900],        # A마트, B마트
                   [2000, 2500],
                   [1500, 1000]])
print("총액 (A마트, B마트):", count @ prices)

# 6. 행렬 곱셈 = 후보 토큰마다 점수 매기기
state = np.array([0.9, 0.1])           # 지금 상황: [음식 얘기?, 사람 얘기?]
candidates = ["나는", "먹었다", "잤다"]
table = np.array([[0.0, 1.0, 0.0],     # 음식 얘기에 어울리는 정도
                  [1.0, 0.0, 0.5]])    # 사람 얘기에 어울리는 정도
scores = state @ table
probs = scores / scores.sum()          # 실제로는 softmax를 쓴다. 지금은 비율로
for w, s, p in zip(candidates, scores, probs):
    print(f"{w}: 점수 {s:.2f}, 확률 {p:.0%}")
print("고른 토큰:", candidates[int(np.argmax(probs))])
