import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from music21 import stream, note, midi, instrument
from threading import Thread
from time import time, sleep
from pygame import mixer

# 뫼비우스 띠의 파라메트릭 방정식
def mobius_coords(u, v):
    x = (1 + v * np.cos(u / 2)) * np.cos(u)
    y = (1 + v * np.cos(u / 2)) * np.sin(u)
    z = v * np.sin(u / 2)
    return x, y, z

# 12음계 배열과 quarterLength 설정
notes_with_lengths = [
    # 마디 1
    ('C3', 1), ('C3', 0.5), ('D3', 0.5), ('E3', 1), ('E3', 0.5), ('F3', 0.5),
    
    # 마디 2
    ('G3', 0.5), ('A3', 0.25), ('G3', 0.25), ('F3', 0.5), ('E3', 0.5),
    ('D3', 0.5), ('F3', 0.5), ('E3', 0.5), ('D3', 0.5),

    # 반복 마디 1
    ('C3', 2.5), ('D3', 0.5), ('E3', 0.5), ('F3', 0.5),

    # 반복 마디 2
    ('G3', 1.5), ('G3', 0.5), ('F3', 0.5), ('E3', 0.5), ('D3', 0.5), ('E3', 0.5),

    # 반복 마디 3
    ('F3', 0.5), ('G3', 0.5), ('A3', 0.5), ('G3', 0.25), ('F3', 0.25),
    ('E3', 0.5), ('D3', 0.5), ('C3', 1),

    # 반복 마디 4
    ('G3', 1.5), ('F3', 0.25), ('E3', 0.25), ('D3', 1), ('D3', 0.5), ('E3', 0.5),

    # 반복 마디 5
    ('F3', 1), ('F3', 0.5), ('G3', 0.5), ('A3', 0.5), ('B3', 0.5),
    ('C4', 0.5), ('B3', 0.25), ('A3', 0.25),

    # 반복 마디 6
    ('G3', 0.5), ('F3', 0.5), ('E3', 0.5), ('D3', 0.25), ('C3', 0.25),
    ('B2', 0.5), ('A2', 0.5), ('G2', 1),

    # 반복 마디 7
    ('D3', 0.5), ('E3', 0.5), ('F3', 0.5), ('G3', 0.5), ('A3', 1.5), ('B3', 0.5),

    # 반복 마디 8
    ('C4', 1.5), ('B3', 0.25), ('A3', 0.25), ('G3', 0.5), ('F3', 0.25),
    ('E3', 0.25), ('D3', 1),

    # 반복 마디 9
    ('D3', 0.5), ('E3', 0.5), ('F3', 1.5), ('E3', 0.25), ('D3', 0.25), ('C3', 1),

    # 반복 마디 10
    ('C3', 0.5), ('D3', 0.5), ('E3', 0.5), ('F3', 0.5), ('G3', 1), ('G2', 0.5), ('A2', 0.5),

    # 반복 마디 11
    ('B2', 0.5), ('C3', 0.5), ('D3', 1), ('Rest', 2),

    # 반복 마디 12
    ('C3', 1), ('C3', 0.5), ('D3', 0.5), ('E3', 1), ('E3', 0.5), ('F3', 0.5),

    # 반복 마디 13
    ('G3', 0.5), ('A3', 0.25), ('G3', 0.25), ('F3', 0.5), ('E3', 0.5),
    ('D3', 0.5), ('F3', 0.5), ('E3', 0.5), ('D3', 0.5),

    # 도돌이 끝난 후
    ('C3', 2), ('C3', 4)
]


# 음과 위치 매핑
def calculate_note_positions():
    num_notes = len(notes_with_lengths)
    u_positions = np.linspace(0, 2 * np.pi, num_notes, endpoint=False)
    v = 0  # 뫼비우스 띠의 중앙에 고정
    positions = {}
    for i, u in enumerate(u_positions):
        x, y, z = mobius_coords(u, v)
        positions[notes_with_lengths[i][0]] = (x, y, z)
    return positions

note_positions = calculate_note_positions()

# 음악 생성
def create_music(notes_with_lengths):
    """
    notes_with_lengths 데이터를 기반으로 Stream 객체 생성.
    쉼표는 'Rest'로 처리.
    """
    melody = stream.Stream()
    for note_name, length in notes_with_lengths:
        if note_name == 'Rest':  # 쉼표 처리
            melody.append(note.Rest(quarterLength=length))
        else:  # 음표 처리
            melody.append(note.Note(note_name, quarterLength=length))
    return melody


melody = create_music(notes_with_lengths)

# 음악 재생 함수
def play_music():
    mf = midi.translate.music21ObjectToMidiFile(melody)
    mf.open('melody.mid', 'wb')
    mf.write()
    mf.close()

    mixer.init()
    mixer.music.load('melody.mid')
    mixer.music.play()

# 3D 시각화 설정
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# 뫼비우스 띠 표면
u_vals = np.linspace(0, 2 * np.pi, 100)
v_vals = np.linspace(-0.5, 0.5, 10)
u, v = np.meshgrid(u_vals, v_vals)
x, y, z = mobius_coords(u, v)
ax.plot_surface(x, y, z, color='cyan', alpha=0.6, edgecolor='k')

# 초기 음표 위치
highlight, = ax.plot([], [], [], 'ro', markersize=10)

# 애니메이션 업데이트를 위한 전역 변수
start_time = None
current_index = 0

# 애니메이션 업데이트 함수
def update(frame):
    global start_time, current_index

    # 애니메이션 시작 시간 설정
    if start_time is None:
        start_time = time()

    # 현재 시간 계산
    elapsed_time = time() - start_time

    # 현재 출력할 음표 찾기
    total_time = 0
    for i, (_, length) in enumerate(notes_with_lengths):
        total_time += length * 0.5  # quarterLength를 초로 변환
        if elapsed_time <= total_time:
            current_index = i
            break

    # 현재 음표의 좌표 계산
    current_note, _ = notes_with_lengths[current_index]
    x, y, z = note_positions[current_note]
    highlight.set_data([x], [y])
    highlight.set_3d_properties([z])

    return highlight,

# 음악 재생 스레드
music_thread = Thread(target=play_music)
music_thread.daemon = True
music_thread.start()

# 애니메이션 실행
ani = FuncAnimation(
    fig,
    update,
    frames=len(notes_with_lengths) * 4,  # 임의로 충분히 큰 값
    interval=10,  # 짧은 간격으로 프레임을 빠르게 갱신
    blit=False
)

plt.show()
