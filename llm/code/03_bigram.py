# 3단계: 글자 → 다음 글자 맞히기 (바이그램)
# 실행: python3 llm/code/03_bigram.py
# 이름 데이터 받기 (커밋 안 함):
#   curl -L -o llm/data/names.txt https://raw.githubusercontent.com/karpathy/makemore/master/names.txt
import random
from collections import Counter
import torch


def count_pairs(words):
    pairs = Counter()
    for w in words:
        w = '.' + w + '.'                    # .은 시작/끝 표시
        for a, b in zip(w, w[1:]):           # "엄마" → ('.','엄') ('엄','마') ('마','.')
            pairs[(a, b)] += 1
    return pairs


def make_word(pairs):
    ch, out = '.', ''
    while True:
        cands = [(b, n) for (a, b), n in pairs.items() if a == ch]
        ch = random.choices([b for b, n in cands], [n for b, n in cands])[0]   # 확률대로 주사위
        if ch == '.':
            return out
        out += ch


# 1. 이 글자 뒤에 뭐가 자주 왔나 세기
print("== 세기 ==")
print(count_pairs(['엄마', '엄마', '엄지']))

# 2. 확률대로 주사위 굴려서 이어 붙이기
print("\n== 단어 세 개로 짓기 ==")
random.seed(0)
pairs = count_pairs(['엄마', '마루', '엄지'])
print([make_word(pairs) for _ in range(8)])     # 엄마루는 원래 없던 단어

# 3. 이름 32,033개로 짓기 vs 아무렇게나 뽑기
print("\n== 이름 짓기 ==")
words = open('llm/data/names.txt').read().split()
pairs = count_pairs(words)
random.seed(0)
print("바이그램:  ", [make_word(pairs) for _ in range(10)])
letters = 'abcdefghijklmnopqrstuvwxyz.'
randoms = []
for _ in range(5):
    out = ''
    while (ch := random.choice(letters)) != '.':  # 표 없이 아무 글자나
        out += ch
    randoms.append(out)
print("아무렇게나:", randoms)

# 4. 세지 않고 학습해도 같은 확률이 나온다
print("\n== 학습으로 엄 다음 글자 맞히기 ==")
score = torch.zeros(2, requires_grad=True)       # [마, 지] 점수, 처음엔 똑같이 0
answers = [0, 0, 1]                              # 엄 다음 정답: 마, 마, 지
for step in range(51):
    prob = score.softmax(0)                      # 점수 → 확률
    loss = -prob[answers].log().mean()           # 정답에 준 확률로 벌점
    if step in (0, 1, 3, 10, 50):
        print(f'{step}회: 마 {prob[0].item():.0%}, 지 {prob[1].item():.0%}, 벌점 {loss.item():.3f}')
    loss.backward()                              # 경사는 컴퓨터가
    with torch.no_grad():
        score -= score.grad * 0.5                # 경사만큼 반대로 고치기
    score.grad.zero_()
