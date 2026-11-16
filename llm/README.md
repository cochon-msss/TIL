# LLM 직접 만들기

간단한 거라도 LLM을 직접 구현해서 문장을 쓰게 만드는 게 목표다. 선행학습부터 천천히 가고, 성공할 때까지 과정을 여기 남긴다.

시작 전에 본 것: [LLM과 토큰](token.md)

## 진행 상황

| 단계 | 내용 | 노트 | 코드 | 상태 |
|---|---|---|---|---|
| 0 | 파이썬 · numpy | [노트](00-python-numpy.md) | [코드](code/00_python_numpy.py) | ✅ 2026-10-31 |
| 1 | 틀린 만큼 조금씩 고친다 (경사하강) | [노트](01-gradient-descent.md) | [코드](code/01_gradient_descent.py) | ✅ 2026-11-08 |
| 2 | 경사는 컴퓨터가 구해준다 (backward) | [노트](02-autograd.md) | [코드](code/02_autograd.py) | ✅ 2026-11-16 |
| 3 | 글자 → 다음 글자 맞히기 (바이그램) | [노트](03-bigram.md) | [코드](code/03_bigram.py) | ✅ 2026-11-16 |
| 4 | 임베딩 · MLP | | | |
| 5 | 어텐션 | | | |
| 6 | 작은 GPT 조립 → 문장 생성 | | | |

## 환경

- Mac (Apple Silicon), Python 3.9.6, numpy 2.0.2
- PyTorch 2.8.0 (시스템 파이썬에 이미 깔려 있었다)
- 이름 데이터: `curl -L -o llm/data/names.txt https://raw.githubusercontent.com/karpathy/makemore/master/names.txt` (영어 이름 32,033개)
- 학습 데이터와 모델 파일은 크니까 커밋하지 않는다 (`llm/data/`, `*.pt`)
