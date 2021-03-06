# 구현(Implementation)
* 머리속에 있는 알고리즘을 소스코드로 바꾸는 과정
* 파이썬에서의 실수형 변수는 다른 언어와 마찬가지로 유효숫자에 따라서 연산 결과가 원하는 값이 나오지 않을 수 있다.
* 파이썬은 다른 언어에 비해서 구현상의 복잡함이 적은 편이지만 데이터 처리량이 많을 때는 꼭 메모리 제한을 고려하자

<br>

* int 자료형 데이터의 개수에 따른 메모리 사용량

|데이터의 개수(리스트의 길이)|메모리 사용량|
|-----|---|
|1,000|약 4KB|
|1,000,000|약 4MB|
|10,000,000|약 40MB|
* 일반적인 기업 코딩 테스트 환경에서는 파이썬으로 제출한 코드가 1초에 2,000만 번의 연산을 수행한다고 가정하면 크게 무리가 없다.
* $N = 1,000,000$일 때 $Nlog_2N$은 약 20,000,000정도 된다.
---
## 까다로운 유형
* 알고리즘은 간단한데 코드가 지나치게 길어지는 문제
* 특정 소수점 자리까지 출력해야 하는 문제
* 문자열이 입력으로 주어졌을 때 한 문자 단위로 끊어서 리스트에 넣어야 하는(파싱을 해야 하는) 문제
#### 대체로 사소한 조건 설정이 많은 문제일수록 코드로 구현하기가 까다롭다.

<br>

---
## 완전탐색
* 모든 경우의 수를 다 계산하는 해결 방법

<br>

---
## 시뮬레이션
* 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행

