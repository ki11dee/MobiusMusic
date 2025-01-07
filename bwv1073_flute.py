from music21 import stream, note

# 첼로 성부 정의
flute = stream.Part()

# 마디 1
measure1 = stream.Measure()
measure1.append(note.Rest(quarterLength=4))

# 마디 2
measure2 = stream.Measure()
measure2.append(note.Rest(quarterLength=2))
measure2.append(note.Note('A2', quarterLength=1))
measure2.append(note.Note('A2', quarterLength=0.5))
measure2.append(note.Note('B2', quarterLength=0.5))

# ---------도돌이표--------
repeat_section = stream.Measure()

# 반복 마디 1
repeat_section.append(note.Note('E3', quarterLength=1))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=0.5))
repeat_section.append(note.Note('A3', quarterLength=0.25))
repeat_section.append(note.Note('G3', quarterLength=0.25))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))

# 반복 마디 2
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('C3', quarterLength=2.0)) # 다음 마디에서 이어짐

# 반복 마디 3
repeat_section.append(note.Note('C3', quarterLength=0.5)) # 끝
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=1.5))
repeat_section.append(note.Note('G3', quarterLength=0.5))

# 반복 마디 4
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=0.5))
repeat_section.append(note.Note('A3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=0.25))
repeat_section.append(note.Note('F3', quarterLength=0.25))

# 반복 마디 5
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('C3', quarterLength=1))
repeat_section.append(note.Note('G3', quarterLength=1.5))
repeat_section.append(note.Note('F3', quarterLength=0.25))
repeat_section.append(note.Note('E3', quarterLength=0.25))

# 반복 마디 6
repeat_section.append(note.Note('D3', quarterLength=1))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=1))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=0.5))

# 반복 마디 7
repeat_section.append(note.Note('A3', quarterLength=0.5))
repeat_section.append(note.Note('B3', quarterLength=0.5))
repeat_section.append(note.Note('C4', quarterLength=0.5))
repeat_section.append(note.Note('B3', quarterLength=0.25))
repeat_section.append(note.Note('A3', quarterLength=0.25))
repeat_section.append(note.Note('G3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('D3', quarterLength=0.25))
repeat_section.append(note.Note('C3', quarterLength=0.25))

# 반복 마디 8
repeat_section.append(note.Note('B2', quarterLength=0.5))
repeat_section.append(note.Note('A2', quarterLength=0.5))
repeat_section.append(note.Note('G2', quarterLength=1))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))
repeat_section.append(note.Note('G3', quarterLength=0.5))

# 반복 마디 9
repeat_section.append(note.Note('A3', quarterLength=1.5))
repeat_section.append(note.Note('B3', quarterLength=0.5))
repeat_section.append(note.Note('C4', quarterLength=1.5))
repeat_section.append(note.Note('B3', quarterLength=0.25))
repeat_section.append(note.Note('A3', quarterLength=0.25))

# 반복 마디 10
repeat_section.append(note.Note('G3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.25))
repeat_section.append(note.Note('E3', quarterLength=0.25))
repeat_section.append(note.Note('D3', quarterLength=1.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=1.0)) # 다음 마디에서 이어짐

# 반복 마디 11
repeat_section.append(note.Note('F3', quarterLength=0.5)) # 끝
repeat_section.append(note.Note('E3', quarterLength=0.25))
repeat_section.append(note.Note('D3', quarterLength=0.25))
repeat_section.append(note.Note('C3', quarterLength=1.5))
repeat_section.append(note.Note('D3', quarterLength=0.5))
repeat_section.append(note.Note('E3', quarterLength=0.5))
repeat_section.append(note.Note('F3', quarterLength=0.5))

# 반복 마디 12
repeat_section.append(note.Note('G3', quarterLength=1))
repeat_section.append(note.Note('G2', quarterLength=0.5))
repeat_section.append(note.Note('A2', quarterLength=0.5))
repeat_section.append(note.Note('B2', quarterLength=0.5))
repeat_section.append(note.Note('C3', quarterLength=0.5))
repeat_section.append(note.Note('D3', quarterLength=1))

# 반복 마디 13
repeat_section_end = stream.Measure()
repeat_section_end.append(note.Rest(quarterLength=2)) # 쉼
repeat_section_end.append(note.Note('C3', quarterLength=1))
repeat_section_end.append(note.Note('C3', quarterLength=0.5))
repeat_section_end.append(note.Note('D3', quarterLength=0.5))

# ---------도돌이표 종료--------

flute.append(measure1)
flute.append(measure2)
flute.repeatAppend(repeat_section, 2)  # 도돌이표 부분 2번 반복
flute.append(repeat_section_end)

# 마디 3
measure3 = stream.Measure()
flute.append(note.Note('E3', quarterLength=1))
flute.append(note.Note('E3', quarterLength=0.5))
flute.append(note.Note('F3', quarterLength=0.5))
flute.append(note.Note('G3', quarterLength=4))

flute.append(measure3)

from transpose_function2 import transpose_part_handle_sharp_and_flat

flute_mod = transpose_part_handle_sharp_and_flat(flute, 20)

# flute_mod.show('text')
# flute_mod.show('midi')