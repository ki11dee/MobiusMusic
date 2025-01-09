import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from music21 import stream, note, midi, chord
from threading import Thread
from time import time, sleep
from pygame import mixer

# 기존 뫼비우스 띠 좌표 계산 함수
def mobius_coords(u, v):
    """
    뫼비우스 띠의 파라메트릭 방정식 (u, v)
    """
    x = (1 + v * np.cos(u / 2)) * np.cos(u)
    y = (1 + v * np.cos(u / 2)) * np.sin(u)
    z = v * np.sin(u / 2)
    return x, y, z

# 새로운 파라메트릭 방정식: 회전 이동
def rotated_mobius_coords(u, v, shift):
    """
    기존 뫼비우스 좌표를 회전 이동 (shift만큼 u를 이동)
    """
    u_rotated = u + shift  # u 값을 shift만큼 이동
    return mobius_coords(u_rotated, v)

# 4개의 기존 리스트 정의
chords_edge = [
    ('F#', 'F#'), ('G', 'G'), ('G#', 'G#'), ('A', 'A'), ('A#', 'A#'),
    ('B', 'B'), ('C', 'C'), ('C#', 'C#'), ('D', 'D'), ('D#', 'D#'),
    ('E', 'E'), ('F', 'F')
]

chords_list1 = [
    ('G', 'F'), ('G#', 'F#'), ('A', 'G'), ('A#', 'G#'), ('B', 'A'),
    ('C', 'A#'), ('C#', 'B'), ('D', 'C'), ('D#', 'C#'),
    ('E', 'D'), ('F', 'D#'), ('F#', 'E')
]

chords_list2 = [
    ('G#', 'E'), ('A', 'F'), ('A#', 'F#'), ('B', 'G'), ('C', 'G#'),
    ('C#', 'A'), ('D', 'A#'), ('D#', 'C'), ('E', 'C'),
    ('F', 'C#'), ('F#', 'D'), ('G', 'D#')
]

chords_list3 = [
    ('A', 'D#'), ('A#', 'E'), ('B', 'F'), ('C', 'F#'), ('C#', 'G'),
    ('D', 'G#'), ('D#', 'A'), ('A', 'D#'), ('A#', 'E'), ('B', 'F'),
    ('C', 'F#'), ('C#', 'G'), ('D', 'G#')
]

# 추가 리스트 정의
chords_list4 = [
    ('G', 'F#'), ('G#', 'G'), ('A', 'G#'), ('A#', 'A'), ('B', 'A#'),
    ('C', 'B'), ('C#', 'C'), ('D', 'C#'), ('D#', 'D'), ('E', 'D#'),
    ('F', 'E'), ('F#', 'F')
]

chords_list5 = [
    ('G#', 'F'), ('A', 'F#'), ('A#', 'G'), ('B', 'G#'), ('C', 'A'),
    ('C#', 'A#'), ('B', 'D'), ('D#', 'C'), ('E', 'D#'), ('F', 'D'),
    ('F#', 'D#'), ('G', 'E')
]

chords_list6 = [
    ('A', 'E'), ('A#', 'F'), ('B', 'F#'), ('C', 'G'), ('C#', 'G#'),
    ('D', 'A'), ('D#', 'A#'), ('E', 'B'), ('F', 'C'), ('F#', 'C#'),
    ('G', 'D'), ('G#', 'D#')
]

# 좌표 계산 함수 (기존 및 회전 이동)
def calculate_positions(chords, num_points=12, v_offset=0.3, shift=0.0):
    u_positions = np.linspace(0, 4 * np.pi, num_points, endpoint=False)
    positions = {}
    for i, u in enumerate(u_positions):
        x, y, z = rotated_mobius_coords(u, v=v_offset, shift=shift)
        positions[chords[i]] = (x, y, z)
    return positions

# 기존 리스트의 좌표 계산
edge_positions = calculate_positions(chords_edge, v_offset=0.3)
list1_positions = calculate_positions(chords_list1, v_offset=0.2)
list2_positions = calculate_positions(chords_list2, v_offset=0.1)
list3_positions = calculate_positions(chords_list3, v_offset=0.0)

# 추가 리스트의 좌표 계산 (회전 이동 적용)
list4_positions = calculate_positions(chords_list4, v_offset=0.25, shift=0.5)
list5_positions = calculate_positions(chords_list5, v_offset=0.15, shift=0.5)
list6_positions = calculate_positions(chords_list6, v_offset=0.05, shift=0.5)

# 3D 시각화 설정
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# 뫼비우스 띠 표면
u_vals = np.linspace(0, 4 * np.pi, 200)
v_vals = np.linspace(-0.3, 0.3, 20)
u, v = np.meshgrid(u_vals, v_vals)
x, y, z = mobius_coords(u, v)
ax.plot_surface(x, y, z, color='cyan', alpha=0.3, edgecolor='k')

# 모든 리스트의 화음 텍스트 표시
for positions, color in zip(
    [edge_positions, list1_positions, list2_positions, list3_positions, list4_positions, list5_positions, list6_positions],
    ['red', 'blue', 'green', 'purple', 'orange', 'pink', 'yellow']
):
    for chords, (x, y, z) in positions.items():
        ax.text(x, y, z, f"{chords[0]}-{chords[1]}", color=color, fontsize=8, ha='center')

# 그래프 설정
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# 화음 텍스트 고정
for chords, (x, y, z) in edge_positions.items():
    ax.text(x, y, z, f"{chords[0]}-{chords[1]}", color='red', fontsize=10, ha='center')


# ---------------------------------------------


plt.show()
