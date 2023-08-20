import numpy as np
import matplotlib.pyplot as plt

# 원의 중심점과 반지름 정의
center = (3, 4)  # 중심점 좌표 (x, y)
radius = 2       # 반지름

# 원 그리기
circle = plt.Circle(center, radius, color='blue', fill=True)

# 그래프 설정
fig, ax = plt.subplots()
ax.set_aspect('equal')  # x, y축 비율을 같게 설정하여 원이 원형으로 보이도록 함
ax.add_artist(circle)
ax.set_xlim(0, 6)  # 그래프 x축 범위 설정
ax.set_ylim(0, 8)  # 그래프 y축 범위 설정

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Circle in 2D Matrix')
plt.grid(True)
plt.show()
