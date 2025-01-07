from music21 import stream, note, instrument

# 첼로 성부 정의
cello = stream.Part()

# 마디 1
measure1 = stream.Measure()
measure1.append(note.Note('C3', quarterLength=1))
measure1.append(note.Note('C3', quarterLength=0.5))
measure1.append(note.Note('D3', quarterLength=0.5))
measure1.append(note.Note('E3', quarterLength=1))
measure1.append(note.Note('E3', quarterLength=0.5))
measure1.append(note.Note('F3', quarterLength=0.5))

# 마디 2
measure2 = stream.Measure()
measure2.append(note.Note('G3', quarterLength=0.5))
measure2.append(note.Note('A3', quarterLength=0.25))
measure2.append(note.Note('G3', quarterLength=0.25))
measure2.append(note.Note('F3', quarterLength=0.5))
measure2.append(note.Note('E3', quarterLength=0.5))
measure2.append(note.Note('D3', quarterLength=0.5))
measure2.append(note.Note('F3', quarterLength=0.5))
measure2.append(note.Note('E3', quarterLength=0.5))
measure2.append(note.Note('D3', quarterLength=0.5))

# ---------도돌이표--------
repeat_section = stream.Measure()

# 반복 마디 1
repeat_section.append(note.Note('C3', quarterLength=2.5))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))

# 반복 마디 2
repeat_section.append(note.Note('G3', quarterLength=1.5))
repeat_section.append(note.Note('G3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))

# 반복 마디 3
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=0.5))
repeat_section.append(note.Note('A3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=0.25))
repeat_section.append(note.Note('F3', quarterLength=0.25))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('C3', quarterLength=1))

# 반복 마디 4
repeat_section.append(note.Note('G3', quarterLength=1.5))
repeat_section.append(note.Note('F3', quarterLength=0.25))
repeat_section.append(note.Note('E3', quarterLength=0.25))
repeat_section.append(note.Note('D3', quarterLength=1))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))

# 반복 마디 5
repeat_section.append(note.Note('F3', quarterLength=1))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=0.5))
repeat_section.append(note.Note('A3', quarterLength=0.5))
repeat_section.append(note.Note('B3', quarterLength=0.5))
repeat_section.append(note.Note('C4', quarterLength=0.5))
repeat_section.append(note.Note('B3', quarterLength=0.25))
repeat_section.append(note.Note('A3', quarterLength=0.25))

# 반복 마디 6
repeat_section.append(note.Note('G3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('D3', quarterLength=0.25))
repeat_section.append(note.Note('C3', quarterLength=0.25))
repeat_section.append(note.Note('B2', quarterLength=0.5))
repeat_section.append(note.Note('A2', quarterLength=0.5))
repeat_section.append(note.Note('G2', quarterLength=1))

# 반복 마디 7
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=0.5))
repeat_section.append(note.Note('A3', quarterLength=1.5))
repeat_section.append(note.Note('B3', quarterLength=0.5))

# 반복 마디 8
repeat_section.append(note.Note('C4', quarterLength=1.5))
repeat_section.append(note.Note('B3', quarterLength=0.25))
repeat_section.append(note.Note('A3', quarterLength=0.25))
repeat_section.append(note.Note('G3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.25))
repeat_section.append(note.Note('E3', quarterLength=0.25))
repeat_section.append(note.Note('D3', quarterLength=1)) #다음 마디에서 이어짐

# 반복 마디 9
repeat_section.append(note.Note('D3', quarterLength=0.5)) # 끝
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=1.5))
repeat_section.append(note.Note('E3', quarterLength=0.25))
repeat_section.append(note.Note('D3', quarterLength=0.25))
repeat_section.append(note.Note('C3', quarterLength=1)) # 다음 마디에서 이어짐

# 반복 마디 10
repeat_section.append(note.Note('C3', quarterLength=0.5)) # 끝
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=1))
repeat_section.append(note.Note('G2', quarterLength=0.5))
repeat_section.append(note.Note('A2', quarterLength=0.5))

# 반복 마디 11
repeat_section.append(note.Note('B2', quarterLength=0.5))
repeat_section.append(note.Note('C3', quarterLength=0.5))
repeat_section.append(note.Note('D3', quarterLength=1))
repeat_section.append(note.Rest(quarterLength=2)) # 쉼

# 반복 마디 12
repeat_section.append(note.Note('C3', quarterLength=1))
repeat_section.append(note.Note('C3', quarterLength=0.5))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=1))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))

# 반복 마디 13
repeat_section_end = stream.Measure()
repeat_section_end.append(note.Note('G3', quarterLength=0.5))
repeat_section_end.append(note.Note('A3', quarterLength=0.25))
repeat_section_end.append(note.Note('G3', quarterLength=0.25))
repeat_section_end.append(note.Note('F3', quarterLength=0.5))
repeat_section_end.append(note.Note('E3', quarterLength=0.5))
repeat_section_end.append(note.Note('D3', quarterLength=0.5))
repeat_section_end.append(note.Note('F3', quarterLength=0.5))
repeat_section_end.append(note.Note('E3', quarterLength=0.5))
repeat_section_end.append(note.Note('D3', quarterLength=0.5))

# ---------도돌이표 종료--------

cello.append(measure1)
cello.append(measure2)
cello.repeatAppend(repeat_section, 2)  # 도돌이표 부분 2번 반복
cello.append(repeat_section_end)

# 마디 3
measure3 = stream.Measure()
measure3.append(note.Note('C3', quarterLength=2))
measure3.append(note.Note('C3', quarterLength=4))

cello.append(measure3)


# cello.show('text')
# cello.show('midi')