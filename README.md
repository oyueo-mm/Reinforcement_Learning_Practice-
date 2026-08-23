# Reinforcement Learning Practice

강화학습을 공부하면서 구현하고 실험한 내용을 정리한 저장소입니다.

7×7 격자 환경을 직접 구성하고, 같은 환경에서 MC(Monte Carlo)와 TD(Temporal Difference) 방법을 적용해 보았습니다.

## 구현

### Monte Carlo

MC 방법을 이용해 에피소드가 끝난 뒤 얻은 경험을 바탕으로 가치 함수를 업데이트합니다.

### Temporal Difference

TD 방법을 이용해 다음 상태의 가치 추정값을 사용하면서 에피소드가 끝나기 전에 가치 함수를 업데이트합니다.

## 환경

- Grid World
- 7×7 Grid
- 상태(State)
- 행동(Action)
- 보상(Reward)

## 구조

```text
Reinforcement_Learning_Practice-/
├── MC/
├── TD/
└── README.md
