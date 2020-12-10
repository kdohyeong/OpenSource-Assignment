import pandas as pd
from matplotlib import font_manager,rc
import matplotlib
import matplotlib.pyplot as plt

# 한글 폰트 사용
font_path = "C:/Windows/Fonts/H2GTRM.TTF"
font_name = font_manager.FontProperties(fname=font_path).get_name()

matplotlib.rc('font',family=font_name)

# df는 경기도 자전거 공기주입기 설치위치 데이터
df = pd.read_csv("dataset.csv", encoding="CP949")
# print(df.columns)

## 구 데이터 추출
contry_gu = df['구']

## 동 데이터 추출
contry_dong = df['동']

## 위치 데이터 추출
contry_location = df['설치위치']

# 잘 들어갔는지 확인
print('\n구 데이터\n')
print(contry_gu)

print('\n동 데이터\n')
print(contry_dong)

print('\n위치 데이터\n')
print(contry_location)

## 구별 설치 개수 그리기
plt.hist(contry_gu, bins=100)
plt.xlabel('구별')
plt.ylabel('설치 개수')

# 프롬프트 창에 구별 개수 출력
print('\n구 별 설치 개수\n')
print(df.groupby('구')['설치위치'].nunique())

plt.show()

## 동별 설치 개수 그리기
plt.hist(contry_dong, bins=100, rwidth=0.1)
plt.xticks(rotation=45)
plt.xlabel('동별')
plt.ylabel('설치 개수')

# 프롬프트 창에 동별 설치 개수 출력
print('\n동 별 설치 개수\n')
print(df.groupby('동')['설치위치'].nunique())

plt.show()

## 구 별로 데이터를 따로 추출
bundang = df[df['구'] == '분당구']
sujung = df[df['구'] == '수정구']
jungone = df[df['구'] == '중원구']
gu_dong_location = df[['구', '동', '설치위치']]


print('\n분당구 내 설치 개수 데이터\n')
print(bundang.groupby('구')['설치위치'].nunique())

print('\n수정구 내 설치 개수 데이터\n')
print(sujung.groupby('구')['설치위치'].nunique())

print('\n중원구 내 설치 개수 데이터\n')
print(jungone.groupby('구')['설치위치'].nunique())

print('\n정확한 위치 데이터\n')
print(gu_dong_location)
